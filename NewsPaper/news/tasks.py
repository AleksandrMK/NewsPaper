from django.contrib.auth.models import User
from NewsPaper.celery import app
from celery import shared_task
import datetime

from news.models import Post, Category
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@app.task
def mailing():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_context = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )
    for email in subscribers:
        msg = EmailMultiAlternatives(
            subject='Статьи за неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        msg.attach_alternative(html_context, 'text/html')
        msg.send()


@shared_task
def generation_and_sending_mail(post_pk):  # Генерация и отправка письма
    instance = Post.objects.get(id=post_pk)
    emails = []
    for cat in instance.category.all():
        emails.extend(User.objects.filter(
            subscriber__category=cat
        ).values_list('email', flat=True))
    subject = f'Новая статья в категории'
    text_content = (
        f'Статья: {instance.header}\n'
        f'Ссылка на статью: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Статья: {instance.header}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
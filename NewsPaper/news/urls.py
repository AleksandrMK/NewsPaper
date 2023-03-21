from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, PostDelete, ArticlesList, PostList, \
   ArticlesDetail, NewsEdit, ArticlesEdit, ArticlesCreate, PostCreate, news, subscriptions

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('create/', news, name='create'),
   path('search/', NewsSearch.as_view(), name='search'),
   path('news/', NewsList.as_view(), name='news_list'),
   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('news/<int:pk>', NewsDetail.as_view(), name='one_news'),
   path('articles/<int:pk>', ArticlesDetail.as_view(), name='one_articles'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='news_edit'),
   path('news/<int:pk>/edit/', NewsEdit.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]

from django.forms import DateTimeInput
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category


class PostFilter(FilterSet):
    title = ModelChoiceFilter(
        field_name='Category',
        queryset=Category.objects.all(),
        label='Категории',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
        }

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        label='Date later than',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

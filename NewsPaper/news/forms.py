from django import forms
from .models import Post


class PostForms(forms.ModelForm):
    header = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'text', 'postCategory', 'author']

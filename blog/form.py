from dataclasses import fields
from django import forms
from .models import BlogApp

class BlogAppForm(forms.ModelForm):
    class Meta:
        model = BlogApp
        fields = [
            "title",
            "description"
        ]
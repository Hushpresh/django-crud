from audioop import reverse
from re import template
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import BlogApp, Post

class PostListView(ListView):
    model = Post
 
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailview(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

    template_name = 'templates'
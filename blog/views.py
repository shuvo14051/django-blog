from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy



class BlogListView(ListView):
    model = Post
    # context_obejct_name = 'posts'
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'blog/new.html'
    # fields = ('title','body')
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')



from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'login'
    # context_obejct_name = 'posts'
    template_name = 'blog/home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):  # new
    model = Post
    template_name = 'blog/new.html'
    # fields = ('title','body')
    fields = '__all__'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'body']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')

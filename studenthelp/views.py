from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Transport, HousingPost
from .forms import PostForm, TransportForm

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('post_list')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class TransportCreate(LoginRequiredMixin, CreateView):
    model = Transport
    form_class = TransportForm
    template_name = 'transport_create.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class HousingNewsFeed(ListView):
    model = HousingPost
    template_name = 'housing_news_feed.html'
    context_object_name = 'housing_posts'
    ordering = ['-created_at']

class CreateHousingPost(LoginRequiredMixin, CreateView):
    model = HousingPost
    fields = ['title', 'content']
    template_name = 'create_housing_post.html'
    success_url = '/housing-news/'  # Redirige vers la page du fil d'actualité après la création d'un post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    data = {
        'news': Posts.objects.all(),
        'title': 'Blog page'
    }
    return render(request, 'blog/home.html', data)


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class ShowNewsView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ShowNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class UserAllNewsView(ListView):
    model = Posts
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(UserAllNewsView, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class NewsDetailView(DetailView):
    model = Posts
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['title'] = Posts.objects.filter(pk=self.kwargs['pk']).first()
        return context


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


def contacts(request):
    return render(request, 'blog/contacts.html')

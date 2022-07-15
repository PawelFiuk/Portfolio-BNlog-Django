from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def articles_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, "articles/articles_list.html", {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) # tworzymy formularz nowego artykulu
        if form.is_valid():  # zapisz artykuł do db jeżeli wszystko jest ok
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article   # wybieramy model
    template_name = 'articles/article_update.html'
    fields = ['title', 'slug', 'body']  # wybieramy, co chcemy zmienic z modelu
    success_url = reverse_lazy('articles:list')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('articles:list')

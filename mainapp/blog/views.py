from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Article, Category, Comment,Fact
from .mixins import CategoryDetailMixin
from .forms import CommentForm


class MainListView(ListView):

    def get(self, request, *args, **kwargs):
        article = Article.objects.filter(is_active=True).order_by('-date')[:5]
        categories = Category.objects.all()
        facts = Fact.objects.filter(is_active=True)
        context = {
            'article': article,
            'categories': categories,
            'facts': facts,


        }
        return render(request, 'blog/article.html', context)


def post_detail(request, slug):
    article = Article.objects.get(slug__iexact=slug)
    categories = Category.objects.all()
    facts = Fact.objects.filter(is_active=True)
    # comments = article.comments.filter(is_active=True)
    # if request.method == 'POST':
    #     # A comment was posted
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # Create Comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.article = article
    #         # Save the comment to the database
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()
    context = {
        'article': article,
        'categories': categories,
        'facts': facts,
        # 'comments': comments,
        # 'comment_form': comment_form,
    }
    return render(request, 'blog/article_detail.html', context)


def search(request):
    query = request.GET.get('q')
    if query is not None:
        article = Article.objects.filter(
            Q(title__icontains=query) | Q(intro__icontains=query) | Q(date__icontains=query) | Q(body__icontains=query) | Q(slug__icontains=query),is_active=True).order_by('-date')
        categories = Category.objects.all()
        facts = Fact.objects.filter(is_active=True)
        context = {
            'article': article,
            'categories': categories,
            'facts': facts,

        }
        return render(request, 'blog/search.html', context)
    else:
        return redirect(request, 'blog/article.html')


class ArticleForCategoryList(ListView):

    def get(self, request, *args, **kwargs):
        article = Article.objects.filter(is_active=True,category__slug=self.kwargs.get('slug')).order_by('-date')
        paginator = Paginator(article, 3)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        categories = Category.objects.all()
        facts = Fact.objects.filter(is_active=True)
        context = {
            'article': page,
            'categories': categories,
            'facts': facts,
        }
        return render(request, 'blog/category_detail.html', context)


def contacts(request):
    categories = Category.objects.all()
    facts = Fact.objects.filter(is_active=True)
    context = {
        'categories': categories,
        'facts': facts,
    }
    return render(request, 'blog/contacts.html', context)


class FullArticlesListView(ListView):

    def get(self, request, *args, **kwargs):
        article = Article.objects.filter(is_active=True).order_by('-date')
        paginator = Paginator(article, 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        categories = Category.objects.all()
        facts = Fact.objects.filter(is_active=True)
        context = {
            'article': page,
            'categories': categories,
            'facts': facts,

        }
        return render(request, 'blog/full_article.html', context)




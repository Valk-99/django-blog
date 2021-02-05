from django.urls import path
from .views import *

urlpatterns = [
    path('', MainListView.as_view(), name='article'),
    path('articles/', FullArticlesListView.as_view(), name='full-articles'),
    path('article/<slug:slug>/', post_detail, name='article_detail'),
    path('search/', search, name='search_results'),
    path('category/<str:slug>/', ArticleForCategoryList.as_view(), name='category_detail'),
    path('contacts/', contacts, name='contacts'),
]
from django.contrib import admin
from .models import Article, Category, Comment, Fact


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','is_active', 'date', 'category', 'author')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Fact)
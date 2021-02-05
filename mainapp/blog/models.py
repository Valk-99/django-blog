from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=220, db_index=True, default=True)
    intro = models.CharField(max_length=255, verbose_name='Вводный текст')
    title = models.CharField(max_length=255, verbose_name='Название поста')
    image = models.ImageField(upload_to='articles-photo/%Y/%m/%d',blank=True, null=True, verbose_name='Изображение')
    body = models.TextField(verbose_name='Основной Текст')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,verbose_name='Автор')
    is_active = models.BooleanField(default=False, db_index=True,
                                    verbose_name='Выводить на экран?')

    class Meta:
        ordering = ['date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    author = models.CharField(max_length=30, verbose_name='Автор')
    comment = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Выводить?')
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']

    def __str__(self):
        return self.comment[0:50]


class Fact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название',)
    body = models.CharField(max_length=255, verbose_name='Текст факта')
    is_active = models.BooleanField(default=False, verbose_name='Выкладывать?')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Факт дня'
        verbose_name_plural = "Факты дня"

    def __str__(self):
        return self.name



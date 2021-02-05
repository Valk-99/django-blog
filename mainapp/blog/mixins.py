from django.views.generic.detail import SingleObjectMixin

from .models import *


class CategoryDetailMixin(SingleObjectMixin):

    def get_queryset(self):
        category = self.kwargs.get('category_slug', '')
        q = super().get_queryset()
        return q.filter(category__slug=category).select_related('category')
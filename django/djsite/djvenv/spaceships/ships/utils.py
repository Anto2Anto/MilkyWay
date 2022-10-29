from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        # {'title': 'Sign up', 'url_name': 'sign_up'},
        ]


class DataMixin:
        paginate_by = 4

        def get_user_context(self, **kwargs):
                context = kwargs
                cats = cache.get('cats')  # low-level API
                if not cats:
                        cats = Category.objects.annotate(Count('ships'))
                        cache.set('cats', cats, 120)

                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.pop(1)

                context['menu'] = menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context

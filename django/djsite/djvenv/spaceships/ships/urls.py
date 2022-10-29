from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', ShipsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('sign_in/', SignInUser.as_view(), name='sign_in'),
    path('sign_out/', logout_user, name='sign_out'),
    path('sign_up/', SignUpUser.as_view(), name='sign_up'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShipsCategory.as_view(), name='category'),
]

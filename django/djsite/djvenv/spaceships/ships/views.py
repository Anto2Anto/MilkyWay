from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *


class ShipsHome(DataMixin, ListView):
        model = ships
        template_name = 'ships/index.html'
        context_object_name = 'posts'

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Milky Way')
                return dict(list(context.items()) + list(c_def.items()))

        def get_queryset(self):
                return ships.objects.filter(is_published = True).select_related('cat')


# def index(request):
#        posts = ships.objects.all()
#        context = {
#                'posts': posts,
#                'menu': menu,
#                'title': 'Main page',
#                'cat_selected': 0,
#        }
#        return render(request, 'ships/index.html', context = context)


def about(request):
        return render(request, 'ships/about.html', {'menu': menu, 'title': 'About'})


class Feedback(DataMixin, FormView):
        form_class = Feedback
        template_name = 'ships/feedback.html'
        success_url = reverse_lazy('home')

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Feedback')
                return dict(list(context.items()) + list(c_def.items()))

        def form_valid(self, form):
                print(form.cleaned_data)
                return redirect('home')


# def sign_in(request):
#        return HttpResponse('Sign_in')
#
#
# def sign_up(request):
#        return HttpResponse('Sign_up')


class ShowPost(DataMixin, DetailView):
        model = ships
        template_name = 'ships/post.html'
        slug_url_kwarg = 'post_slug'
        context_object_name = 'post'

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Milky Way: ' + str(context['post']))
                return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#        post = get_object_or_404(ships, slug = post_slug)
#        context = {
#                'post': post,
#                'menu': menu,
#                'title': post.title,
#                'cat_selected': post.cat_id,
#        }
#        return render(request, 'ships/post.html', context = context)


# def show_category(request, cat_slug):
#        cat = Category.objects.filter(slug=cat_slug)
#        posts = ships.objects.filter(cat_id=cat[0].id)

class ShipsCategory(DataMixin, ListView):
        model = ships
        template_name = 'ships/index.html'
        context_object_name = 'posts'
        allow_empty = False

        def get_queryset(self):
                return ships.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published = True).select_related('cat')

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c = Category.objects.get(slug = self.kwargs['cat_slug'])
                c_def = self.get_user_context(title = 'Company: ' + str(c.name),
                                              cat_selected = c.pk)
                return dict(list(context.items()) + list(c_def.items()))

        # if len(posts) == 0:
        #        raise Http404()


#     context = {
#             'posts': posts,
#             'menu': menu,
#             'title': 'View by categories',
#             'cat_selected': cat[0].id,
#     }
#
#     return render(request, 'ships/index.html', context = context)


def categories(request, slug):
        if request.GET:
                print(request.GET)
        return HttpResponse(f"<h1>Articles by categories</h1><p>{slug}</p>")


def archive(request, year):
        if int(year) > 2022:
                return redirect('home', permanent = True)
        return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')


def pageNotFound(request, exception):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class SignUpUser(DataMixin, CreateView):
        form_class = RegisterUserForm
        template_name = 'ships/signup.html'
        success_url = reverse_lazy('sign_in')

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = "Registration")
                return dict(list(context.items()) + list(c_def.items()))

        def form_valid(self, form):
                user = form.save()
                login(self.request, user)
                return redirect('home')


class SignInUser(DataMixin, LoginView):
        form_class = AuthenticationForm
        template_name = 'ships/signin.html'

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Authorization')
                return dict(list(context.items()) + list(c_def.items()))

        def get_success_url(self):
                return reverse_lazy('home')


def logout_user(request):
        logout(request)
        return redirect('sign_in')

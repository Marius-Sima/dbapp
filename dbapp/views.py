from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from dbapp import models
from .models import cerere_de_finantare as cerere
from dbapp import forms
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse

# Create your views here.

class cerere_de_finantare(ListView):
    model = models.cerere_de_finantare
    template_name = 'home.html'
    context_object_name = 'dosare'

class AddDosarForm(CreateView):
    template_name = 'add.html'
    form_class = forms.DosarForm
    model = models.cerere_de_finantare
    sucess_url = "/"

class UserProfileDV(DetailView):
    model = models.UserProfile
    template_name = 'user_profile_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        user_profile = get_object_or_404(models.UserProfile, user__id=user_id)
        return user_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = cerere.objects.filter(user=self.object.user)
        context['user_posts'] = user_posts
        return context
    
    
class CreateUser(View):
    form_class = forms.UserRegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Contul creat pentru {username}')

            return redirect('/')
        return render(request, self.template_name, {'form': form})
    
    
class CustomLoginView(LoginView):
    form_class = forms.Autentificare

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

@login_required
def adauga_dosar(request):
    if request.method == "POST":
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(reverse('profile', args=[request.user.id]))
    else:
        form = models.cerere_de_finantare()
    return render(request, 'add.html', {'form':form})

@login_required
def profile(request, user_id=None):
    if user_id is not None:
        if request.user.id != int(user_id):
            raise Http404('Nu ai permisiune pentru a accesa aceasta pagina')
        user = get_object_or_404(User, pk=user_id)
    else:
        user = request.user
    user_profile = get_object_or_404(models.UserProfile, user=user)
    user_posts = models.cerere_de_finantare.objects.filter(user=request.user)
    return render(request, 'profile.html',{'user_posts': user_posts})
    #return render(request, 'profile.html', {'user_profile': user_profile})

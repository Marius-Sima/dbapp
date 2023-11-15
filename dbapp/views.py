from django.shortcuts import render, redirect
from dbapp import models
from dbapp import forms
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


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
    
class UserPage(ListView):
    model = models.cerere_de_finantare
    template_name = 'user.html'
    context_object_name = 'dosare'


#models and forms
from django import forms
from dbapp import models
#django stuff
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class DosarForm(forms.ModelForm):
    class Meta:
        model = models.cerere_de_finantare
        fields = ["numele_solicitantului", "titlul_proiectului", "descriere", "programe", "locul_derulare"]

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Prenume',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Nume',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class Autentificare(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UserProfileForm(forms.ModelForm): # de revizuit
    class Meta:
        model = models.cerere_de_finantare
        exclude = ['user']
        fields =['numele_solicitantului', 'titlul_proiectului', 'programe', 'descriere','perioada_incepere', 'perioada_incheiere']
        widgets = {
            'perioada_incepere':forms.DateInput(attrs={'type':'date'}),
            'perioada_incheiere':forms.DateInput(attrs={'type':'date'}),
        }
class FileUploadForm(forms.ModelForm):  #posibil sa scot asta odata cu uploaded_file field din UserProfile model
    class Meta:
        model = models.UserProfile
        fields = ['uploaded_file']

class SesiuneForm(forms.ModelForm):
    class Meta:
        model = models.Sesiune
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
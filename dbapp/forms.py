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
        fields = ["numele_solicitantului", "titlul_proiectului", "programe", "locul_derulare"]

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Prenume',
                                                               'class': 'form-control',
                                                               }))
    name = forms.CharField(max_length=100,
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
        fields = ['first_name', 'name', 'username', 'email', 'password1', 'password2']

'''
        def save(self, commit=True):
            user = super(UserRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
        '''
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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.cerere_de_finantare
        exclude = ['user']
        fields =['numele_solicitantului', 'titlul_proiectului', 'programe', 'perioada_incepere', 'perioada_incheiere']
        widgets = {
            'perioada_incepere':forms.DateInput(attrs={'type':'date'}),
            'perioada_incheiere':forms.DateInput(attrs={'type':'date'}),
        }
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['uploaded_file']
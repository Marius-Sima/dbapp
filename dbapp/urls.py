from django.urls import include, path
from dbapp import views
from dbapp import forms
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.cerere_de_finantare.as_view(), name="Dosare"),
    path("add/", views.AddDosarForm.as_view(), name="adauga_dosar"),
    path("register/", views.CreateUser.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=forms.Autentificare), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
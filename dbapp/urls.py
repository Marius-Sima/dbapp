from django.urls import include, path
from dbapp import views
from dbapp import forms
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.cerere_de_finantare.as_view(), name="Dosare"),
    path("add/", views.adauga_dosar, name="adauga_dosar"),
    path("register/", views.CreateUser.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=forms.Autentificare), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('user/<int:pk>/', views.UserProfileDV.as_view(), name='user_profile_detail'),
    path('display_file/<int:user_id>/', views.uploaded_file, name='display_file'),
    path('download_file/<int:user_id>/', views.download_file, name='download_file'),
]
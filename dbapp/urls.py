from django.urls import include, path
from dbapp import views
from dbapp import forms
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static # asta este pt admin ca sa poata descarca fisierele de pe profilele utilizatorilor
from django.conf import settings

urlpatterns = [
    path("", views.welcome.as_view(), name="home"),
    path("add/", views.adauga_dosar, name="adauga_dosar"),
    path("register/", views.CreateUser.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=forms.Autentificare), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('display_file/<int:user_id>/', views.uploaded_file, name='display_file'),
    path('download_file/<int:user_id>/', views.download_file, name='download_file'),
    path('sesiune/', views.SesiuneView.as_view(), name='sesiune'),
    path('user/<int:user_id>/dosar/<int:dosar_id>/', views.dosar_detail, name='dosar_detail'),
    path('responsabil/', views.responsabil_dosar.as_view(), name='responsabil')
]

if settings.DEBUG: # pt admin (NUMAI IN DEVELOPMENT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login,LogoutView
from . views import RegisterView

urlpatterns = [
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(),name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    
]

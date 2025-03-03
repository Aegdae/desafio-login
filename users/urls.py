from django.urls import path
from .views import user_register, user_login, home, user_logout

urlpatterns = [
    path("login", user_login, name='login'),
    path("register/", user_register, name='register'),
    path("home", home, name='home'),
    path("logout", user_logout, name="logout")
]
from authentication import views as authViews
from contact import views as contactViews
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', contactViews.contact, name="contact"),
    path('login/', authViews.authLogin, name="login"),
    path('logout/', authViews.authLogOut, name="logout"),
    path('forgot-password', authViews.forgot, name="forgot-password"),
    path('register', authViews.register, name="register"),
]

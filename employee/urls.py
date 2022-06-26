from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee, name="employee"),
    path('profile/', views.profile, name="employee.profile")
]

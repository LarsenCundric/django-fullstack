from django.urls import path
from second_app_users import views

urlpatterns = [
    path('', views.users),
    path('form/', views.users_form),
]
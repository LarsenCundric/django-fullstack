from django.urls import path
from second_app_users import views

urlpatterns = [
    path('', views.users)
]
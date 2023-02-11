from django.urls import path
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_url_template, name='relative'),
    path('other/', views.other, name='other'),
]
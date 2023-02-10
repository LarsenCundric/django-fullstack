from django.shortcuts import render
from django.http import HttpResponse
from second_app_users.models import DemoUser
# Create your views here.

def users(request):
    users = DemoUser.objects.all()
    users_dict = {'demo_users': users}
    return render(request, 'second_app_users/index.html', context=users_dict)
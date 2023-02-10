from django.shortcuts import render
from django.http import HttpResponse
from second_app_users.models import DemoUser
from second_app_users.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def users(request):
    users = DemoUser.objects.all()
    users_dict = {'demo_users': users}
    return render(request, 'second_app_users/index.html', context=users_dict)

def users_form(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            print('validation success!')
            print(form.cleaned_data)
            form.save(commit=True)
            return index(request)
        else:
            print('not valid!')

    return render(request, 'second_app_users/user_form.html', context={'form':form})
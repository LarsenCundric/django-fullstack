from django.forms import ModelForm
from second_app_users.models import DemoUser

class NewUserForm(ModelForm):
    class Meta:
        model = DemoUser
        fields = '__all__'
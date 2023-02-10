import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from second_app_users.models import DemoUser
from faker import Faker
    
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()
        
        print(fake_fname, fake_lname)
        print(fake_email)

        DemoUser.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Done.')
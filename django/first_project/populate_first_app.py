import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t
    
def populate(N=5):
    for entry in range(N):
        topic = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Done.')
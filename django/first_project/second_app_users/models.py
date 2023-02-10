from django.db import models

# Create your models here.

class DemoUser(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.email})'

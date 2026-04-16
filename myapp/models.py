

# Create your models here.
from django.db import models

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name  
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=10)
    name = models.CharField(max_length=5)
    email = models.EmailField(max_length=70, null=True, unique=True, blank=True)

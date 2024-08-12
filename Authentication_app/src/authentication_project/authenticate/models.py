from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(blank=False, null=False)
    password1 = models.CharField(max_length=128, default='')
    password2 = models.CharField(max_length=128, default='')

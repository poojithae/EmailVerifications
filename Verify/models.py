from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=30, blank=True)
    password2 = models.CharField(max_length=30, blank=True)
   
    def __str__(self):
        return self.email

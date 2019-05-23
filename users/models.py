from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """standart user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'
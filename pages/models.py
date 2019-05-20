from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .coder import coding

class Product(models.Model):
    link = models.CharField(max_length = 240,null = True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(coding(self.id))
    
    def get_absolute_url(self):
        return reverse("rd", kwargs={'rd':coding(self.id)})
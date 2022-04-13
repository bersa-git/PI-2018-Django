from django.db import models


# Create your models here. 
from profiles.models import Profile


class Posts(models.Model):
    title = models.CharField(max_length=8000)
    text = models.CharField(max_length=8000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
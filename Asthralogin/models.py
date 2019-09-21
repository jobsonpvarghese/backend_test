from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name=models.CharField(max_length=100)
    volunteer=models.CharField(max_length=50)
    discription=models.TextField()
    contact=models.IntegerField()

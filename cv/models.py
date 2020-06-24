from django.db import models
from django.utils import timezone
# Create your models here.
class Summary(models.Model):
    text = models.TextField()
    last_edited = models.DateTimeField(default=timezone.now)

class Qualification(models.Model):
    date = models.TextField()
    location = models.TextField()
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

class Experience(models.Model):
    date = models.TextField()
    location = models.TextField()
    duties = models.TextField()
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
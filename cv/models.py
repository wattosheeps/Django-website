from django.db import models
from django.utils import timezone

# Create your models here.
class Summary(models.Model):
    text = models.TextField()
    last_edited = models.DateTimeField(default=timezone.now)

class Qualification(models.Model):
    date_start = models.DateField(default=timezone.now)
    date_end = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100,)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)


class Experience(models.Model):
    date_start = models.DateField(default=timezone.now)
    date_end = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100,)
    duties = models.TextField()
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
class ExperienceDuties(models.Model):
    duty = models.TextField()

class Skill(models.Model):
    heading = models.CharField(max_length=100,)
    info = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
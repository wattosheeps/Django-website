from django.db import models
from django.utils import timezone
# Create your models here.
class Summary(models.Model):
    text = models.TextField()
    last_edited = models.DateTimeField(default=timezone.now)

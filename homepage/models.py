from django.db import models

# Create your models here.
class Task_data(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=300)
    datetime = models.DateTimeField()
    datetime_iso = models.CharField(max_length=16)
    status = models.IntegerField()
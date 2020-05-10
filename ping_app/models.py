from django.db import models


# Create your models here.

class Devices(models.Model):
    Router = models.CharField(max_length=20)
    Output = models.TextField(blank=True)

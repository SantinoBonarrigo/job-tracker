from django.db import models

# Create your models here.
from django.db import models


class JobApplication(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
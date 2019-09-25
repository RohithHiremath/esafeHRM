from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


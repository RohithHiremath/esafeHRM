from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Jobcategory(models.Model):
    jobcategory = models.CharField(max_length=50)

class Jobgrade(models.Model):
    jobgrade = models.CharField(max_length=50)

class Salarycomponent(models.Model):
    componentname = models.CharField(max_length=50)
    types = models.CharField(max_length=50)

class Employmentstatus(models.Model):
    employementstatus = models.CharField(max_length=50)

class Department(models.Model):
    departmentname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


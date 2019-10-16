from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=100)
    # status = models.SmallIntegerField(default=1)

    def __str__(self):
       return self.jobtitle

class Jobcategory(models.Model):
    jobcategory = models.CharField(max_length=50)

    def __str__(self):
       return self.jobcategory

class Jobgrade(models.Model):
    jobgrade = models.CharField(max_length=50)

    def __str__(self):
       return self.jobgrade

class Salarycomponent(models.Model):
    componentname = models.CharField(max_length=50)
    types = models.CharField(max_length=50)

    def __str__(self):
       return self.componentname

class Employmentstatus(models.Model):
    employementstatus = models.CharField(max_length=50)

    def __str__(self):
       return self.employementstatus

class Department(models.Model):
    departmentname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
       return self.departmentname

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
       return self.location

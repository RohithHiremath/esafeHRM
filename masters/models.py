from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, auth, Permission

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

# class Salarycomponent(models.Model):
#     componentname = models.CharField(max_length=50)
#     types = models.CharField(max_length=50)

#     def __str__(self):
#        return self.componentname

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

class Emailtemplate(models.Model):
    title = models.CharField(max_length=50,default='')
    description = RichTextField(blank=True,null=True)

    def __str__(self):
       return self.title

class ShiftDetails(models.Model):
    
    shiftname = models.CharField(max_length=150,blank = False)
    shortname = models.CharField(max_length=150,blank = False)
    shiftdescription = models.CharField(max_length=150,blank = False)
    flexibleshift = models.SmallIntegerField(default=1,blank=False)
    
    def __str__(self):
        return self.shiftname
    
class ShiftTimings(models.Model):
    shift_name = models.ForeignKey(ShiftDetails,on_delete=models.CASCADE)
    workdays = models.SmallIntegerField(default=0,blank=False)
    shift_in_time = models.TimeField()
    shift_out_time = models.TimeField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    weekoff = models.SmallIntegerField(default=2)



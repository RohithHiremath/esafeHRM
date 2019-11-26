from django.db import models
from django.core.validators import RegexValidator
from masters.models import Job, Jobgrade

# Create your models here.
class Leveldefinition(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    levelName = models.CharField(max_length=100,validators=[alphanumeric])
    shortName = models.CharField(max_length=3,validators=[alphanumeric])
    parentlevel = models.IntegerField()

    def __str__(self):
       return self.levelName

class LevelDesignation(models.Model):
    levelid = models.ForeignKey(Leveldefinition,on_delete=models.CASCADE)
    designations = models.ForeignKey(Job,on_delete=models.CASCADE)

class LevelGrades(models.Model):
    levelid = models.ForeignKey(Leveldefinition,on_delete=models.CASCADE)
    grades = models.ForeignKey(Jobgrade,on_delete=models.CASCADE)    
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Leveldefinition(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    levelName = models.CharField(max_length=100,validators=[alphanumeric])
    shortName = models.CharField(max_length=3,validators=[alphanumeric])
    designations = models.CharField(max_length=50,validators=[alphanumeric])
    grades = models.CharField(max_length=50,validators=[alphanumeric])
    parentlevel = models.IntegerField()

    def __str__(self):
       return self.levelName
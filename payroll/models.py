from django.db import models
from django.core.validators import RegexValidator
from organisation.models import Leveldefinition
# Create your models here.

class Salarycomponent(models.Model):
    componentname = models.CharField(max_length=50)
    types = models.CharField(max_length=50)

    def __str__(self):
       return self.componentname

class PayScale(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    payscalename = models.CharField(max_length=50,validators=[alphanumeric])
    description = models.CharField(max_length=100)
    shortname = models.CharField(max_length=3,validators=[alphanumeric])
    experincefrom = models.IntegerField()
    experienceto = models.IntegerField()

    def __str__(self):
       return self.payscalename

class Linktocomponent(models.Model):
    payscale_name = models.ForeignKey(PayScale,on_delete = models.CASCADE)
    component_name = models.ForeignKey(Salarycomponent,on_delete = models.CASCADE)

class AssigningLevelsToPayscale(models.Model):
    payscalenameid = models.ForeignKey(PayScale,on_delete = models.CASCADE)
    levels = models.ForeignKey(Leveldefinition,on_delete = models.CASCADE)

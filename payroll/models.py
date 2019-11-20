from django.db import models

# Create your models here.

class Salarycomponent(models.Model):
    componentname = models.CharField(max_length=50)
    types = models.CharField(max_length=50)

    def __str__(self):
       return self.componentname
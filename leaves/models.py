from django.db import models
from django.core.validators import RegexValidator
from pim.models import Personal_details
# Create your models here.
class Leavestructure(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    leavestructure = models.CharField(max_length=50,validators=[alphanumeric])
    leavedescription = models.CharField(max_length=100)
    
    def __str__(self):
       return str(self.leavestructure)

class Leavetype(models.Model):
    leavetype = models.CharField(max_length=50)
    leavedescription = models.CharField(max_length=100)
    
    def __str__(self):
       return self.leavetype

class Linktoleavetype(models.Model):
    leave_structure = models.ForeignKey(Leavestructure,on_delete = models.CASCADE)
    leave_type = models.ForeignKey(Leavetype,on_delete = models.CASCADE)

class AssignLeaveStructure(models.Model):
    empid = models.ForeignKey(Personal_details,on_delete = models.CASCADE)
    leave_structure = models.ForeignKey(Leavestructure,on_delete = models.CASCADE)
    fromDate = models.DateField(blank = False)
    toDate = models.DateField(blank = False)
    updatedDate = models.DateTimeField(blank = False)
    status = models.BooleanField(default=True)
   
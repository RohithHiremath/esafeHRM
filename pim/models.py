from django.db import models
from masters.models import Job ,Jobgrade, Location ,Employmentstatus, Department
from organisation.models import Leveldefinition
# Create your models here.

class Personal_details(models.Model):

   first_name = models.CharField(max_length=150,blank = False)
   middle_name = models.CharField(max_length=150,blank = True)
   last_name = models.CharField(max_length=150,blank = False)
   date_of_birth = models.DateField(blank = False)
   employee_id = models.CharField(max_length=150,blank = False)
   emailid = models.EmailField(max_length=150)
   mobilenumber = models.CharField(max_length=15,blank = False)
   gender = models.SmallIntegerField(default=1,blank = False)
   marital_status = models.SmallIntegerField(default=1,blank = False)
   nationality = models.SmallIntegerField(default=1,blank = False)
   aadhar_card_no = models.BigIntegerField(blank = False)
   joined_date = models.DateField(blank = False)
   date_of_permanency = models.DateField(blank = False)
   employmentLevel = models.ForeignKey(Leveldefinition,on_delete=models.CASCADE)
   job_title = models.ForeignKey(Job, on_delete=models.CASCADE)
   job_grade = models.ForeignKey(Jobgrade, on_delete=models.CASCADE)
   department = models.ForeignKey(Department,on_delete=models.CASCADE)
   worklocation = models.ForeignKey(Location,on_delete=models.CASCADE)
   employment_status = models.ForeignKey(Employmentstatus,on_delete=models.CASCADE)
   work_shifts = models.IntegerField(default=1)
   isHOD = models.SmallIntegerField(default=0,blank = False)
   
   def __str__(self):
       return self.first_name
from django.db import models
from masters.models import Job ,Jobcategory, Location ,Employmentstatus, Department

# Create your models here.

class Personal_details(models.Model):

   first_name = models.CharField(max_length=150,blank = False)
   middle_name = models.CharField(max_length=150,blank = True)
   last_name = models.CharField(max_length=150,blank = False)
   employee_id = models.CharField(max_length=150,blank = False)
   date_of_birth = models.DateField(blank = False)
   marital_status = models.SmallIntegerField(default=1,blank = False)
   gender = models.SmallIntegerField(default=1,blank = False)
   nationality = models.SmallIntegerField(default=1,blank = False)
   nick_name = models.CharField(max_length=150,blank = True)
   aadhar_card_no = models.BigIntegerField(blank = False)
   joined_date = models.DateField(blank = False)
   date_of_permanency = models.DateField(blank = False) 
   job_title = models.ForeignKey(Job, on_delete=models.CASCADE)
   employment_status = models.ForeignKey(Employmentstatus,on_delete=models.CASCADE)
   job_category = models.ForeignKey(Jobcategory, on_delete=models.CASCADE)
   work_shifts = models.IntegerField(default=1)
   department = models.ForeignKey(Department,on_delete=models.CASCADE)
   worklocation = models.ForeignKey(Location,on_delete=models.CASCADE)

   def __str__(self):
       return self.first_name
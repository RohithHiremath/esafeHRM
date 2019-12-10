from django.db import models
from pim.models import Personal_details
# Create your models here.

class TardinessDetails(models.Model):

    maxallowedlate = models.SmallIntegerField(default=0,blank = False)
    penalty_late = models.SmallIntegerField(default=3,blank = False)
    maxallowedearly = models.SmallIntegerField(default=0,blank = False)
    penalty_early = models.SmallIntegerField(default=3,blank = False)
    holidaycompensatorytype = models.SmallIntegerField(default=2,blank = False)
    holidaypaymentqty = models.SmallIntegerField(default=3,blank = False)
    holidaydaystoexpire = models.SmallIntegerField(default=1,blank = False)
    weekendcompensatorytype = models.SmallIntegerField(default=2,blank = False)
    weekendpaymentqty = models.SmallIntegerField(default=3,blank = False)
    weekenddaystoexpire = models.SmallIntegerField(default=1,blank = False)
    minimumHoursForOT = models.SmallIntegerField(default=2,blank = False)
    OTcompensatorytype = models.SmallIntegerField(default=2,blank = False)
    OTPayment = models.SmallIntegerField(default=3,blank = False)

class EmployeeAttendance(models.Model):

    attendance_date = models.DateField(blank = False)
    employee_code = models.ForeignKey(Personal_details,on_delete = models.CASCADE)
    employee_name = models.CharField(max_length=150,blank=False)
    employee_shift = models.CharField(max_length=150,blank=False)
    employee_intime = models.TimeField(auto_now=False, auto_now_add=False)
    employee_outime = models.TimeField(auto_now=False, auto_now_add=False)
    employee_workduration = models.TimeField(auto_now=False, auto_now_add=False)
    employee_OT = models.TimeField(auto_now=False, auto_now_add=False)
    employee_totalwork = models.TimeField(auto_now=False, auto_now_add=False)
    holiday_status  = models.SmallIntegerField(default=2,blank = False)
    weekend_status  = models.SmallIntegerField(default=2,blank = False)
    attendance_status  = models.SmallIntegerField(default=1,blank = False)
    leave_status  = models.SmallIntegerField(default=1,blank = False)
    compoff_status  = models.SmallIntegerField(default=1,blank = False)
    updated_date_time = models.DateTimeField(blank = False)




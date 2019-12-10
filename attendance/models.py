from django.db import models
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


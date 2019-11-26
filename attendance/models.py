from django.db import models
# Create your models here.

class TardinessDetails(models.Model):

    maxallowedlate = models.SmallIntegerField(default=0,blank = False)
    penalty_late = models.SmallIntegerField(default=3,blank = False)
    maxallowedearly = models.SmallIntegerField(default=0,blank = False)
    penalty_early = models.SmallIntegerField(default=3,blank = False)
    holidaycompensatorytype = models.SmallIntegerField(default=2,blank = False)
    holidaypaymentqty = models.SmallIntegerField(default=3,blank = False)
    weekendcompensatorytype = models.SmallIntegerField(default=2,blank = False)
    weekendpaymentqty = models.SmallIntegerField(default=3,blank = False)

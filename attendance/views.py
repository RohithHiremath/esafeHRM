from django.shortcuts import render
from .models import TardinessDetails
# Create your views here.

def policyDetails(request):
    if request.method == 'POST':
        tardinessvalues = TardinessDetails.objects.all()
        if not tardinessvalues:
            tardinessdetails = TardinessDetails(maxallowedlate=request.POST['maxallowedlate'],
                                penalty_late=request.POST['penalty_late'],
                                maxallowedearly=request.POST['maxallowedearly'],
                                penalty_early=request.POST['penalty_early'],
                                holidaycompensatorytype=request.POST['holidaycompensatorytype'],
                                holidaypaymentqty=request.POST['holidaypaymentqty'],
                                weekendcompensatorytype=request.POST['weekendcompensatorytype'],
                                weekendpaymentqty=request.POST['weekendpaymentqty']
                                )
            tardinessdetails.save()
            tardinessvalues = TardinessDetails.objects.all()
            return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})
        else:
            tardinessdetails = TardinessDetails.objects.get(id=1)
            tardinessdetails.maxallowedlate=request.POST['maxallowedlate']
            tardinessdetails.penalty_late=request.POST['penalty_late']
            tardinessdetails.maxallowedearly=request.POST['maxallowedearly']
            tardinessdetails.penalty_early=request.POST['penalty_early']
            tardinessdetails.holidaycompensatorytype=request.POST['holidaycompensatorytype']
            tardinessdetails.holidaypaymentqty=request.POST['holidaypaymentqty']
            tardinessdetails.weekendcompensatorytype=request.POST['weekendcompensatorytype']
            tardinessdetails.weekendpaymentqty=request.POST['weekendpaymentqty']
            tardinessdetails.minimumHoursForOT=request.POST['minimumHoursForOT']
            tardinessdetails.OTcompensatorytype=request.POST['OTcompensatorytype']
            tardinessdetails.OTPayment=request.POST['OTPayment']
            tardinessdetails.save()
            tardinessvalues = TardinessDetails.objects.all()
            return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})
    else:
        tardinessvalues = TardinessDetails.objects.all()
        return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})


def shiftDetails(request):
    return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})
from django.shortcuts import render,redirect
from .models import TardinessDetails,ShiftDetails,ShiftTimings
from django.http import JsonResponse
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
                                weekendpaymentqty=request.POST['weekendpaymentqty'],
                                holidaydaystoexpire=request.POST['holidaydaystoexpire'],
                                weekenddaystoexpire=request.POST['weekenddaystoexpire'],
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
            tardinessdetails.holidaydaystoexpire=request.POST['holidaydaystoexpire']
            tardinessdetails.weekenddaystoexpire=request.POST['weekenddaystoexpire']
            tardinessdetails.save()
            tardinessvalues = TardinessDetails.objects.all()
            return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})
    else:
        tardinessvalues = TardinessDetails.objects.all()
        return render(request,'policy.html',{'title':'Attendance Policy Details','tardinessvalues':tardinessvalues})

def shiftDetails(request):
    if request.method == "GET":
        return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})
    else:
        response_data = {}
        shiftname = None
        shiftname = ShiftDetails.objects.filter(shiftname = request.POST['shiftname'])
        if not shiftname:
            response_data["is_success"] = True
            shiftdetail = ShiftDetails(shiftname=request.POST['shiftname'],
                                    shortname=request.POST['shortname'],
                                    shiftdescription=request.POST['shiftdescription'],
                                    flexibleshift=request.POST['flexibleshift'])
            shiftdetail.save()
            shiftid = shiftdetail.id
            mondayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['mondayworkingday'],
                                    shift_in_time=request.POST['mondayintime'],
                                    shift_out_time=request.POST['mondayouttime'],
                                    from_time=request.POST['mondaybreaktimefrom'],
                                    to_time=request.POST['mondaybreaktimeto'],
                                    weekoff=request.POST['weekoffmonday'])
            tuesdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['tuesdayworkingday'],
                                    shift_in_time=request.POST['tuesdayintime'],
                                    shift_out_time=request.POST['tuesdayouttime'],
                                    from_time=request.POST['tuesdaybreaktimefrom'],
                                    to_time=request.POST['tuesdaybreaktimeto'],
                                    weekoff=request.POST['weekofftuesday'])   
            wednesdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['wednesdayworkingday'],
                                    shift_in_time=request.POST['wednesdayintime'],
                                    shift_out_time=request.POST['wednesdayouttime'],
                                    from_time=request.POST['wednesdaybreaktimefrom'],
                                    to_time=request.POST['wednesdaybreaktimeto'],
                                    weekoff=request.POST['weekoffwednesday'])  
            thursdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['thursdayworkingday'],
                                    shift_in_time=request.POST['thursdayintime'],
                                    shift_out_time=request.POST['thursdayouttime'],
                                    from_time=request.POST['thursdaybreaktimefrom'],
                                    to_time=request.POST['thursdaybreaktimeto'],
                                    weekoff=request.POST['weekoffthursday'])
            fridayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['fridayworkingday'],
                                    shift_in_time=request.POST['fridayintime'],
                                    shift_out_time=request.POST['fridayouttime'],
                                    from_time=request.POST['fridaybreaktimefrom'],
                                    to_time=request.POST['fridaybreaktimeto'],
                                    weekoff=request.POST['weekofffriday'])
            saturdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['saturdayworkingday'],
                                    shift_in_time=request.POST['saturdayintime'],
                                    shift_out_time=request.POST['saturdayouttime'],
                                    from_time=request.POST['saturdaybreaktimefrom'],
                                    to_time=request.POST['saturdaybreaktimeto'],
                                    weekoff=request.POST['weekoffsaturday'])  
            sundayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                    workdays= request.POST['sundayworkingday'],
                                    shift_in_time=request.POST['sundayintime'],
                                    shift_out_time=request.POST['sundayouttime'],
                                    from_time=request.POST['sundaybreaktimefrom'],
                                    to_time=request.POST['sundaybreaktimeto'],
                                    weekoff=request.POST['weekoffsunday'])       
            mondayshifttiming.save()
            tuesdayshifttiming.save()
            wednesdayshifttiming.save()
            thursdayshifttiming.save()
            fridayshifttiming.save()
            saturdayshifttiming.save()
            sundayshifttiming.save()
            return redirect('/attendance/employeeshiftlist')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    
def validateshiftDetails(request):
    if request.method == "GET":
        return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})
    else: 
        response_data = {}
        shortname = None
        shortname = ShiftDetails.objects.filter(shortname = request.POST['shortname'])
        if not shortname:
            response_data["is_success"] = True
            shiftdetail = ShiftDetails(shiftname=request.POST['shiftname'],
                                    shortname=request.POST['shortname'],
                                    shiftdescription=request.POST['shiftdescription'],
                                    flexibleshift=request.POST['flexibleshift'])
            shiftdetail.save()
            return redirect('/attendance/employeeshiftlist')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def employeeshiftlist(request): 
    shiftdetails = ShiftTimings.objects.all().select_related('shift_name').values('shift_name__shiftname','shift_name__shortname','shift_in_time','shift_out_time').distinct()
    return render(request,'employeeshiftlist.html',{'title':'Employee Shift list','shiftdetails':shiftdetails})



        


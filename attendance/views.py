from django.shortcuts import render
from .models import TardinessDetails
# import xlrd
import openpyxl
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
    return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})

def uploadattendance(request):
    if "GET" == request.method:
        render(request,'processattendance.html',{'title':'Upload Attendance'})
    else:
        new_file = request.FILES["uploadattendance"]
        wb_obj = openpyxl.load_workbook(new_file)
        sheet_obj = wb_obj.active
        max_row = sheet_obj.max_row
        max_col = sheet_obj.max_column
        cell_obj = sheet_obj.cell(row = 12, column = 4) 
        for i in range(12, max_row): 
            Employee_Code = sheet_obj.cell(row = i, column = 4)
            Employee_Name = sheet_obj.cell(row = i, column = 6)
            shift = sheet_obj.cell(row = i, column = 8)
            Intime = sheet_obj.cell(row = i, column = 9)
            outime = sheet_obj.cell(row = i, column = 10)
            workduration = sheet_obj.cell(row = i, column = 13)
            OT = sheet_obj.cell(row = i, column = 14) 
            totalwork = sheet_obj.cell(row = i, column = 16)
            status = sheet_obj.cell(row = i, column = 17)
            print(Employee_Code.value)
            print(Employee_Name.value)
            print(shift.value)
            print(Intime.value)
            print(outime.value)
            print(workduration.value)
            print(OT.value)
            print(totalwork.value)
            print(status.value)

    return render(request,'processattendance.html',{'title':'Upload Attendance'})
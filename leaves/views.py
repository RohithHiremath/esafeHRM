from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import datetime
import openpyxl
import re
from django.urls import reverse
from masters.models import Job
from pim.models import Personal_details
from leaves.models import Holidays,Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure, Upload_list
from django.db import IntegrityError
from leaves.models import Holidays,Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure, LeaveDetails
from django.contrib import messages
import datetime
from datetime import date, timedelta
from django.db.models import Sum

# Create your views here.
def leavestructure(request):
    if request.method == 'POST':
        response_data = {}
        leave = None
        leave = Leavestructure.objects.filter(leavestructure = request.POST['leavestructure'])
        if not leave:
            leave = Leavestructure(leavestructure=request.POST['leavestructure'],
                            shortname=request.POST['shortname'],
                            leavedescription=request.POST['leavedescription'],
                            experincefrom=request.POST['experincefrom'],
                            experienceto=request.POST['experienceto'])
            leave.save()
            return redirect('/leaves/leavestructure/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)        
    else:
        leaves = Leavestructure.objects.all()
        for leavesww in leaves:
            assignedleaves = ''
            linkeddetails = Linktoleavetype.objects.filter(leave_structure=leavesww.id).select_related('leave_type')
            for linkeddetailswww in linkeddetails:
                assignedleaves = assignedleaves+' , '+linkeddetailswww.leave_type.shortname
            assignedleavetypes = assignedleaves.lstrip(' ,')
            leavesww.assignedleavetypes = assignedleavetypes
        return render(request,'leaves/leavestructure.html',{'title':'Leavestructure List','leaves':leaves})

def validateleavestructure(request):
    if request.method == 'POST':
        response_data = {}
        leave = None
        leave = Leavestructure.objects.filter(shortname=request.POST['shortname'])
        if not leave:
            leave = Leavestructure(leavestructure=request.POST['leavestructure'],
                            shortname=request.POST['shortname'],
                            leavedescription=request.POST['leavedescription'],
                            experincefrom=request.POST['experincefrom'],
                            experienceto=request.POST['experienceto'])
            leave.save()
            return redirect('/leaves/leavestructure/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)        
    else:
        leaves = Leavestructure.objects.all()
        for leavesww in leaves:
            assignedleaves = ''
            linkeddetails = Linktoleavetype.objects.filter(leave_structure=leavesww.id).select_related('leave_type')
            for linkeddetailswww in linkeddetails:
                assignedleaves = assignedleaves+' , '+linkeddetailswww.leave_type.shortname
            assignedleavetypes = assignedleaves.lstrip(' ,')
            leavesww.assignedleavetypes = assignedleavetypes
        return render(request,'leaves/leavestructure.html',{'title':'Leavestructure List','leaves':leaves})

def editleavestructure(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Leavestructure.objects.filter(leavestructure = request.POST['leavestructure'])
        if not job:
            leave = Leavestructure.objects.get(id=id)
            leave.leavestructure = request.POST['leavestructure']
            leave.shortname = request.POST['shortname']
            leave.leavedescription = request.POST['leavedescription']
            leave.experincefrom=request.POST['experincefrom']
            leave.experienceto=request.POST['experienceto']
            leave.save()
            return redirect('/leaves/leavestructure/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('/leaves/leavestructure/')

def validateeditleavestructure(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Leavestructure.objects.filter(shortname = request.POST['shortname'])
        if not job:
            leave = Leavestructure.objects.get(id=id)
            leave.leavestructure = request.POST['leavestructure']
            leave.shortname = request.POST['shortname']
            leave.leavedescription = request.POST['leavedescription']
            leave.experincefrom=request.POST['experincefrom']
            leave.experienceto=request.POST['experienceto']
            leave.save()
            return redirect('/leaves/leavestructure/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('/leaves/leavestructure/')

def leavetype(request):
    if request.method == 'POST':
        response_data = {}
        leavetypes =None
        leavetypes =Leavetype.objects.filter(leavetype=request.POST['leavetype'])
        if not leavetypes:
            leave = Leavetype(leavetype=request.POST['leavetype'],
                                shortname=request.POST['shortname'],
                                leavedescription=request.POST['leavedescription'])
            leave.save()
            return redirect('/leaves/leavetype/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        leavetype = Leavetype.objects.all()
        return render(request,'leaves/leavetype.html',{'title':'Leave Type List','leavetype':leavetype})

def validateleavetype(request):
    if request.method == 'POST':
        response_data = {}
        shortnames =None
        shortnames =Leavetype.objects.filter(shortname=request.POST['shortname'])
        if not shortnames:
            leave = Leavetype(leavetype=request.POST['leavetype'],
                                shortname=request.POST['shortname'],
                                leavedescription=request.POST['leavedescription'])
            leave.save()
            return redirect('/leaves/leavetype/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        leavetype = Leavetype.objects.all()
        return render(request,'leaves/leavetype.html',{'title':'Leave Type List','leavetype':leavetype})

def editleavetype(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Leavetype.objects.filter(leavetype = request.POST['leavetype'])
        if not job:
            leave = Leavetype.objects.get(id=id)
            leave.leavetype = request.POST['leavetype']
            leave.shortname = request.POST['shortname']
            leave.leavedescription = request.POST['leavedescription']
            leave.save()
            return redirect('/leaves/leavetype/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('/leaves/leavetype/')

def editvalidateleavetype(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Leavetype.objects.filter(shortname = request.POST['shortname'])
        if not job:
            leave = Leavetype.objects.get(id=id)
            leave.leavetype = request.POST['leavetype']
            leave.shortname = request.POST['shortname']
            leave.leavedescription = request.POST['leavedescription']
            leave.save()
            return redirect('/leaves/leavetype/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('/leaves/leavetype/')
                                                                                                       
def relationwithleave(request, id):
    if request.method =="POST":
        link = Linktoleavetype(leave_structure_id = id,leave_type_id=request.POST['leave_type'],numberOfLeaves=request.POST['numberofleaves'])
        link.save()
        return redirect('/leaves/relationwithleave/'+str(id)+'/')
    else:
        leavestructurename = Leavestructure.objects.get(id=id)
        leavetypes = Leavetype.objects.all()
        linkeddetails = Linktoleavetype.objects.filter(leave_structure=id).select_related('leave_type')
        return render(request,'leaves/linkleaves.html',{'linkeddetails':linkeddetails, 'leavetypes':leavetypes,'leavestructurename':leavestructurename})
                                         
def delete(request, id, idleave):
    job = Linktoleavetype.objects.get(id=id)
    job.delete()
    return redirect('/leaves/relationwithleave/'+str(idleave)+'/')

def assignleavestructure(request):
    if request.method == 'POST':
        selList = request.POST.getlist('empids')
        for val in range(len(selList)):
            dt_obj = datetime.datetime.strptime(request.POST['effectivedate'],"%d-%m-%Y")
            effectivedate = datetime.datetime.strftime(dt_obj, "%Y-%m-%d")
            assignedleavedata = AssignLeaveStructure(
                fromDate = effectivedate,
                toDate = '2099-12-31',
                updatedDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                status = True,
                empid_id = selList[val],
                leave_structure_id = request.POST['leavestructure']
            )
            assignedleavedata.save()
        return redirect('/leaves/assignleavestructure/')
    else:
        personals = Personal_details.objects.all()
        leavestructures = Leavestructure.objects.all()
        return render(request,'leaves/assignleavestructure.html',{'personals':personals,'leavestructures':leavestructures})

def holidays(request):
    if request.method == 'POST':
        response_data = {}
        holyname =None
        holyname =Holidays.objects.filter(holidayname=request.POST['holidayname'])
        if not holyname:
            holy = Holidays(holidayname=request.POST['holidayname'],holidayDate=request.POST['holidayDate'])
            holy.save()
            return redirect('/leaves/holidays/')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:   
        holiday = Holidays.objects.all()
        return render(request,'leaves/holiday.html',{'title':'Holiday List','holiday':holiday})

def upload(request):
    if "GET" == request.method:
        holiday = Holidays.objects.all()
        return render(request, 'leaves/holiday.html', {'holiday':holiday})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        sheet = wb.active
        for c1, c2 in sheet[sheet.dimensions]:
            holidayname = c1.value
            holidaydate = c2.value
            holyname =Holidays.objects.filter(holidayname=holidayname)
            if not holyname:
                holy = Holidays(holidayname=holidayname,holidayDate=holidaydate)
                holy.save()
        return redirect('/leaves/holidays/')
        
def applyleave(request):
    current_user = request.user
    
    if request.method == 'POST':
        dt_obj_from = datetime.datetime.strptime(request.POST['Fromdate'],"%d-%m-%Y")
        fromdate = dt_obj_from.date()
        dt_obj_to = datetime.datetime.strptime(request.POST['Todate'],"%d-%m-%Y")
        todate = dt_obj_to.date()
        delta = todate - fromdate
        for i in range(delta.days+1):
            day = fromdate + timedelta(days=i)
            leavedetails = LeaveDetails(
                            employee_id = request.POST['employee'],
                            Fromdate = day,
                            Todate = day,
                            NumberOfLeaves = 1,
                            AppliedDate = datetime.datetime.now().strftime('%Y-%m-%d'),
                            Status = 1,
                            Reason = request.POST['Reason'],
                            FullorHalfday = request.POST['FullorHalfday'],
                            leave_type_id = request.POST['idleave'],
                          )
            leavedetails.save()
        return redirect('/leaves/applyleave/')
    else:
        personal = Personal_details.objects.get(companyemailid=current_user.email)
        leavestructurdetails = AssignLeaveStructure.objects.filter(empid_id=personal.id).select_related('leave_structure')
        for leavestructurdetails in leavestructurdetails:
            leavestructurrname = leavestructurdetails.leave_structure.leavestructure
            leavestructureid =  leavestructurdetails.leave_structure.id  
            leavestructureshortname =  leavestructurdetails.leave_structure.shortname
        linkedleavetypes = Linktoleavetype.objects.filter(leave_structure_id=leavestructureid).select_related('leave_type')
        for linkedleavetype in linkedleavetypes:
            leaveid = linkedleavetype.leave_type.id
            availed = LeaveDetails.objects.filter(employee_id = personal.id,leave_type_id = leaveid,Status = 2).aggregate(totalleaves = Sum('NumberOfLeaves'))
            requested = LeaveDetails.objects.filter(employee_id = personal.id,leave_type_id = leaveid,Status = 1).aggregate(totalleaves = Sum('NumberOfLeaves'))
            linkedleavetype.leave_type.availed = availed['totalleaves']
            linkedleavetype.leave_type.requested = requested['totalleaves']
            if availed['totalleaves'] is not None:
                availedval = availed['totalleaves']
            else:
                availedval = 0

            if requested['totalleaves'] is not None:
                requestedval = requested['totalleaves']
            else:
                requestedval = 0
            balance = linkedleavetype.numberOfLeaves - (availedval+requestedval)
            print(balance)
            linkedleavetype.leave_type.balance = balance 
        return render(request,'leaves/applyleave.html',{'title':'My Leave Entitlements','personid' : personal.id,'leavestructurrname':leavestructurrname,'leavestructureshortname':leavestructureshortname,'linkedleavetypes':linkedleavetypes})

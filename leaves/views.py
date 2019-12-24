from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import openpyxl
from django.urls import reverse
from masters.models import Job, Emailtemplate
from pim.models import Personal_details
from leaves.models import Holidays,Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure, LeaveDetails, Upload_list
from django.contrib import messages
import datetime
from datetime import date, timedelta
from django.db.models import Sum
from esafehrm.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import string
import re

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
    per = Personal_details.objects.filter()
    if not per:
        return render(request,'leaves/leavemessage.html',{'title':'My Leave Entitlements'})
    else:    
        current_user = request.user
        personal = Personal_details.objects.get(companyemailid=current_user.email)
        leavestructurdetails = AssignLeaveStructure.objects.filter(empid_id=personal.id).select_related('leave_structure')
        for leavestructurdetails in leavestructurdetails:
            leavestructurrname = leavestructurdetails.leave_structure.leavestructure
            leavestructureid =  leavestructurdetails.leave_structure.id  
            leavestructureshortname =  leavestructurdetails.leave_structure.shortname
        linkedleavetypes = Linktoleavetype.objects.filter(leave_structure_id=leavestructureid).select_related('leave_type')
        currentdate = datetime.datetime.now()
        today = date.today()
        for linkedleavetype in linkedleavetypes:
            leaveid = linkedleavetype.leave_type.id
            availed = LeaveDetails.objects.filter(employee_id = personal.id,leave_type_id = leaveid,Status = 2).aggregate(totalleaves = Sum('NumberOfLeaves'))
            requested = LeaveDetails.objects.filter(employee_id = personal.id,leave_type_id = leaveid,Status__in=[1,2,3],Fromdate__gte=today).aggregate(totalleaves = Sum('NumberOfLeaves'))
            cancelled = LeaveDetails.objects.filter(employee_id = personal.id,leave_type_id = leaveid,Status__in=[4,5],Fromdate__gte=today).aggregate(totalleaves = Sum('NumberOfLeaves'))
            linkedleavetype.leave_type.availed = availed['totalleaves']
            linkedleavetype.leave_type.requested = requested['totalleaves']
            linkedleavetype.leave_type.cancelled = cancelled['totalleaves']
            if availed['totalleaves'] is not None:
                availedval = availed['totalleaves']
            else:
                availedval = 0

            if requested['totalleaves'] is not None:
                requestedval = requested['totalleaves']
            else:
                requestedval = 0
            balance = linkedleavetype.numberOfLeaves - (availedval+requestedval)
            linkedleavetype.leave_type.balance = balance 
        return render(request,'leaves/applyleave.html',{'title':'My Leave Entitlements','personid' : personal.id,'leavestructurrname':leavestructurrname,'leavestructureshortname':leavestructureshortname,'linkedleavetypes':linkedleavetypes})
                
def leaverequested(request):
    if request.method == "POST":
        statuslist = request.POST.getlist('status')
        empList = request.POST.getlist('empids')
        for (val,lst) in zip(empList,statuslist):
            leaverequest = LeaveDetails.objects.filter(id = val)
            leaverequest.update(Status = lst)
        for i in leaverequest:
            i.save()

        for (val,lst) in zip(empList,statuslist):
            apptemplate = Emailtemplate.objects.filter(title = 'approve')
            for temp in apptemplate:
                atemplate = temp.description
            clean = re.compile('<.*?>')
            approvetemp = re.sub(clean, '', str(atemplate))
            approvetemplate = approvetemp.replace("&nbsp;", "").replace("Employee",str( LeaveDetails.objects.values_list('employee__first_name',flat=True).get(id = val))).replace("requestdate",str( LeaveDetails.objects.values_list('AppliedDate',flat=True).get(id = val))).replace("leavereason",str( LeaveDetails.objects.values_list('Reason',flat=True).get(id = val))).replace("leaveshortname",str( LeaveDetails.objects.values_list('leave_type__shortname',flat=True).get(id = val))).replace("fromdate",str( LeaveDetails.objects.values_list('Fromdate',flat=True).get(id = val))).replace("todate",str( LeaveDetails.objects.values_list('Todate',flat=True).get(id = val)))

            rejtemplate = Emailtemplate.objects.filter(title = 'reject')
            for temp in rejtemplate:
                rtemplate = temp.description
            clean = re.compile('<.*?>')
            rejecttemp = re.sub(clean, '', str(rtemplate))
            rejecttemplate = rejecttemp.replace("&nbsp;", "").replace("Employee",str( LeaveDetails.objects.values_list('employee__first_name',flat=True).get(id = val))).replace("requestdate",str( LeaveDetails.objects.values_list('AppliedDate',flat=True).get(id = val))).replace("leavereason",str( LeaveDetails.objects.values_list('Reason',flat=True).get(id = val))).replace("leaveshortname",str( LeaveDetails.objects.values_list('leave_type__shortname',flat=True).get(id = val))).replace("fromdate",str( LeaveDetails.objects.values_list('Fromdate',flat=True).get(id = val))).replace("todate",str( LeaveDetails.objects.values_list('Todate',flat=True).get(id = val)))
            
            emailid =  LeaveDetails.objects.values_list('employee__companyemailid',flat=True).get(id = val)
            sendemail(request,emailid,approvetemplate,rejecttemplate,lst)
        return redirect('/leaves/leaverequested/')
    else:    
        leavedetails = LeaveDetails.objects.filter(Status=1).select_related('employee','leave_type')
        return render(request,'leaves/leaverequested.html',{'leavedetails':leavedetails})

def sendemail(request,emailid,approvetemplate,rejecttemplate,statuslist):
    if request.method == 'POST':
        if (statuslist == '2'):
            subject = 'Approval of leave'
            recepient = str(emailid)
            message = approvetemplate
            send_mail(subject,
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        else:
            subject = 'Leave Rejected'
            recepient = str(emailid)
            message = rejecttemplate
            send_mail(subject,
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def getleavedetails(request):
    leaveid = request.POST['leaveid']
    typeflag = request.POST['typeflag']
    empid = request.POST['empid']
    today = date.today()
    if int(typeflag) == 1:
        details = LeaveDetails.objects.filter(employee_id = empid,leave_type_id = leaveid,Status = 2)
    elif int(typeflag) == 2:
        details = LeaveDetails.objects.filter(employee_id = empid,leave_type_id = leaveid,Status = 2)
    elif int(typeflag) == 3:
        details = LeaveDetails.objects.filter(employee_id = empid,leave_type_id = leaveid,Status__in=[1,2,3],Fromdate__gte=today)
    else:
        details = LeaveDetails.objects.filter(employee_id = empid,leave_type_id = leaveid,Status__in=[4,5],Fromdate__gte=today)
    llist=[]
    for detail in details:
        fromdt = datetime.datetime.strftime(detail.Fromdate, '%d-%m-%Y')
        todt = datetime.datetime.strftime(detail.Todate, '%d-%m-%Y')
        appdt = datetime.datetime.strftime(detail.AppliedDate, '%d-%m-%Y')
        l = {}
        l['id']=detail.id
        l['Fromdate']=fromdt
        l['Todate']=todt
        l['AppliedDate']=appdt
        l['FullorHalfday']=detail.FullorHalfday
        l['Reason']=detail.Reason
        l['Status']=detail.Status
        llist.append(l)
    leavedetailsarr = llist
    return JsonResponse(leavedetailsarr, safe=False)

def cancelrequest(request):
    leaveid = request.POST['leaveid']
    leave = {}
    leavesobj = LeaveDetails.objects.get(id=leaveid)
    leavesobj.Status = 4
    leavesobj.save()
    leave['status'] = "Success"
    return JsonResponse(leave, safe=False)

def saveleaverequest(request):
    Fromdate = request.POST['Fromdate']
    Todate = request.POST['Todate']
    FullorHalfday = request.POST['FullorHalfday']
    Reason = request.POST['Reason']
    idleave = request.POST['idleave']
    employee = request.POST['employee']
    if int(FullorHalfday) == 1:
        NumberOfLeaves = 1
    else:
        NumberOfLeaves = 0.5
    dt_obj_from = datetime.datetime.strptime(Fromdate,"%d-%m-%Y")
    fromdate = dt_obj_from.date()
    dt_obj_to = datetime.datetime.strptime(Todate,"%d-%m-%Y")
    todate = dt_obj_to.date()
    delta = todate - fromdate
    for i in range(delta.days+1):
        day = fromdate + timedelta(days=i)
        leavedetails = LeaveDetails(
                        employee_id = employee,
                        Fromdate = day,
                        Todate = day,
                        NumberOfLeaves = NumberOfLeaves,
                        AppliedDate = datetime.datetime.now().strftime('%Y-%m-%d'),
                        Status = 1,
                        Reason = Reason,
                        FullorHalfday = FullorHalfday,
                        leave_type_id = idleave,
                        )
        leavedetails.save()
    leave = {}
    leave['status'] = "Success"
    return JsonResponse(leave, safe=False)



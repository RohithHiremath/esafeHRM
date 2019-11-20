from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from masters.models import Job
from pim.models import Personal_details
from leaves.models import Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure
from django.contrib import messages
import datetime

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
        link = Linktoleavetype(leave_structure_id = id,leave_type_id=request.POST['leave_type'])
        link.save()
        return redirect('/leaves/relationwithleave/'+str(id)+'/')
    else:
        leavestructurename = Leavestructure.objects.get(id=id)
        leavetypes = Leavetype.objects.all()
        linkeddetails = Linktoleavetype.objects.filter(leave_structure=id).select_related('leave_type')
        print(linkeddetails)
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
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from masters.models import Job
from pim.models import Personal_details
from leaves.models import Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure
from django.contrib import messages
import datetime

# Create your views here.
def leavestructure(request):
    if request.method == 'POST':
        leave = Leavestructure(leavestructure=request.POST['leavestructure'],leavedescription=request.POST['leavedescription'])
        leave.save()
        return redirect('/leaves/leavestructure/')
    else:
        leaves = Leavestructure.objects.all()
        return render(request,'leaves/leavestructure.html',{'title':'Leavestructure List','leaves':leaves})

def editleavestructure(request, id):
    if request.method == 'POST':
        leave = Leavestructure.objects.get(id=id)
        leave.leavestructure = request.POST['leavestructure']
        leave.leavedescription = request.POST['leavedescription']
        leave.save()
        return redirect('/leaves/leavestructure/')
    else:
        return redirect('/leaves/leavestructure/')

def leavetype(request):
    if request.method == 'POST':
        leave = Leavetype(leavetype=request.POST['leavetype'],leavedescription=request.POST['leavedescription'])
        leave.save()
        return redirect('/leaves/leavetype/')
    else:
        leavetype = Leavetype.objects.all()
        return render(request,'leaves/leavetype.html',{'title':'Leave Type List','leavetype':leavetype})

def editleavetype(request, id):
    if request.method == 'POST':
        leave = Leavetype.objects.get(id=id)
        leave.leavetype = request.POST['leavetype']
        leave.leavedescription = request.POST['leavedescription']
        leave.save()
        return redirect('/leaves/leavetype/')
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
        linkeddetails = Linktoleavetype.objects.filter(leave_structure=id)
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
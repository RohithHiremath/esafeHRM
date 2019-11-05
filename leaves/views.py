from django.shortcuts import render,redirect
from django.http import HttpResponse
from masters.models import Job
from leaves.models import Leavestructure, Leavetype, Linktoleavetype

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

# def linktoleavetype(request):
    
#     if request.method =="POST":
#         link = Linktoleavetype(leave_structure_id =request.POST['leave_structure'],
#                                leave_type_id=request.POST['leave_type'])
#         link.save()
#         return redirect('/leaves/linkleavetype/')
#     else:
#         links = Linktoleavetype.objects.all()
#         leaves = Leavestructure.objects.all()
#         leavetype = Leavetype.objects.all()
#         return render(request,'leaves/linkleaves.html',{'links':links, 'leaves':leaves,'leavetype':leavetype})
                                                                                                       
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
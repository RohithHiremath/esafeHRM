# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Job

# Create your views here.

def jobtitles(request):
    if request.method == 'POST':
        job = Job(jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
        job.save()
        return redirect('jobtitle')
    else:
        jobs = Job.objects.all()
        return render(request,'jobtitles.html',{'title':'Jobtitles List','jobs':jobs})

def editjobtitles(request, id):
    job = Job.objects.get(id=id)
    context = {'editjob':job}
    print(context)
    return render(request, 'jobtitles.html', context)

def jobcategories(request):
    return render(request,'jobcategories.html',{'title':'Jobtitles List'})

def jobgrades(request):
    return render(request,'jobgrades.html',{'title':'Jobtitles List'})

# <div class="card" style="width: 5rem;margin-bottom: 10px;" id="addbtn">
#         <button type="button" class="btn btn-success" onclick="fnshowaddform()"> Add </button>
#     </div>
#     <div class="card" style="display:none;margin-top: 10px;" id="add">
#         <div class="card-body">
#             <form action="" name="addjob" id="addjob" method="POST">
#                 {% csrf_token %}
#                 <div class="row">
#                     <div class="col-md-4">
#                         <label for="jobtitle">Job Title</label><span>*</span>
#                         <input type="text" class="form-control" id="jobtitle" name="jobtitle" value="" required>
#                     </div>
#                     <div class="col-md-5">
#                         <label for="description">Description</label>
#                         <input type="text" class="form-control" id="jobdescription" value="" name="jobdescription">
#                     </div>
#                     <div class="col-md-3" style="margin-top:30px;">
#                         <button type="submit" class="btn btn-primary"> Save </button>
#                         <button type="button" class="btn btn-primary" onclick="fnshowaddform();"> Cancel </button>
#                     </div>
#                 </div>
#             </form>
#         </div>
#     </div>
#     <div class="card" style="display:none;margin-top: 10px;" id="edit">
#         <div class="card-body">
#             <form action="" name="editjob" id="editjob" method="POST">
#                 {% csrf_token %}
#                 <div class="row">
#                     <div class="col-md-4">
#                         <label for="jobtitle">Job Title</label><span>*</span>
#                         <input type="text" class="form-control" id="jobtitle" name="jobtitle" value="" required>
#                     </div>
#                     <div class="col-md-5">
#                         <label for="description">Description</label>
#                         <input type="text" class="form-control" id="jobdescription" value="" name="jobdescription">
#                     </div>
#                     <div class="col-md-3" style="margin-top:30px;">
#                         <button type="submit" class="btn btn-primary"> Save </button>
#                         <button type="button" class="btn btn-primary" onclick="fnshoweditdform(0);"> Cancel </button>
#                     </div>
#                 </div>
#             </form>
#         </div>
#     </div>
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Job

# Create your views here.

def jobtitles(request):
    if request.method == 'POST':
        job = Job(jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
        job.save()
        return redirect('jobtitle')
    else:
        jobs = Job.objects.all()
        paginator = Paginator(jobs, 2)
        page = request.GET.get('page')
        jobs = paginator.get_page(page)
        return render(request,'jobtitles.html',{'title':'Jobtitles List','jobs':jobs})

def editjobtitles(request, id):
    if request.method == 'POST':
        job = Job.objects.get(id=id)
        job.jobtitle = request.POST['jobtitle']
        job.jobdescription = request.POST['jobdescription']
        job.save()
        return redirect('jobtitle')
    else:
        return redirect('jobtitle')

def jobcategories(request):
    return render(request,'jobcategories.html',{'title':'Jobtitles List'})

def jobgrades(request):
    return render(request,'jobgrades.html',{'title':'Jobtitles List'})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Job, Jobcategory, Jobgrade, Salarycomponent, Employmentstatus, Department, Location

# Create your views here.

def jobtitles(request):
    if request.method == 'POST':
        job = Job(jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
        job.save()
        return redirect('jobtitle')
    else:
        jobs = Job.objects.all().order_by('jobtitle')
        # paginator = Paginator(jobs, 2)
        # page = request.GET.get('page')
        # jobs = paginator.get_page(page)
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
    if request.method == 'POST':
        category = Jobcategory(jobcategory=request.POST['jobcategory'])
        category.save()
        return redirect('jobcategory')
    else:
        categories = Jobcategory.objects.all().order_by('jobcategory')
    return render(request,'jobcategories.html',{'title':'Jobcategories List','categories':categories})

def editjobcategories(request, id):
    if request.method == 'POST':
        cat = Jobcategory.objects.get(id=id)
        cat.jobcategory = request.POST['jobcategory']
        cat.save()
        return redirect('jobcategory')
    else:
        return redirect('jobcategory')

def jobgrade(request):
    if request.method == 'POST':
        grade = Jobgrade(jobgrade=request.POST['jobgrade'])
        grade.save()
        return redirect('jobgrade')
    else:
        grades = Jobgrade.objects.all().order_by('jobgrade')
    return render(request,'jobgrades.html',{'title':'jobgrades List','grades':grades})

def editjobgrade(request, id):
    if request.method == 'POST':
        cat = Jobgrade.objects.get(id=id)
        cat.jobgrade = request.POST['jobgrade']
        cat.save()
        return redirect('jobgrade')
    else:
        return redirect('jobgrade')

def component(request):
    if request.method == 'POST':
        component = Salarycomponent(componentname=request.POST['componentname'],types=request.POST['types'])
        component.save()
        return redirect('component')
    else:
        components = Salarycomponent.objects.all().order_by('componentname','types')
    return render(request,'salarycomponents.html',{'title':'component List','components':components})

def editcomponent(request, id):
    if request.method == 'POST':
        cat = Salarycomponent.objects.get(id=id)
        cat.componentname = request.POST['componentname']
        cat.types = request.POST['types']
        cat.save()
        return redirect('component')
    else:
        return redirect('component')

def employementstatus(request):
    if request.method == 'POST':
        status = Employmentstatus(employementstatus=request.POST['employementstatus'])
        status.save()
        return redirect('status')
    else:
        statuses = Employmentstatus.objects.all().order_by('employementstatus')
    return render(request,'employmentstatus.html',{'title':'status List','statuses':statuses})

def editemployementstatus(request, id):
    if request.method == 'POST':
        cat = Employmentstatus.objects.get(id=id)
        cat.employementstatus = request.POST['employementstatus']
        cat.save()
        return redirect('status')
    else:
        return redirect('status')

def department(request):
    if request.method == 'POST':
        department = Department(departmentname=request.POST['departmentname'],description=request.POST['description'])
        department.save()
        return redirect('department')
    else:
        departments = Department.objects.all().order_by('departmentname')
    return render(request,'department.html',{'title':'status List','departments':departments})

def editdepartment(request, id):
    if request.method == 'POST':
        cat = Department.objects.get(id=id)
        cat.departmentname = request.POST['departmentname']
        cat.description = request.POST['description']
        cat.save()
        return redirect('department')
    else:
        return redirect('department')

def location(request):
    if request.method == 'POST':
        location = Location(location=request.POST['location'])
        location.save()
        return redirect('location')
    else:
        locations = Location.objects.all().order_by('location')
    return render(request,'location.html',{'title':'status List','locations':locations})

def editlocation(request, id):
    if request.method == 'POST':
        loc = Location.objects.get(id=id)
        loc.location = request.POST['location']
        loc.save()
        return redirect('location')
    else:
        return redirect('location')
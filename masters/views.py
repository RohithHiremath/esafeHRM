# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth.models import User, auth, Permission
from .models import Job, Jobcategory, Jobgrade, Salarycomponent, Employmentstatus, Department, Location
# Create your views here.

def jobtitles(request):
    if request.method == 'POST':
        job = Job(jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
        job.save()
        return redirect('jobtitle')
    else:
        jobs = Job.objects.all().order_by('jobtitle')
        return render(request,'jobtitles.html',{'title':'Jobtitles List','jobs':jobs})

def jobtitlesajax(request):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Job.objects.filter(jobtitle = request.POST['jobtitle'])
        if not grade:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editjobtitles(request, id):
    if request.method == 'POST':
        jobs = Job.objects.get(id=id)
        jobs.jobtitle = request.POST['jobtitle']
        jobs.jobdescription = request.POST['jobdescription']
        jobs.save()
        return redirect('jobtitle')
    else:
        return redirect('jobtitle')

def editjobtitlesajax(request, id):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Job.objects.filter(jobtitle = request.POST['jobtitle'])
        deptid = Job.objects.get(id = id)
        if deptid in grade:
            response_data["is_success"] = True
        else:
            if not grade:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def jobcategories(request):
    if request.method == 'POST':
        response_data = {}
        category = None
        category = Jobcategory.objects.filter(jobcategory = request.POST['jobcategory'])
        if not category:
            response_data["is_success"] = True
            category = Jobcategory(jobcategory=request.POST['jobcategory'])
            category.save()
            return redirect('jobcategory')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        categories = Jobcategory.objects.all().order_by('jobcategory')
        return render(request,'jobcategories.html',{'title':'Jobcategories List','categories':categories})

def editjobcategories(request, id):
    if request.method == 'POST':
        response_data = {}
        cat = None
        cat = Jobcategory.objects.filter(jobcategory = request.POST['jobcategory'])
        if cat is not None:
            cats = Jobcategory.objects.get(id=id)
            cats.jobcategory = request.POST['jobcategory']
            cats.save()
            return redirect('jobcategory')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('jobcategory')

def jobgrade(request):
    if request.method == 'POST':
        grade = Jobgrade(jobgrade = request.POST['jobgrade'])
        grade.save()
        return redirect('jobgrade')
    else:
        grades = Jobgrade.objects.all().order_by('jobgrade')
    return render(request,'jobgrades.html',{'title':'jobgrades List','grades':grades})

def jobgradeajax(request):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Jobgrade.objects.filter(jobgrade = request.POST['jobgrade'])
        if not grade:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editjobgrade(request, id):
    if request.method == 'POST':
        cat = Jobgrade.objects.get(id=id)
        cat.jobgrade = request.POST['jobgrade']
        cat.save()
        return redirect('jobgrade')
    else:
        return redirect('jobgrade')

def editjobgradeajax(request, id):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Jobgrade.objects.filter(jobgrade = request.POST['jobgrade'])
        deptid = Jobgrade.objects.get(id = id)
        if deptid in grade:
            response_data["is_success"] = True
        else:
            if not grade:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def component(request):
    if request.method == 'POST':
        response_data = {}
        component = None
        component = Salarycomponent.objects.filter(componentname = request.POST['componentname'])
        if not component:
            response_data["is_success"] = True
            component = Salarycomponent(componentname=request.POST['componentname'],types=request.POST['types'])
            component.save()
            return redirect('component')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        components = Salarycomponent.objects.all().order_by('componentname','types')
    return render(request,'salarycomponents.html',{'title':'component List','components':components})

def editcomponent(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Salarycomponent.objects.filter(componentname = request.POST['componentname'])
        if not job:
            cat = Salarycomponent.objects.get(id=id)
            cat.componentname = request.POST['componentname']
            cat.types = request.POST['types']
            cat.save()
            return redirect('component')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
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

def employementstatusajax(request):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Employmentstatus.objects.filter(employementstatus = request.POST['employementstatus'])
        if not grade:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editemployementstatus(request, id):
    if request.method == 'POST':
        cat = Employmentstatus.objects.get(id=id)
        cat.employementstatus = request.POST['employementstatus']
        cat.save()
        return redirect('status')
    else:
        return redirect('status')

def editemployementstatusajax(request, id):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Employmentstatus.objects.filter(employementstatus = request.POST['employementstatus'])
        deptid = Employmentstatus.objects.get(id = id)
        if deptid in grade:
            response_data["is_success"] = True
        else:
            if not grade:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def department(request):
    if request.method == 'POST':
        department = Department(departmentname=request.POST['departmentname'],description=request.POST['description'])
        department.save()
        return redirect('department')
    else:
        departments = Department.objects.all().order_by('departmentname')
    return render(request,'department.html',{'title':'Department','departments':departments})

def departmentajax(request):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Department.objects.filter(departmentname = request.POST['departmentname'])
        if not grade:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editdepartment(request, id):
    if request.method == 'POST':
        depts = Department.objects.get(id=id)
        depts.departmentname = request.POST['departmentname']
        depts.description = request.POST['description']
        depts.save()
        return redirect('department')
    else:
        return redirect('department')

def editdepartmentajax(request, id):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Department.objects.filter(departmentname = request.POST['departmentname'])
        deptid = Department.objects.get(id = id)
        if deptid in grade:
            response_data["is_success"] = True
        else:
            if not grade:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def worklocation(request):
    if request.method == 'POST':
        loctn = Location(location=request.POST['joblocation'])
        loctn.save()
        return redirect('worklocation')
    else:
        locations = Location.objects.all().order_by('location')
    return render(request,'location.html',{'title':'Location','locations':locations})   

def locationajax(request):
    if request.method == 'POST':
        response_data = {}
        dept = None
        dept = Location.objects.filter(location = request.POST['joblocation'])
        if not dept:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editlocation(request, id):
    if request.method == 'POST':
        loc = Location.objects.get(id=id)
        loc.location = request.POST['joblocation']
        loc.save()
        return redirect('worklocation')
    else:
        return redirect('worklocation')
    
def editlocationajax(request, id):
    if request.method == 'POST':
        response_data = {}
        grade = None
        grade = Location.objects.filter(location = request.POST['joblocation'])
        locid = Location.objects.get(id = id)
        if locid in grade:
            response_data["is_success"] = True
        else:
            if not grade:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import Http404,JsonResponse
from .models import Job, Jobcategory, Jobgrade, Salarycomponent, Employmentstatus, Department, Location
# Create your views here.

def jobtitles(request):
    if request.method == 'POST':
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
            response_data = {}
            job = None
            job = Job.objects.filter(jobtitle = request.POST['jobtitle'])
            if not job:
                response_data["is_success"] = True
                job = Job(jobtitle=request.POST['jobtitle'],jobdescription=request.POST['jobdescription'])
                job.save()
                return redirect('jobtitle')
            else:
                response_data["is_success"] = False
            return JsonResponse(response_data)
    else:
        jobs = Job.objects.all().order_by('jobtitle')
        return render(request,'jobtitles.html',{'title':'Jobtitles List','jobs':jobs})

def editjobtitles(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Job.objects.filter(jobtitle = request.POST['jobtitle'])
        if not job:
            jobs = Job.objects.get(id=id)
            jobs.jobtitle = request.POST['jobtitle']
            jobs.jobdescription = request.POST['jobdescription']
            jobs.save()
            return redirect('jobtitle')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('jobtitle')

def jobcategories(request):
    if request.method == 'POST':
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
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
        cat = jobcategory.objects.filter(jobcategory = request.POST['jobcategory'])
        if not cat:
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
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
            response_data = {}
            grade = None
            grade = Jobgrade.objects.filter(jobgrade = request.POST['jobgrade'])
            if not grade:
                # response_data["is_success"] = True
                grade = Jobgrade(jobgrade=request.POST['jobgrade'])
                grade.save()
                return redirect('jobgrade')
            else:
                response_data["is_success"] = False
                return JsonResponse(response_data)
    else:
        grades = Jobgrade.objects.all().order_by('jobgrade')
    return render(request,'jobgrades.html',{'title':'jobgrades List','grades':grades})

def editjobgrade(request, id):
    if request.method == 'POST':
        response_data = {}
        cat = None
        cat = Jobgrade.objects.filter(jobgrade = id)
        if not cat:
            cat = Jobgrade.objects.get(id=id)
            cat.jobgrade = request.POST['jobgrade']
            cat.save()
            return redirect('jobgrade')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('jobgrade')

def component(request):
    if request.method == 'POST':
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
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
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
            response_data = {}
            status = None
            status = Employmentstatus.objects.filter(employementstatus = request.POST['employementstatus'])
            if not status:
                response_data["is_success"] = True
                status = Employmentstatus(employementstatus=request.POST['employementstatus'])
                status.save()
                return redirect('status')
            else:
                response_data["is_success"] = False
            return JsonResponse(response_data)
    else:
        statuses = Employmentstatus.objects.all().order_by('employementstatus')
    return render(request,'employmentstatus.html',{'title':'status List','statuses':statuses})

def editemployementstatus(request, id):
    if request.method == 'POST':
        response_data = {}
        job = None
        job = Salarycomponent.objects.filter(employementstatus = request.POST['employementstatus'])
        if not job:
            cat = Employmentstatus.objects.get(id=id)
            cat.employementstatus = request.POST['employementstatus']
            cat.save()
            return redirect('status')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('status')

def department(request):
    if request.method == 'POST':
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
            response_data = {}
            department = None
            department = Department.objects.filter(departmentname = request.POST['departmentname'])
            if not department:
                response_data["is_success"] = True
                department = Department(departmentname=request.POST['departmentname'],description=request.POST['description'])
                department.save()
                return redirect('department')
            else:
                response_data["is_success"] = False
            return JsonResponse(response_data)
    else:
        departments = Department.objects.all().order_by('departmentname')
    return render(request,'department.html',{'title':'Department','departments':departments})

def editdepartment(request, id):
    if request.method == 'POST':
        response_data = {}
        dept = None
        dept = Department.objects.filter(departmentname = request.POST['departmentname'])
        if not dept:
            # response_data["is_success"] = True
            depts = Department.objects.get(id=id)
            depts.departmentname = request.POST['departmentname']
            depts.description = request.POST['description']
            depts.save()
            return redirect('department')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('department')

def location(request):
    if request.method == 'POST':
        if request.method == "GET":
            raise Http404("URL doesn't exists")
        else:
            response_data = {}
            loc = None
            loc = Location.objects.filter(location = request.POST['locationname'])
            if not loc:
                response_data["is_success"] = True
                location = Location(location = request.POST['locationname'])
                location.save()
                return redirect('location')
            else:
                response_data["is_success"] = False
            return JsonResponse(response_data)
    else:
        locations = Location.objects.all()
    return render(request,'location.html',{'title':'Location','locations':locations})

def editlocation(request, id):
    if request.method == 'POST':
        response_data = {}
        dept = None
        dept = Location.objects.filter(location = request.POST['locationname'])
        if not dept:
            # response_data["is_success"] = True
            loc = Location.objects.get(id=id)
            loc.location = request.POST['locationname']
            loc.save()
            return redirect('location')
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)
    else:
        return redirect('location')
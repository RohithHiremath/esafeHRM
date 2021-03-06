# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth.models import User, auth, Permission
from .models import Job, Jobcategory, Jobgrade, Employmentstatus, Department, Location, ShiftDetails, ShiftTimings
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

def shiftDetails(request):
    if request.method == "GET":
        return render(request,'shiftdetails.html',{'title':'Employee ShiftDetails'})
    else:
        shiftdetail = ShiftDetails(shiftname=request.POST['shiftname'],
                                shortname=request.POST['shortname'],
                                shiftdescription=request.POST['shiftdescription'],
                                flexibleshift=request.POST['flexibleshift'])
        shiftdetail.save()
        shiftid = shiftdetail.id
        mondayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['mondayworkingday'],
                                shift_in_time=request.POST['mondayintime'],
                                shift_out_time=request.POST['mondayouttime'],
                                from_time=request.POST['mondaybreaktimefrom'],
                                to_time=request.POST['mondaybreaktimeto'],
                                weekoff=request.POST['weekoffmonday'])
        tuesdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['tuesdayworkingday'],
                                shift_in_time=request.POST['tuesdayintime'],
                                shift_out_time=request.POST['tuesdayouttime'],
                                from_time=request.POST['tuesdaybreaktimefrom'],
                                to_time=request.POST['tuesdaybreaktimeto'],
                                weekoff=request.POST['weekofftuesday'])   
        wednesdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['wednesdayworkingday'],
                                shift_in_time=request.POST['wednesdayintime'],
                                shift_out_time=request.POST['wednesdayouttime'],
                                from_time=request.POST['wednesdaybreaktimefrom'],
                                to_time=request.POST['wednesdaybreaktimeto'],
                                weekoff=request.POST['weekoffwednesday'])  
        thursdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['thursdayworkingday'],
                                shift_in_time=request.POST['thursdayintime'],
                                shift_out_time=request.POST['thursdayouttime'],
                                from_time=request.POST['thursdaybreaktimefrom'],
                                to_time=request.POST['thursdaybreaktimeto'],
                                weekoff=request.POST['weekoffthursday'])
        fridayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['fridayworkingday'],
                                shift_in_time=request.POST['fridayintime'],
                                shift_out_time=request.POST['fridayouttime'],
                                from_time=request.POST['fridaybreaktimefrom'],
                                to_time=request.POST['fridaybreaktimeto'],
                                weekoff=request.POST['weekofffriday'])
        saturdayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['saturdayworkingday'],
                                shift_in_time=request.POST['saturdayintime'],
                                shift_out_time=request.POST['saturdayouttime'],
                                from_time=request.POST['saturdaybreaktimefrom'],
                                to_time=request.POST['saturdaybreaktimeto'],
                                weekoff=request.POST['weekoffsaturday'])  
        sundayshifttiming = ShiftTimings(shift_name_id=shiftid,
                                workdays= request.POST['sundayworkingday'],
                                shift_in_time=request.POST['sundayintime'],
                                shift_out_time=request.POST['sundayouttime'],
                                from_time=request.POST['sundaybreaktimefrom'],
                                to_time=request.POST['sundaybreaktimeto'],
                                weekoff=request.POST['weekoffsunday'])       
        mondayshifttiming.save()
        tuesdayshifttiming.save()
        wednesdayshifttiming.save()
        thursdayshifttiming.save()
        fridayshifttiming.save()
        saturdayshifttiming.save()
        sundayshifttiming.save()
        return redirect('employeeshiftlist')
    
def shiftdetailsajax(request):
    if request.method == 'POST':
        response_data = {}
        dept = None
        dept = ShiftDetails.objects.filter(shiftname = request.POST['shiftname'])
        if not dept:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def shortnameajax(request):
    if request.method == 'POST':
        response_data = {}
        dept = None
        dept = ShiftDetails.objects.filter(shortname = request.POST['shortname'])
        if not dept:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def employeeshiftlist(request): 
    shiftdetails = ShiftTimings.objects.all().select_related('shift_name').values('shift_name__shiftname','shift_name__shortname','shift_in_time','shift_out_time').distinct()
    return render(request,'employeeshiftlist.html',{'title':'Employee Shift list','shiftdetails':shiftdetails})

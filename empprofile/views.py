from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.hashers import check_password
from pim.models import Personal_details
from masters.models import Job, Jobgrade ,Employmentstatus, Location, Department, Emailtemplate
from organisation.models import Leveldefinition, LevelDesignation,LevelGrades
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.

def changepassword(request):
    currentpassword= request.user.password
    currentid= request.user.id
    if request.method == 'POST':
        oldpassword= request.POST['oldpassword']
        newpassword= request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        matchcheck= check_password(oldpassword, currentpassword)
        if matchcheck:
            user = User.objects.get(id=currentid)
            user.set_password(newpassword)
            user.save()
        else:
            pass

    return render(request,'changepassword.html',{'title':'Change Password'})

def checkoldpassword(request):
    currentpassword= request.user.password
    oldpassword = request.POST['oldpassword']
    passwordstatus = {}
    matchcheck= check_password(oldpassword, currentpassword)
    if matchcheck:
        passwordstatus['status'] = 1
    else:
        passwordstatus['status'] = 2
    return JsonResponse(passwordstatus, safe=False)
    
def profiledetails(request):
    currentid= request.user.id
    personal = Personal_details.objects.get(id=currentid)
    personal.date_of_birth = datetime.strftime(personal.date_of_birth, "%Y-%m-%d")
    personal.joined_date = datetime.strftime(personal.joined_date, "%Y-%m-%d")
    personal.date_of_permanency = datetime.strftime(personal.date_of_permanency, "%Y-%m-%d")
    jobtitles = LevelDesignation.objects.filter(levelid_id=personal.employmentLevel_id).select_related('designations')
    jobgrades = LevelGrades.objects.filter(levelid_id=personal.employmentLevel_id).select_related('grades')
    employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
    locations = Location.objects.all().order_by('location')
    departments = Department.objects.all().order_by('departmentname')
    reportingmanagers = Personal_details.objects.filter(department_id=personal.reportingdepartment, job_grade_id__gte = personal.job_grade_id)
    levels = Leveldefinition.objects.all().order_by('levelName')
    return render(request,'myprofile.html',{'title':'My Profile','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobgrades':jobgrades,
                                                'employmentstatus':employmentstatus,
                                                'locations':locations,
                                                'departments':departments,
                                                'levels':levels,
                                                "reportingmanagers":reportingmanagers}) 



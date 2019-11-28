from django.shortcuts import render,redirect
from .models import Personal_details
from datetime import datetime
from masters.models import Job, Jobgrade ,Employmentstatus, Location, Department, Emailtemplate
from organisation.models import Leveldefinition
from django.shortcuts import render
from esafehrm.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import string
import re
from random import *
from organisation.models import Leveldefinition, LevelDesignation,LevelGrades
from django.http import HttpResponse,Http404,JsonResponse
import json

def Personal_details_view(request):
    if request.method =="POST":
        duhead = request.POST.get('duhead', False)
        if not duhead:
            duhead=0
        else:
            duhead=request.POST['duhead']
        
        emp_id = fngetempid(request)
        personal = Personal_details(first_name=request.POST['first_name'],
                                middle_name=request.POST['middle_name'],
                                last_name =request.POST['last_name'],
                                employee_id = emp_id,
                                date_of_birth=request.POST['date_of_birth'],
                                personalemailid = request.POST['personalemailid'],
                                mobilenumber=request.POST['mobilenumber'],
                                gender=request.POST['gender'],
                                marital_status=request.POST['marital_status'],
                                nationality=request.POST['nationality'],                                                             
                                aadhar_card_no=request.POST['aadhar_card_no'],
                                joined_date=request.POST['joined_date'],
                                date_of_permanency=request.POST['date_of_permanency'],
                                employmentLevel_id = request.POST['empllevel'],
                                job_title_id =request.POST['job_title'],
                                job_grade_id=request.POST['Jobgrade'],
                                employment_status_id=request.POST['employment_status'],
                                work_shifts=request.POST['work_shifts'],
                                worklocation_id=request.POST['worklocation'],
                                department_id=request.POST['department'],
                                DUHead=duhead,
                                companyemailid = request.POST['companyemailid'],
                                reportingto = request.POST['reportingname'],
                                reportingtoId = request.POST['reportingmanager'],
                                reportingdepartment = request.POST['reportingdepartment'])
        emailid = request.POST['companyemailid']
        personal.save()
        characters = string.ascii_letters + string.digits 
        password = "".join(choice(characters) for x in range(randint(5,6)))
        emailtemplate = Emailtemplate.objects.filter(title = 'welcome')
        for temp in emailtemplate:
            template = temp.description
        clean = re.compile('<.*?>')
        emailtemplate = re.sub(clean, '', str(template))
        mailtemplate = emailtemplate.replace("Name",(request.POST['first_name']+" "+request.POST['middle_name'] +" "+request.POST['last_name'])).replace("user",request.POST['companyemailid']).replace("pword",password).replace("&nbsp;", "")
        sendemail(request,emailid,mailtemplate)
        return redirect('/pim/employeelist/')
    else:
        levels = Leveldefinition.objects.all().order_by('levelName')
        personals = Personal_details.objects.all()
        jobtitles = Job.objects.all().order_by('jobtitle')
        jobgrades = Jobgrade.objects.all().order_by('jobgrade')
        employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
        locations = Location.objects.all().order_by('location')
        departments = Department.objects.all().order_by('departmentname')
        return render(request,'pim/personaldetails.html',{'personals':personals,
                                                    'jobtitles':jobtitles,
                                                    'jobgrades':jobgrades,
                                                    'employmentstatus':employmentstatus,
                                                    'locations':locations,
                                                    'departments':departments,
                                                    'levels': levels})

def sendemail(request,emailid,mailtemplate):
    if request.method == 'POST':
        subject = 'Login Details'
        recepient = str(emailid)
        message = mailtemplate
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def fnGetReportingId(idval):
    personals = Personal_details.objects.filter(department_id=idval, isHOD=1).values()
    return personals

def employeelist(request):
    personals = Personal_details.objects.all()
    return render(request,'pim/employeelist.html',{'personals':personals})

def edit(request, id):
    personal = Personal_details.objects.get(id=id)
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
    return render(request,'pim/editdetails.html',{'title':'Edit Employee List','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobgrades':jobgrades,
                                                'employmentstatus':employmentstatus,
                                                'locations':locations,
                                                'departments':departments,
                                                'levels':levels,
                                                "reportingmanagers":reportingmanagers})                                              

def update(request, id):
    duhead = request.POST.get('duhead', False)
    reportingid = request.POST.get('department_id', False)
    if not duhead:
        duhead=0
    else:
        duhead=request.POST['duhead']
    personal = Personal_details.objects.get(id=id)
    personal.employee_id = request.POST['employee_id']
    personal.first_name = request.POST['first_name']
    personal.middle_name = request.POST['middle_name']
    personal.last_name = request.POST['last_name']
    personal.date_of_birth = request.POST['date_of_birth']
    personal.personalemailid = request.POST['personalemailid']
    personal.mobilenumber = request.POST['mobilenumber']
    personal.gender = request.POST['gender']
    personal.marital_status = request.POST['marital_status']
    personal.nationality = request.POST['nationality']
    personal.aadhar_card_no = request.POST['aadhar_card_no']
    personal.joined_date = request.POST['joined_date']
    personal.date_of_permanency = request.POST['date_of_permanency']
    personal.employmentLevel_id = request.POST['empllevel']
    personal.job_title_id= request.POST['job_title_id']
    personal.job_grade_id = request.POST['job_grade_id']
    personal.department_id = request.POST['department_id']
    personal.companyemailid = request.POST['companyemailid']
    personal.employment_status_id = request.POST['employment_status_id']
    personal.worklocation_id = request.POST['worklocation_id']
    personal.work_shifts = request.POST['work_shifts']
    personal.duhead = duhead
    personal.reportingtoId = request.POST['reportingmanager']
    personal.reportingto = request.POST['reportingname']
    personal.reportingdepartment = request.POST['reportingdepartment']
    personal.save()
    return redirect('/pim/employeelist/')

def fngetempid(request):
    try:
        personal = Personal_details.objects.latest('employee_id')
        if personal.employee_id == None:
            latestempid = 1
            latestempid = str(latestempid).zfill(5)
            return latestempid
        else:
            latestempid = int(personal.employee_id) + 1
            latestempid = str(latestempid).zfill(5)
            return latestempid
    except:
        latestempid = 1
        latestempid = str(latestempid).zfill(5)
        return latestempid

def getdropdownvalues(request):
    levelid = None
    levelid = request.POST['levelid']
    reqflag = request.POST['reqflag']
    if int(reqflag) == 1:   
        designations = LevelDesignation.objects.filter(levelid_id=levelid).select_related('designations')
        dlist=[]
        for designation in designations:
            d={}
            d['id']=designation.designations.id
            d['value']=designation.designations.jobtitle
            dlist.append(d)
        jobgradelist = dlist
    else:
        grades = LevelGrades.objects.filter(levelid_id=levelid).select_related('grades')
        glist=[]
        for grade in grades:
            g={}
            g['id']=grade.grades.id
            g['value']=grade.grades.jobgrade
            glist.append(g)
        jobgradelist = glist
    return JsonResponse(jobgradelist, safe=False)

def getmanagers(request):
    deptid = None
    deptid = request.POST['deptid']
    idgrade = request.POST['idgrade']
    print(idgrade)
    reportingmanagers = Personal_details.objects.filter(department_id=deptid, job_grade_id__gte = idgrade)
    rlist=[]
    for reportingmanager in reportingmanagers:
        r={}
        r['id']=reportingmanager.id
        r['value']=reportingmanager.first_name+' '+reportingmanager.middle_name+' '+reportingmanager.last_name
        rlist.append(r)
    reportingmanagers = rlist
    return JsonResponse(reportingmanagers, safe=False)


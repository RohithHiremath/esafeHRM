from django.shortcuts import render,redirect
from .models import Personal_details
from datetime import datetime
from masters.models import Job, Jobcategory ,Employmentstatus, Location, Department
# Create your views here.

def Personal_details_view(request):
    emp_id = fngetempid(request)
    if request.method =="POST":
        emp_id = fngetempid(request)
        personal = Personal_details(first_name=request.POST['first_name'],
                                middle_name=request.POST['middle_name'],
                                last_name =request.POST['last_name'],
                                employee_id = emp_id,
                                date_of_birth=request.POST['date_of_birth'],
                                marital_status=request.POST['marital_status'],
                                gender=request.POST['gender'],
                                nationality=request.POST['nationality'],
                                nick_name=request.POST['nick_name'],
                                aadhar_card_no=request.POST['aadhar_card_no'],
                                joined_date=request.POST['joined_date'],
                                date_of_permanency=request.POST['date_of_permanency'],
                                job_title =request.POST['job_title'],
                                employment_status=request.POST['employment_status'],
                                job_category=request.POST['job_category'],
                                work_shifts=request.POST['work_shifts'],
                                department=request.POST['department'],
                                worklocation=request.POST['worklocation'])
        personal.save()                        
        return redirect('/pim/employeelist/')
    else:
        personals = Personal_details.objects.all()
        jobtitles = Job.objects.all().order_by('jobtitle')
        jobcategory = Jobcategory.objects.all().order_by('jobcategory')
        employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
        locations = Location.objects.all().order_by('location')
        departments = Department.objects.all().order_by('departmentname')
        return render(request,'pim/personaldetails.html',{'personals':personals,
                                                    'jobtitles':jobtitles,
                                                    'jobcategory':jobcategory,
                                                    'employmentstatus':employmentstatus,
                                                    'locations':locations,
                                                    'departments':departments})

def employeelist(request):
    personals = Personal_details.objects.all()
    return render(request,'pim/employeelist.html',{'personals':personals})

def edit(request, id):
    personal = Personal_details.objects.get(id=id)
    personal.date_of_birth = datetime.strftime(personal.date_of_birth, "%Y-%m-%d")
    personal.joined_date = datetime.strftime(personal.joined_date, "%Y-%m-%d")
    personal.date_of_permanency = datetime.strftime(personal.date_of_permanency, "%Y-%m-%d")
    jobtitles = Job.objects.all().order_by('jobtitle')
    jobcategory = Jobcategory.objects.all().order_by('jobcategory')
    employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
    locations = Location.objects.all().order_by('location')
    departments = Department.objects.all().order_by('departmentname')
    return render(request,'pim/editdetails.html',{'title':'Edit Employee List','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobcategory':jobcategory,
                                                'employmentstatus':employmentstatus,
                                                'locations':locations,
                                                'departments':departments})                                              

def update(request, id):
    personal = Personal_details.objects.get(id=id)
    personal.employee_id = request.POST['employee_id']
    personal.first_name = request.POST['first_name']
    personal.middle_name = request.POST['middle_name']
    personal.last_name = request.POST['last_name']
    personal.job_title = request.POST['job_title']
    personal.nationality = request.POST['nationality']
    personal.worklocation = request.POST['worklocation']
    personal.date_of_birth = request.POST['date_of_birth']
    personal.joined_date = request.POST['joined_date']
    personal.date_of_permanency = request.POST['date_of_permanency']
    personal.marital_status = request.POST['marital_status']
    personal.gender = request.POST['gender']
    personal.nick_name = request.POST['nick_name']
    personal.work_shifts = request.POST['work_shifts']
    personal.aadhar_card_no = request.POST['aadhar_card_no']
    personal.employment_status = request.POST['employment_status']
    personal.job_category = request.POST['job_category']
    personal.department = request.POST['department']
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


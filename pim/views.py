from django.shortcuts import render,redirect
from .models import Personal_details
from datetime import datetime
from masters.models import Job, Jobgrade ,Employmentstatus, Location, Department
from organisation.models import Leveldefinition
# Create your views here.

def Personal_details_view(request):
    if request.method =="POST":
        ishod = request.POST.get('ishod', False)
        if not ishod:
            ishod=0
        else:
            ishod=request.POST['ishod']
        emp_id = fngetempid(request)
        personal = Personal_details(first_name=request.POST['first_name'],
                                middle_name=request.POST['middle_name'],
                                last_name =request.POST['last_name'],
                                employee_id = emp_id,
                                date_of_birth=request.POST['date_of_birth'],
                                emailid = request.POST['emailid'],
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
                                isHOD = ishod
                                )
        personal.save()
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
   
def employeelist(request):
    personals = Personal_details.objects.all()
    return render(request,'pim/employeelist.html',{'personals':personals})

def edit(request, id):
    personal = Personal_details.objects.get(id=id)
    personal.date_of_birth = datetime.strftime(personal.date_of_birth, "%Y-%m-%d")
    personal.joined_date = datetime.strftime(personal.joined_date, "%Y-%m-%d")
    personal.date_of_permanency = datetime.strftime(personal.date_of_permanency, "%Y-%m-%d")
    jobtitles = Job.objects.all().order_by('jobtitle')
    jobgrades = Jobgrade.objects.all().order_by('jobgrade')
    employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
    locations = Location.objects.all().order_by('location')
    departments = Department.objects.all().order_by('departmentname')
    levels = Leveldefinition.objects.all().order_by('levelName')
    return render(request,'pim/editdetails.html',{'title':'Edit Employee List','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobgrades':jobgrades,
                                                'employmentstatus':employmentstatus,
                                                'locations':locations,
                                                'departments':departments,
                                                'levels':levels})                                              

def update(request, id):
    ishod = request.POST.get('ishod', False)
    if not ishod:
        ishod=0
    else:
        ishod=request.POST['ishod']
   
    personal = Personal_details.objects.get(id=id)
    personal.employee_id = request.POST['employee_id']
    personal.first_name = request.POST['first_name']
    personal.middle_name = request.POST['middle_name']
    personal.last_name = request.POST['last_name']
    personal.date_of_birth = request.POST['date_of_birth']
    personal.emailid = request.POST['emailid']
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
    personal.employment_status_id = request.POST['employment_status_id']
    personal.worklocation_id = request.POST['worklocation_id']
    personal.work_shifts = request.POST['work_shifts']
    personal.isHOD = ishod
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
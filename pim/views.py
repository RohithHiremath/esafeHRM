from django.shortcuts import render,redirect
from .models import Personal_details
from masters.models import Job, Jobcategory ,Employmentstatus
# Create your views here.

def Personal_details_view(request):
    if request.method =="POST":
        personal = Personal_details(first_name=request.POST['first_name'],
                                middle_name=request.POST['middle_name'],
                                last_name =request.POST['last_name'],
                                employee_id=request.POST['employee_id'],
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
                                work_shifts=request.POST['work_shifts'])
        personal.save()
        return redirect('/pim/employeelist/')
    else:
        personals = Personal_details.objects.all()
        jobtitles = Job.objects.all()
        jobcategory = Jobcategory.objects.all()
        employmentstatus = Employmentstatus.objects.all()
        return render(request,'pim/personaldetails.html',{'personals':personals,
                                                    'jobtitles':jobtitles,
                                                    'jobcategory':jobcategory,
                                                    'employmentstatus':employmentstatus})

def employeelist(request):
    personals = Personal_details.objects.all()
    return render(request,'pim/employeelist.html',{'personals':personals})

def edit(request, id):
    personal = Personal_details.objects.get(id=id)
    jobtitles = Job.objects.all()
    jobcategory = Jobcategory.objects.all()
    employmentstatus = Employmentstatus.objects.all()
    return render(request,'pim/editdetails.html',{'title':'Edit Employee List','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobcategory':jobcategory,
                                                'employmentstatus':employmentstatus})                                              

def update(request, id):
    personal = Personal_details.objects.get(id=id)
    personal.employee_id = request.POST['employee_id']
    personal.first_name = request.POST['first_name']
    personal.job_title = request.POST['job_title']
    personal.employment_status = request.POST['employment_status']
    personal.nationality = request.POST['nationality']
    personal.save()
    return redirect('/pim/employeelist/')

from django.shortcuts import render,redirect
from .models import Personal_details
from masters.models import Job, Jobgrade ,Employmentstatus, Location, Department, Emailtemplate, ShiftDetails
from organisation.models import Leveldefinition
from esafehrm.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import string
import re
import random
from organisation.models import Leveldefinition, LevelDesignation,LevelGrades
from django.http import HttpResponse,Http404,JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from datetime import timedelta
from datetime import datetime, date
from dateutil import relativedelta
from leaves.models import AssignLeaveStructure,AssigningLevelsToStructure, Leavestructure
from payroll.models import AssignPayscale, AssigningLevelsToPayscale, PayScale

def Personal_details_view(request):
    if request.method =="POST":
        response_data = {}
        compmail = None
        duhead = request.POST.get('duhead', False)
        if not duhead:
            duhead=0
        else:
            duhead=request.POST['duhead']
        emp_id = fngetempid(request)
        compmail = Personal_details.objects.filter(companyemailid = request.POST['companyemailid'])
        if not compmail:
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
                                    work_shifts_id=request.POST['work_shifts'],
                                    worklocation_id=request.POST['worklocation'],
                                    department_id=request.POST['department'],
                                    DUHead=duhead,
                                    companyemailid = request.POST['companyemailid'],
                                    reportingto = request.POST['reportingname'],
                                    reportingtoId = request.POST['reportingmanager'],
                                    reportingdepartment = request.POST['reportingdepartment'])
            emailid = request.POST['companyemailid']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            emplevel = request.POST['empllevel']
            fromdate = request.POST['joined_date']
            personal.save()
            empid = personal.id
            assigning_leave_structure(request,emplevel,fromdate,empid)
            # assigning_payscale(request,emplevel,fromdate,empid)
            password = password_generator(request)
            register(request,emailid,fname,lname,password)
            emailtemplate = Emailtemplate.objects.filter(title = 'Welcome Email')
            for temp in emailtemplate:
                template = temp.description
            clean = re.compile('<.*?>')
            emailtemplate = re.sub(clean, '', str(template))
            mailtemplate = emailtemplate.replace("Name",(request.POST['first_name']+" "+request.POST['middle_name'] +" "+request.POST['last_name'])).replace("user",request.POST['companyemailid']).replace("pword",password).replace("&nbsp;", "")
            sendemail(request,emailid,mailtemplate)
            return redirect('/pim/employeelist/')
        else:
            response_data["is_success"] = False
            return JsonResponse(response_data)
    else:
        levels = Leveldefinition.objects.all().order_by('levelName')
        personals = Personal_details.objects.all()
        jobtitles = Job.objects.all().order_by('jobtitle')
        jobgrades = Jobgrade.objects.all().order_by('jobgrade')
        employmentstatus = Employmentstatus.objects.all().order_by('employementstatus')
        locations = Location.objects.all().order_by('location')
        departments = Department.objects.all().order_by('departmentname')
        Shiftdetails = ShiftDetails.objects.all()
        return render(request,'pim/personaldetails.html',{'personals':personals,
                                                    'jobtitles':jobtitles,
                                                    'jobgrades':jobgrades,
                                                    'employmentstatus':employmentstatus,
                                                    'locations':locations,
                                                    'departments':departments,
                                                    'levels': levels,
                                                    'Shiftdetails':Shiftdetails})

def sendemail(request,emailid,mailtemplate):
    if request.method == 'POST':
        subject = 'Login Details'
        recepient = str(emailid)
        message = mailtemplate
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def register(request,mail,fname,lname,pword):
    user = User.objects.create_user('xyz', 'xyz@gmail.com' , 'password')
    user.username = mail
    user.first_name = fname
    user.last_name = lname
    user.email = mail
    user.set_password(pword) 
    user.is_staff = True
    user.save()
    my_group = Group.objects.get(name='Employee') 
    my_group.user_set.add(user)

def assigning_leave_structure(request,emplevel,fromdate,empid):
    asslevel = AssigningLevelsToStructure.objects.filter(levels_id = emplevel).values_list('leavestructureid_id',flat=True).first()
    assignedleavedata = AssignLeaveStructure(
        fromDate = fromdate,
        toDate = '2099-12-31',
        updatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status = True,
        empid_id = empid,
        leave_structure_id = asslevel
    )
    assignedleavedata.save()

def assigning_payscale(request,emplevel,fromdate,empid):
    asslevel = AssigningLevelsToPayscale.objects.filter(levels_id = emplevel).values_list('payscalenameid_id',flat=True).first()
    assignedleavedata = AssignPayscale(
        fromDate = fromdate,
        toDate = '2099-12-31',
        updatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status = True,
        empid_id = empid,
        pay_scale_id = asslevel
    )
    assignedleavedata.save()

def change_leave_structure(request):
    leaves = AssignLeaveStructure.objects.all().select_related('leave_structure')
    for leave in leaves:
        lid = leave.id
        start_date = leave.fromDate
        end_date = date.today() 
        delta = relativedelta.relativedelta(end_date,start_date)
        months = delta.years * 12 + delta.months
        expfrom = leave.leave_structure.experienceto
        if months >= leave.leave_structure.experienceto:
            todate = date.today()
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            empid = leave.empid.id
            leavestructure = leave.leave_structure.id
            create_new_leave_structure(request,empid,leavestructure,expfrom,lid)
            replaceddata = AssignLeaveStructure.objects.filter(id = lid)
            replaceddata.update(fromDate = start_date,toDate = todate,updatedDate = updated_at,status = False,empid_id = leave.empid.id,leave_structure_id = leave.leave_structure.id)
            for i in replaceddata:
                i.save()
        else:
            pass

def create_new_leave_structure(request,empid,leavestructure,expfrom,lid):
    fromdate = date.today()
    experiences = Leavestructure.objects.filter(experincefrom = expfrom).get().id
    assigningdata = AssignLeaveStructure(
        fromDate = fromdate,
        toDate = '2099-12-31',
        updatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status = True,
        empid_id = empid,
        leave_structure_id = experiences
    )
    updatedata = AssignLeaveStructure.objects.filter(id = lid)
    updatedata.update(leave_structure = experiences)
    assigningdata.save()

def change_pay_scale(request):
    pays = AssignPayscale.objects.all().select_related('pay_scale')
    for pay in pays:
        pid = pay.id
        start_date = pay.fromDate
        end_date = date.today() 
        delta = relativedelta.relativedelta(end_date,start_date)
        months = delta.years * 12 + delta.months
        expfrom = pay.pay_scale.experienceto
        if months >= pay.pay_scale.experienceto:
            todate = date.today()
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            empid = pay.empid.id
            payscale = pay.pay_scale.id
            create_new_pay_scale(request,empid,payscale,expfrom,pid)
            replaceddata = AssignPayscale.objects.filter(id = pid)
            replaceddata.update(fromDate = start_date,toDate = todate,updatedDate = updated_at,status = False,empid_id = pay.empid.id,pay_scale_id = pay.pay_scale.id)
            for i in replaceddata:
                i.save()
        else:
            pass

def create_new_pay_scale(request,empid,payscale,expfrom,pid):
    fromdate = date.today()
    experiences = PayScale.objects.filter(experincefrom = expfrom).get().id
    assigningdata = AssignPayscale(
        fromDate = fromdate,
        toDate = '2099-12-31',
        updatedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status = True,
        empid_id = empid,
        pay_scale_id = experiences
    )
    updatedata = AssignPayscale.objects.filter(id = pid)
    updatedata.update(pay_scale = experiences)
    assigningdata.save()

def password_generator(request):
    MAX_LEN = 8

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%',  '?', '/','*']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    password = ""
    for x in temp_pass:
            password = password + x
    return password

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
    Shiftdetails = ShiftDetails.objects.all()
    return render(request,'pim/editdetails.html',{'title':'Edit Employee List','personal':personal,
                                                'jobtitles':jobtitles,
                                                'jobgrades':jobgrades,
                                                'employmentstatus':employmentstatus,
                                                'locations':locations,
                                                'departments':departments,
                                                'levels':levels,
                                                'Shiftdetails':Shiftdetails,
                                                'reportingmanagers':reportingmanagers})                                              

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
    personal.work_shifts_id = request.POST['work_shifts_id']
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
    reportingmanagers = Personal_details.objects.filter(department_id=deptid, job_grade_id__gte = idgrade)
    rlist=[]
    for reportingmanager in reportingmanagers:
        r={}
        r['id']=reportingmanager.id
        r['value']=reportingmanager.first_name+' '+reportingmanager.middle_name+' '+reportingmanager.last_name
        rlist.append(r)
    reportingmanagers = rlist
    return JsonResponse(reportingmanagers, safe=False)


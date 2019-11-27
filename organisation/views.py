from django.shortcuts import render,redirect
from masters.models import Job,Jobgrade
from organisation.models import Leveldefinition, LevelDesignation, LevelGrades
from pim.models import Personal_details
from django.http import HttpResponse,Http404,JsonResponse
import json

def addlevel(request):
    if request.method == 'POST':
        designations = request.POST.getlist('designations')
        grades = request.POST.getlist('grades')
        leveldetails = Leveldefinition(levelName = request.POST['levelName'],
                                       shortName = request.POST['shortname'],
                                       parentlevel = request.POST['parent']
                                       )   
        leveldetails.save()
        levelid = leveldetails.id
        for desigationval in designations:
            desigationleveldata = LevelDesignation(
                levelid_id = levelid,
                designations_id = desigationval
            )
            desigationleveldata.save()
        
        for gradeval in grades:
            gradeleveldata = LevelGrades(
                levelid_id = levelid,
                grades_id = gradeval
            )
            gradeleveldata.save()
        return  redirect('login:dashboard')
    else:
        levels = Leveldefinition.objects.all().order_by('levelName')
        grades = Jobgrade.objects.all().order_by('jobgrade')
        alldesignations = Job.objects.all()
        return render(request,'levels.html',{'levels':levels, 'allgrades': grades,'alldesignations': alldesignations,'title':'Add Level'})

def orgchart(request):
    return render(request,'orgchart.html',{'title':'Organisation Chart'})

def orgchartdata(request):
    emplist = Personal_details.objects.all().select_related('job_title').order_by('employmentLevel_id','job_grade_id','reportingdepartment')
    levelslist=[]
    i=1
    for emplists in emplist:
        g=[]
        if i==1:
            g.append(emplists.first_name+' '+emplists.middle_name+' '+emplists.last_name)
            g.append('')
            g.append(emplists.job_title.jobtitle)
            i=i+1
        else:
            g.append(emplists.first_name+' '+emplists.middle_name+' '+emplists.last_name)
            g.append(emplists.reportingto)
            g.append(emplists.job_title.jobtitle)
        levelslist.append(g)
    levels = levelslist
    return JsonResponse(levels, safe=False)


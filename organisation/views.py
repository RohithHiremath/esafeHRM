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
        return  redirect('/organisation/levelslist')
    else:
        levels = Leveldefinition.objects.all().order_by('levelName')
        grades = Jobgrade.objects.all().order_by('jobgrade')
        alldesignations = Job.objects.all()
        return render(request,'levels.html',{'levels':levels, 'allgrades': grades,'alldesignations': alldesignations,'title':'Add Level'})

def levelslist(request):
    levels = Leveldefinition.objects.all()
    allgrades = Jobgrade.objects.all()
    alldesignations = Job.objects.all()
    for level in levels:
        leveldesignation = LevelDesignation.objects.filter(levelid_id = level.id).select_related('designations')
        if level.parentlevel == 0:
            parentlevel = 'Top Level'
        else:
            parentlevel = Leveldefinition.objects.get(id = level.parentlevel)
        level.parent = parentlevel
        level.assigneddesignations = leveldesignation
        grades = LevelGrades.objects.filter(levelid_id = level.id).select_related('grades')
        level.assignedgrades = grades
    return render(request,'levelslist.html',{'title':'Organisation Chart','leveldetails':levels,'alldesignations':alldesignations,'allgrades':allgrades})

def updatelist(request,id):
    if request.method == "POST":
        levels = LevelDesignation(levelid_id=id,designations_id=request.POST['designation'])
        levels.save()
        grade = LevelGrades(levelid_id=id,grades_id=request.POST['grade'])
        grade.save()
        return redirect('/organisation/levelslist')
    else: 
        return redirect('/organisation/levelslist')

def delete(request, id):
    grade = Leveldefinition.objects.get(id=id)
    grade.delete()
    return redirect('/organisation/levelslist')

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


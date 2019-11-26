from django.shortcuts import render,redirect
from masters.models import Job,Jobgrade
from organisation.models import Leveldefinition, LevelDesignation, LevelGrades
import json
# Create your views here.

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
    # levels = Leveldefinition.objects.all().order_by('-levelName')
    levels=[
          [{'v':'Chairman', 'f':'Mike<div style="color:red; font-style:italic">President</div>'},
           '', 'The President'],
          [{'v':'Jim', 'f':'Jim<div style="color:red; font-style:italic">Vice President</div>'},
           'Mike', 'VP'],
          ['Alice', 'Mike', ''],
          ['Bob', 'Mike', 'Bob Sponge'],
          ['Carol', 'Mike', '']
        ] 
    myJson = json.dumps(levels)
    return render(request,'orgchart.html',{'title':'Organisation Chart','levels':myJson})

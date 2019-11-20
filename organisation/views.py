from django.shortcuts import render,redirect
from masters.models import Job,Jobgrade
from organisation.models import Leveldefinition
import json
# Create your views here.

def addlevel(request):
    if request.method == 'POST':
        designations = request.POST.getlist('designations')
        grades = request.POST.getlist('grades')
        leveldetails = Leveldefinition(levelName = request.POST['levelName'],
                                       shortName = request.POST['shortname'],
                                       designations = designations,
                                       grades = grades,
                                       parentlevel = request.POST['parent']
                                       )   
        leveldetails.save()
        return  redirect('login:dashboard')
    else:
        levels = Leveldefinition.objects.all().order_by('levelName')
        grades = Jobgrade.objects.all().order_by('jobgrade')
        alldesignations = Job.objects.all()
        return render(request,'levels.html',{'levels':levels, 'allgrades': grades,'alldesignations': alldesignations,'title':'Add Level'})

def orgchart(request):
    levels = Leveldefinition.objects.all().order_by('-levelName')
    # levels=[
    #       [{'v':'Chairman', 'f':'Mike<div style="color:red; font-style:italic">President</div>'},
    #        '', 'The President'],
    #       [{'v':'Jim', 'f':'Jim<div style="color:red; font-style:italic">Vice President</div>'},
    #        'Mike', 'VP'],
    #       ['Alice', 'Mike', ''],
    #       ['Bob', 'Mike', 'Bob Sponge'],
    #       ['Carol', 'Mike', '']
    #     ] 
    # myJson = json.loads(levels)
    return render(request,'orgchart.html',{'title':'Organisation Chart','levels':levels})

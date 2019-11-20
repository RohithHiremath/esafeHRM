from django.shortcuts import render,redirect
from .models import Salarycomponent

# Create your views here.
def component(request):
    if request.method == 'POST':
        component = Salarycomponent(componentname=request.POST['componentname'],types=request.POST['types'])
        component.save()
        return redirect('component')
    else:
        components = Salarycomponent.objects.all().order_by('componentname','types')
    return render(request,'salarycomponents.html',{'title':'component List','components':components})
from django.shortcuts import render,redirect
from django.http import JsonResponse
from payroll.models import Salarycomponent, PayScale, Linktocomponent, AssigningLevelsToPayscale
from organisation.models import Leveldefinition

# Create your views here.
def component(request):
    if request.method == 'POST':
            component = Salarycomponent(componentname=request.POST['componentname'],types=request.POST['types'])
            component.save()
            return redirect('/payroll/component/')
    else:
        components = Salarycomponent.objects.all().order_by('componentname')
    return render(request,'salarycomponents.html',{'title':'component List','components':components})

def componentajax(request):
    if request.method == 'POST':
        response_data = {}
        structure = None
        structure = Salarycomponent.objects.filter(componentname = request.POST['componentname'])
        if not structure:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editcomponent(request, id):
    if request.method == 'POST':
        cat = Salarycomponent.objects.get(id=id)
        cat.componentname = request.POST['componentname']
        cat.types = request.POST['types']
        cat.save()
        return redirect('/payroll/component/')
    else:
        return redirect('/payroll/component/')

def editcomponentajax(request, id):
    if request.method == 'POST':
        response_data = {}
        structure = None
        structure = Salarycomponent.objects.filter(componentname = request.POST['componentname'])
        structureid = Salarycomponent.objects.get(id = id)
        if structureid in structure:
            response_data["is_success"] = True
        else:
            if not structure:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)
        
def payscalelist(request):
    if request.method == 'POST':
        orglevels = request.POST.getlist('addlevels')
        payscale = PayScale(payscalename=request.POST['payscalename'],
                            description=request.POST['description'],
                            shortname=request.POST['shortname'],
                            experincefrom=request.POST['experincefrom'],
                            experienceto=request.POST['experienceto'])
        payscale.save()
        payid = payscale.id
        for payval in orglevels:
            organisationleveldata = AssigningLevelsToPayscale(
                payscalenameid_id = payid,
                levels_id = payval
            )
            organisationleveldata.save()
        return redirect('/payroll/payscale/')
    else:
        payscales = PayScale.objects.all()
        orglevel = Leveldefinition.objects.all().order_by('levelName')
        for leavesww in payscales:
            levels = AssigningLevelsToPayscale.objects.filter(payscalenameid_id=leavesww.id).select_related('levels').order_by('levels__levelName')
            leavesww.assignedlevels = levels
    return render(request,'payscale.html',{'title':'Payscale List','payscales':payscales,'orglevel':orglevel})

def payscaleajax(request):
    if request.method == 'POST':
        response_data = {}
        structure = None
        structure = PayScale.objects.filter(payscalename = request.POST['payscalename'])
        if not structure:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def payshortajax(request):
    if request.method == 'POST':
        response_data = {}
        struc = None
        struc = PayScale.objects.filter(shortname = request.POST['shortname'])
        if not struc:
            response_data["is_success"] = True
        else:
            response_data["is_success"] = False
        return JsonResponse(response_data)

def editpayscale(request, id):
    if request.method == 'POST':
        pay = PayScale.objects.get(id=id)
        pay.payscalename = request.POST['payscalename']
        pay.shortname = request.POST['shortname']
        pay.description = request.POST['description']
        pay.experincefrom=request.POST['experincefrom']
        pay.experienceto=request.POST['experienceto']
        pay.save()
        payid = pay.id
        orglevels = request.POST.getlist('editlevels')
        dell = AssigningLevelsToPayscale.objects.filter(payscalenameid_id = payid).all()
        dell.delete()
        for payval in orglevels:
            organisationleveldata = AssigningLevelsToPayscale(
                payscalenameid_id = payid,
                levels_id = payval
            )
            assign = AssigningLevelsToPayscale.objects.filter(payscalenameid_id = payid, levels_id = payval).distinct()
            if not assign:
                organisationleveldata.save()
        return redirect('/payroll/payscale/')
    else:
        return redirect('/payroll/payscale/')

def editpayscaleajax(request, id):
    if request.method == 'POST':
        response_data = {}
        structure = None
        structure = PayScale.objects.filter(payscalename = request.POST['payscalename'])
        structureid = PayScale.objects.get(id = id)
        if structureid in structure:
            response_data["is_success"] = True
        else:
            if not structure:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def editpayshortajax(request, id):
    if request.method == 'POST':
        response_data = {}
        struc = None
        struc = PayScale.objects.filter(shortname = request.POST['shortname'])
        strucid = PayScale.objects.get(id = id)
        if strucid in struc:
            response_data["is_success"] = True
        else:
            if not struc:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        return JsonResponse(response_data)

def relationwithcomp(request, id):
    if request.method =="POST":
        link = Linktocomponent(payscale_name_id = id,component_name_id=request.POST['component_name'])
        link.save()
        return redirect('/payroll/relationwithcomp/'+str(id)+'/')
    else:
        pscale = PayScale.objects.get(id=id)
        components = Salarycomponent.objects.all()
        linkeddetails = Linktocomponent.objects.filter(payscale_name_id=id).select_related('component_name')
        return render(request,'linktocomp.html',{'linkeddetails':linkeddetails,'components':components,'pscale':pscale})

def delete(request, id, idpay):
    job = Linktocomponent.objects.get(id=id)
    job.delete()
    return redirect('/payroll/relationwithcomp/'+str(idpay)+'/')

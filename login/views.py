from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            return render(request, 'login/dashboard.html', {'title':'Dashboard'})
        else:
            return render(request,'login/login.html',{'title':'Invalid Login'})
    else:
        return render(request,'login/login.html',{'title':'Login'})

def dashboard(request):
    return render(request,'login/dashboard.html',{'title':'Login'})
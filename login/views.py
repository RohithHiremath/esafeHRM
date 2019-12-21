from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Permission
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from leaves.models import LeaveDetails

# Create your views here.
 
def index(request):
    return render(request,'login/login.html',{'title':'Login'})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
             # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to Dashboard.
            return  redirect('login:dashboard')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('login:login')
    else:
        return redirect('/')

def dashboard(request):
    leaverequestcount = LeaveDetails.objects.filter(Status=1).count()
    return render(request,'login/dashboard.html',{'title':'dashboard','requestcount':leaverequestcount})

def logout(request):
    auth.logout(request)
    # Redirect to a login page.
    return redirect('/')
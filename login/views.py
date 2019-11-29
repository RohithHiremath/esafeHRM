from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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
            return redirect('login')
    else:
        return redirect('/')

def dashboard(request):
    print(request.user.is_authenticated)
    return render(request,'login/dashboard.html',{'title':'dashboard'})

def logout(request):
    auth.logout(request)
    # Redirect to a login page.
    return redirect('/')
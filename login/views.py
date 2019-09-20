from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
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
            return  redirect('dashboard')
            # render(request, 'login/dashboard.html', {'title':'Dashboard'})
        else:
            return redirect('login')
    else:
        return render(request,'login/login.html',{'title':'Login'})

def dashboard(request):

    return render(request,'login/dashboard.html',{'title':'Login'})


def logout(request):
    auth.logout(request)
    # Redirect to a login page.
    return render(request,'login/login.html',{'title':'Login'})
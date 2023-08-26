from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


# Create your views here.
def logoutPage(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.method in ["POST"]:
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', { "error": "Wrong username or password"})
        
    return render(request, 'login.html')

def signup(request):
    if request.method in ["POST"]:
        username = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")
        
        if password == re_password:
            
            try:
                User.objects.create_user(username=username, password=password)
                return redirect('login')
            except IntegrityError as e:
                if "UNIQUE constraint failed" in str(e.args):
                    return render(request, 'signup.html', { "error": "Username already taken"})
                return render(request, 'signup.html', { "error": e })
        else:
            return render(request, 'signup.html', { "error": "Passwords don't match"})
        
    return render(request, 'signup.html')

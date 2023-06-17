from django.shortcuts import render, HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def index(request):
    # View logic for the index page
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
       
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password does not match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
            
    # View logic for the signup page
    return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

    # View logic for the login page
    return render(request, 'login.html')
@login_required(login_url='login')
def home(request):
    # View logic for the home page
    return render(request, 'home.html')
def Logout(request):
    logout(request)
    return redirect('index')
def signup2(request):
    # if request.method=='POST':
    #     usname=request.POST.get('username')
    #     email=request.POST.get('email')
    #     pass1=request.POST.get('password1')
    #     pass2=request.POST.get('password2')
       
    #     if pass1!=pass2:
    #         return HttpResponse("Your password and confirm password does not match")
    #     else:
    #         my_user=User.objects.create_user(uname,email,pass1)
    #         my_user.save()
    #         return redirect('login2')
            
    # View logic for the signup page
    return render(request, 'signup2.html')
def login2(request):
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     pass1=request.POST.get('pass')
    #     user=authenticate(request,username=username,password=pass1)
    #     if user is not None:
    #         auth_login(request,user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse("Username or Password is incorrect")

    # View logic for the login page
    return render(request, 'login2.html')
def home2(request):
    # View logic for the home page
    return render(request, 'home2.html')
def form(request):
    return render(request,'form.html')


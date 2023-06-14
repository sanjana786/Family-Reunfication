from django.shortcuts import render

def index(request):
    # View logic for the index page
    return render(request, 'index.html')

def signup(request):
    # View logic for the signup page
    return render(request, 'signup.html')

def login(request):
    # View logic for the login page
    return render(request, 'login.html')

def home(request):
    # View logic for the home page
    return render(request, 'home.html')

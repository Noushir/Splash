from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def sign_up(request):
    return render(request,'signup.html')

def dash(request):
    return render(request,'dash.html')


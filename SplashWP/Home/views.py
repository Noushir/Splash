from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def sign_up(request):
    if request.method=='POST':
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2 :
            return HttpResponse("The password doesn't match!!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')
        print(uname,email,pass1,pass2)
    return render(request,'signup.html')

def dash(request):
    return render(request,'dash.html')


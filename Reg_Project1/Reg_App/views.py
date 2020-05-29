from django.shortcuts import render
from .models import Register_Data
from django.http import HttpResponse

# Create your views here.

def Register_View(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        mobile=request.POST.get('mobile')

        data=Register_Data(
            fname=fname,
            lname=lname,
            username=username,
            password=password,
            mobile=mobile
            )
        data.save()
        return render(request,'Reg_App/index.html')

    else:
        return render(request,'Reg_App/index.html')


def Login_View(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Register_Data.objects.filter(username=username,password=password)

        if not user:
            return HttpResponse('Incorrect Username or Password')
        else:
            return HttpResponse('Login Sucess')

    else:
        return render(request,'Reg_App/login.html')


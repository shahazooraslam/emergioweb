from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Careers,Applyform

# Create your views here.
def Home(request):
    return render(request,"index.html")
def Courses(request):
    return render(request,"review.html")
def Contact(request):
    return render(request,"contact.html")
@login_required
def Career(request):
    return render(request,"categories.html")

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"your account has been created")
        return redirect("/signin/")

    return render(request,"register.html")
def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request,"index.html")
            # return HttpResponse("logged in successfully")
        else:
            messages.error(request,"login failed")
            return redirect("/signup/")
    return render(request,"signin.html")
def logoutview(request):
    logout(request)
    return redirect("index/")
def pdf(request):
    if request.user.is_authenticated:
     
     return render(request,"pdf.html")
    else:
        return redirect("signin/")
def searchvenues(request):
    if request.user.is_authenticated:
     if request.method=="POST":
      searched=request.POST["search"]
      career=Careers.objects.filter(name__contains=searched)
      return render(request,"searchvenues.html",{'searched1':searched,'career':career})
     else:
         return render(request,"searchvenues.html")
    else:
        return redirect("signin/")
def apply(request):
    if request.method=="POST":
        #  files=request.FILES['files']
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["tel"]
        position=request.POST["position"]
        experience=request.POST["experience"]
        cover=request.POST["cover"]
        file=request.FILES["file"]
        a=Applyform(name=name,email=email,phone=phone,position=position,experience=experience,cover_letter=cover,resume=file)
        a.save()
        return redirect("/carrer/")


    return render(request,"applyform.html")
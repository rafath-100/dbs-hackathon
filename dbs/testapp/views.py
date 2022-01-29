from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import User

def home(req):
    return HttpResponse("Hello World")

def signin(req):
    if(req.method=="POST"):
        name=req.POST["username"]
        pwd=req.POST["password"]
        data=User(username=name,password=pwd)
        data.save()
        return render(req,"testapp/login.html")

    return render(req,"testapp/signin.html")

def login(req):
    if(req.method=="POST"):
        username=req.POST["username"]
        password=req.POST["password"]
        try:
            data=User.objects.get(username=username)
            if(data.password==password):
                return HttpResponse("Login successful")
            return HttpResponse("Invalid Password")
        except:
            return HttpResponse("Username is not found")
    return render(req,"testapp/login.html")

def cus(req):
    return render(req,"testapp/customerscreen1.html")

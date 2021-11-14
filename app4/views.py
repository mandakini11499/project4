from django.contrib import messages
from django.shortcuts import render,redirect
from .models import UserModel
from .forms import UserForm

def showIndex(request):
    return render(request,"index.html")

def registerPage(request):
    uf=UserForm()
    return render(request,'register.html',{'form':uf})
from django.http import HttpResponseRedirect
def signupPage(request):
    uname = request.POST.get('username')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    cpwd = request.POST.get('cpassword')
    addrs = request.POST.get('address')
    UserModel(username=uname,email=email,password=pwd,cpassword=cpwd,address=addrs).save()
    return render(request,"index.html",{"message":"User Registered"})


def loginPage(request):
    um=UserModel.objects.all()
    email=request.POST.get('email')
    password=request.POST.get('pwd')
    try:
        um=UserModel.objects.get(email=email)
        if um:
            if um.password == password:
                request.session['email']=email
                return render(request,"welcome.html",{'data':UserModel.objects.all()})
            else:
                return render(request,"index.html",{'message':"Invalid password"})
    except:
        return render(request,"index.html",{'message':"Invalid email or Does not exits"})


def updatePage(request):
    id=request.POST.get('uid')
    um=UserModel.objects.get(id=id)
    return render(request,"update.html",{"data":um})


def updatedPage(request):
    uid = request.POST.get('id')
    uname = request.POST.get('uname')
    email = request.POST.get('uemail')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    addrs = request.POST.get('addr')
    UserModel(id=uid,username=uname, email=email, password=pwd, cpassword=cpwd, address=addrs).save()
    um=UserModel.objects.all()
    return render(request, "welcome.html", {"message": "User Updated","data":um})


def deleteUserPage(request):
    id=request.POST.get('uid')
    UserModel.objects.filter(id=id).delete()
    user=UserModel.objects.all()
    return render(request,"welcome.html",{'data':user})

    return None
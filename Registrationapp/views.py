from django.shortcuts import render, redirect
from .models import Registration
from .forms import *
# Create your views here.
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from textblob import TextBlob
from Registrationapp.models import Registration
from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    print('h5')
    return render(request,'index.html')

def registration(request):
        if request.method == "POST":
            form = Registrationform(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect()
                except:
                    pass
        else:
            form = Registrationform()
        return render(request,"form.html",{'form':form})

def tables(request):
    registrations = Registration.objects.all()
    return render(request, "tables.html", {"registrations": registrations})

def edit(request,id):
    registration= Registration.objects.get(id=id)
    return render(request,"edit.html",{"registration":registration})

def update(request,id):
    registration= Registration.objects.get(id=id)
    form =  Registrationform(request.POST, instance= registration)
    if form.is_valid():
        form.save()
        return redirect("/tables")
    return render(request,"edit.html",{'registration':registration})

def delete(request,id):
    registration= Registration.objects.get(id=id)
    registration.delete()
    return redirect("/tables")

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
             FirstName=request.POST['FirstName']
             LastName=request.POST['LastName']
             Username=request.POST['Username']
             Email   =request.POST['Email']
             Password1=request.POST['Password1']
             Password2=request.POST['Password2']
             if Password1==Password2:
                if Registration.objects.filter(Username=Username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('/Register')
                elif Registration.objects.filter(Email=Email).exists():
                    messages.info(request,'Email Taken')
                    return redirect('/Register')
                else :
                    Registration.objects.filter(FirstName=FirstName,LastName=LastName,Username=Username,Email=Email,Password1=Password1)
                    form.save()
                    print("hello")

                    return redirect('/Register')


             else:
                messages.info(request, 'Password Is not maching')
                return redirect('/Register')
        else:
                form = RegisterForm()
                return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
     if request.method=='POST':
         form = RegisterForm(request.POST or None)
         if form.is_valid():
            Email=request.POST['Email']

            Password1=request.POST['Password1']

            user=auth.authenticate(Email=Email,Password1=Password1)
            print('h1')

            if user is not None:
                auth.login(request,user)
                print('h2')
                return redirect('/index')

            else:
               messages.info(request,'Invalid creadential')
               print('h3')
               return redirect('/login')

     else:
         form = RegisterForm()
         print('h4')
     return render(request,'login.html',{'form': form})



def search( request):
    if request.method=='POST':


        srch = request.POST['srh']
        srh = srch.read()
        srch = TextBlob(srh.correct)

        if srch:
            match= Registration.objects.filter(
                                         Q(eid__iexact=srch)|
                                         Q(ename__istartswith=srch)|
                                         Q(email__icorrect =srch)
                                         )

            if match:
                return render(request,'search.html',{'sr' : match})
            else:
                Registration.error(request,'No Result Found')

        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')



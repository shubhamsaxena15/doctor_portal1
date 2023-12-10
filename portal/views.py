from imaplib import _Authenticator
from django.template import loader
from django.shortcuts import render
from .models import member
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,"login.html")

def register(request):
    return render(request,"signup.html")


def signup(request ):
    if request.method == 'POST':
        users = str(request.POST['users'])
        firstname = str(request.POST['firstname'])
        lastname = str(request.POST['lastname'])
        username = str(request.POST['username'])
        email = str(request.POST['email'])
        picture = (request.POST['picture'])
        phonenumber = int(request.POST['phonenumber'])
        password = str(request.POST['password'])
        confirmpassword = str(request.POST['confirmpassword'])
        address = str(request.POST['address'])
        
        data=member.objects.filter(username=username)
        if data:
            return HttpResponse("User Name already exists")
            
        elif password==confirmpassword:
            en = member(users=users,firstname=firstname,lastname=lastname,username=username,email=email,picture=picture,phonenumber=phonenumber,password=password,confirmpassword=confirmpassword,address=address)
            en.save()
            return render(request,"signup.html")
        else:
            return HttpResponse("both password should be same")
        
        
        
def loginview(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password2 = request.POST['password']
        
        mydata = member.objects.filter(username=username1, password=password2).values()
        
        if mydata:
            messages.success(request, "Login Successfully")
            mydata1 = member.objects.filter(username=username1).values()
            template = loader.get_template('profileview.html')
            context = {
                'mymembers': mydata1,
                }
            return HttpResponse(template.render(context, request))
        else:
            messages.warning(request, "Invalid Detail")
            return redirect('index')
        

    
    
    
    
        
        
        
        
        
        
    
    
        
       
        

            
        


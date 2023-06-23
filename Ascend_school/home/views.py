from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest
from .models import students

# Create your views here.
def index (request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pword=request.POST['pword' ]
        user=auth.authenticate(username=uname,password=pword)
        if user:

            
            auth.login(request,user)
            
            return redirect('/')
            
        msg='invalid user name and password'  
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

    

def register(request):
    if request.method=='POST':
      uname=request.POST['uname']
      fname=request.POST['fname']
      lname=request.POST['lname']
      email=request.POST['email']
      pword=request.POST['pword']
      rpword=request.POST['rpword']
      if pword==rpword:
            if User.objects.filter(username=uname):
                msg="username is already taken"
                return render(request,'register.html',{'val':msg})
            elif User.objects.filter(email=email):
                msg="email is already taken"
                return render(request,'register.html',{'val':msg})
            
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pword) 
                user.save();
                auth.login(request,user) 
                return redirect("/")
                
      else:
            msg="invalid password"
            return render(request,'register.html',{'val':msg})
    else:
        return render(request,"register.html") 
    
def logout(request):
    auth.logout(request)
    return redirect('/')
  

    

def about(request):
    return render(request,'about.html')

def admission(request):
    data=[{'name':"science"},{'name':'commerce'},{'name':'humanities'}]
    
    if request.method=='POST':
        
        ad_no=request.POST['ad_no']
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        subject=request.POST['subject']
        gname=request.POST['gname']
        dob=request.POST['dob']
        ctno=request.POST['ctno']
        
        if students.objects.filter(admission_no=ad_no):
            msg='Admision number already exists..!'
            return render(request,'admission.html',{'msg':msg ,'sdata':data})
        else:
            s_obj=students.objects.create(admission_no=ad_no,name=name,age=age,place=place,subject=subject,guardian_name=gname,date_of_birth=dob,contact_detais=ctno)
            s_obj.save()
            msg='student added succesfully '
            return render(request,'admission.html',{'msg':msg ,'sdata':data})
    else:
        if not request.user.is_staff:
            return redirect('/')
        else:
            return render(request,'admission.html',{'sdata':data}) 
    

def table(request):
    obj=students.objects.all
    return render(request,'table.html',{'data':obj})






def testsub_s(request):
     obj_s=students.objects.filter(subject='science')
     return render(request,'science.html',{'data':obj_s})
def testsub_c(request):
     obj_c=students.objects.filter(subject='commerce')
     return render(request,'commerce.html',{'data':obj_c})
def testsub_h(request):
     obj_h=students.objects.filter(subject='humanities')
     return render(request,'humanities.html',{'data':obj_h})
from django.shortcuts import render,redirect,reverse
from.models import Enquiry,Student,Login
from datetime import date
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from adminapp.models import Events,Program, Branch, Year
from . import smssender
# Create your views here.
def index(request):
    einfo=Events.objects.all()
    return render(request,"index.html",locals())
def aboutus(request):
    einfo=Events.objects.all()
    return render(request,"aboutus.html",locals())
def registration(request):
    einfo=Events.objects.all()
    program1=Program.objects.all()
    branch1=Branch.objects.all()
    year1=Year.objects.all()
    print(year1)
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        photo=request.FILES['photo']
        # ---------------------------------------orm - object realtionship method [next two is meaning]---------------------------------------------------------------------
        stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate,profile_pic=photo)
        log=Login(userid=rollno,password=password,usertype=usertype,status=status)
        
        stu.save()
        log.save()
        subject='important email from E-gyan Portal'
        msg=f'Hello,{name}Your Registration Is Successfull. Your Password is {password}'
        email_from=settings.EMAIL_HOST_USER
    
        send_mail(subject,msg,email_from,[emailaddress])
        messages.success(request,"Student Registration Successful ")
    return render(request,"registration.html",locals())
def login(request):
    einfo=Events.objects.all()
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        usertype=request.POST['usertype']
        try:
            obj=Login.objects.get(userid=userid,password=password,usertype=usertype)
            if obj.usertype=="student":
                #messages.success(request,'Welcome ff')
                request.session['rollno']=userid #session variable create kiya jiski id roll no hai
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                # messages.success(request,'Welcome Admin')
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.success(request,'Invalid User')
    return render(request,"login.html",locals())
def contactus(request):
    einfo=Events.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        smssender.sendsms(contactno)
        messages.success(request,"Your Enquiry Is Submitted")
    return render(request,"contactus.html",locals())
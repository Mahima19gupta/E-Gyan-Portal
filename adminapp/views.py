from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from nouapp.models import Student, Enquiry, Login
from studentapp.models import StuResponse
from django.contrib import messages
from . models import Program, Branch, Year, Material,Events,Course,Question
from datetime import date
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,"adminhome.html",{'adminid':adminid})
    except KeyError:
        return redirect(request,"nouapp:login")

def adminlogout(request):
    try:
        del request.session['adminid']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudent(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            student=Student.objects.all()
            return render(request,"viewstudent.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            return render(request,"viewenquiry.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            feed=StuResponse.objects.filter(responsetype='feedback')
            return render(request,"viewfeedback.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            comp=StuResponse.objects.filter(responsetype='complain')
            return render(request,"viewcomplain.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studymaterial(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            program=Program.objects.all()
            branch=Branch.objects.all()
            year=Year.objects.all()
            return render(request,"studymaterial.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def move(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            program=request.POST['program']
            branch=request.POST['branch']
            year=request.POST['year']
            subject=request.POST['subject']
            filename=request.POST['filename']
            myfile=request.FILES['myfile']
            mt=Material(program=program,branch=branch,year=year,subject=subject,file_name=filename,my_file=myfile)
            mt.save()
            return render(request,"studymaterial.html",{'adminid':adminid})
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudymaterial(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            materials=Material.objects.all()
            return render(request, "viewstudymaterial.html",locals())
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def news(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=='POST':
                eventname=request.POST['eventname']
                eventdate=date.today()
                e=Events(event=eventname,eventdate=eventdate)
                e.save()
            einfo=Events.objects.all()
            return render(request,"news.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
def deleteevent(request,eid):
    emp=Events.objects.get(eventid=eid)
    emp.delete()
    return redirect('adminapp:news')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminchangepassword(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=='POST':
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                presentpassword=Login.objects.get(usertype="admin")
                if currentpassword==presentpassword.password:
                    if newpassword!=presentpassword.password:
                        if newpassword==confirmpassword:
                            Login.objects.filter(usertype="admin").update(password=newpassword)
                            return redirect('adminapp:adminlogout')
                        else:
                            messages.warning(request,"Confirm Password Not Matched ")
                    else:
                        messages.warning(request,"Current Password is Wrong")
                else:
                    messages.warning(request,"Sorry!!! You cannot Use Current Password")
            return render(request,"adminchangepassword.html",{'adminid':adminid})
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def admincourse(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,"admin_course.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminaddcourse(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=="POST":
                course_name=request.POST['coursename']
                total_question=request.POST['totalquestion']
                total_marks=request.POST['totalmarks']
                add=Course(course_name=course_name,question_number=total_question,total_marks=total_marks)
                add.save()
            return render(request,"adminaddcourse.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminviewcourse(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            courses = Course.objects.all()
            return render(request,"adminviewcourse.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletecourse(request,pk):
    try:
        if request.session['adminid']!=None:
            course=Course.objects.get(id=pk)
            course.delete()
            return redirect('adminapp:adminviewcourse')
    except KeyError:
        return redirect(request,"nouapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminquestion(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,"adminquestion.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminaddquestion(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            if request.method=="POST":
                course=request.POST['course']
                question=request.POST['question']
                marks=request.POST['marks']
                option1=request.POST['option1']
                option2=request.POST['option2']
                option3=request.POST['option3']
                option4=request.POST['option4']
                answer=request.POST['answer']
                course=Course.objects.get(course_name=course)
                ad=Question(course=course,question=question,marks=marks,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
                ad.save()
            return render(request,"adminaddquestion.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminviewquestion(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            courses = Course.objects.all()
            return render(request,"adminviewquestion.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewquestion(request,pk):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            questions=Question.objects.all().filter(course_id=pk)
            return render(request,"viewquestion.html",locals())
    except KeyError:
        return redirect(request,"nouapp:login")
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletequestion(request,pk):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            question=Question.objects.get(id=pk)
            question.delete()
            return redirect('adminapp:adminviewquestion')
    except KeyError:
        return redirect(request,"nouapp:login")
from django.shortcuts import render,redirect
from nouapp.models import Student,Login
from django.views.decorators.cache import cache_control
from .models import StuResponse,Question,Answer
import datetime
from django.contrib import messages
from adminapp.models import Material,Course,Result
from adminapp.models import Question as qp
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def studenthome(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"studenthome.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
def studentlogout(request):
    try:
        del request .session['rollno'] #session delete
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def response(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=='POST':
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                responsedate=datetime.date.today()
                sr=StuResponse(rollno=stu.rollno,name=stu.name,program=stu.program,year=stu.year,branch=stu.branch,contactno=stu.contactno,emailaddress=stu.emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,responsedate=responsedate)
                sr.save()
                messages.success(request,"Response Submitted  ")
            return render(request,"response.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def postquestion(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=datetime.date.today()
                ques=Question(question=question,postedby=postedby,posteddate=posteddate)
                ques.save()
            ques=Question.objects.all()
            return render(request,"postquestion.html",{'stu':stu,'ques':ques})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def postanswer(request,qid):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"postanswer.html",{'stu':stu,'qid':qid})
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def postans(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answeredby=stu.name
            answerdate=datetime.date.today()
            ans=Answer(qid=qid,answer=answer,answeredby=answeredby,posteddate=answerdate)
            ans.save()
            return redirect("studentapp:postquestion")
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def viewanswer(request,qid):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)
            return render(request,"viewanswer.html",{'stu':stu,'ans':ans})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def changepassword(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=='POST':
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                presentpassword=Login.objects.get(userid=rollno)
                if currentpassword==presentpassword.password:
                    if newpassword!=presentpassword.password:
                        if newpassword==confirmpassword:
                            Login.objects.filter(userid=rollno).update(password=newpassword)
                            return redirect('studentapp:studentlogout')
                        else:
                            messages.warning(request,"Confirm Password Not Matched ")
                    else:
                        messages.warning(request,"Current Password is Wrong")
                else:
                    messages.warning(request,"Sorry!!! You cannot Use Current Password")   
            return render(request,"changepassword.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def viewprofile(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"viewprofile.html",{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def viewmat(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            mt=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year)
            return render(request,"viewmat.html",locals())
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def studentexam(request):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            courses=Course.objects.all()
            return render(request,"studentexam.html",{'stu':stu,'courses':courses})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def takeexam(request,pk):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            course=Course.objects.get(id=pk)
            total_questions=qp.objects.all().filter(course=course).count()
            questions=qp.objects.all().filter(course=course)
            total_marks=0
            for q in questions:
                total_marks=total_marks + q.marks
            return render(request,"takeexam.html",{'stu':stu,'course':course,'total_questions':total_questions,'total_marks':total_marks })
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)#(no_cache=True)for not saving cache(must_revalidate=True)for revalidating with server  (no_store=True)for not storing any data
def startexam(request,pk):
    # checking whether user login kar ke aaya hai ya nhi
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            course=Course.objects.get(id=pk)
            questions=qp.objects.all().filter(course=course)
            if request.method=='POST':
                pass
            response= render(request,'startexam.html',{'stu':stu,'course':course,'questions':questions})
            response.set_cookie('course_id',course.id)
            return response
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def calculatemarks(request):
       try:
            if request.session['rollno']!=None:
                rollno=request.session['rollno']
                stu=Student.objects.get(rollno=rollno)
                if request.COOKIES.get('course_id') is not None:
                    course_id = request.COOKIES.get('course_id')
                    course=Course.objects.get(id=course_id)
                    total_marks=0
                    questions=qp.objects.all().filter(course=course)
                    for i in range(len(questions)):
                        selected_ans = request.COOKIES.get(str(i+1))
                        actual_answer = questions[i].answer
                        if selected_ans ==  actual_answer:
                            total_marks = total_marks + questions[i].marks
                    student = stu
                    result =Result()
                    result.marks=total_marks
                    result.exam=course
                    result.student=student
                    result.date=datetime.datetime.now()
                    print(datetime.datetime.now())
                    result.save()
                return redirect("studentapp:viewresult")
       except KeyError:
           return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewresult(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            courses=Course.objects.all()
            return render(request,'viewresult.html',{'stu':stu,'courses':courses})
    except KeyError:
           return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def checkmarks(request,pk):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            course=Course.objects.get(id=pk)
            results= Result.objects.all().filter(exam=course).filter(student=stu)
            return render(request,'checkmarks.html',{'stu':stu,'results':results})
    except KeyError:
           return redirect('nouapp:login')
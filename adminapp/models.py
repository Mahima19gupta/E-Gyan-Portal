from django.db import models
from nouapp.models import Student
# Create your models here.
class Program(models.Model):
    program=models.CharField(max_length=100)
class Branch(models.Model):
    branch=models.CharField(max_length=100)
class Year(models.Model):
    year=models.CharField(max_length=100)
class Material(models.Model):
    ids=models.AutoField(primary_key=True)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    file_name=models.CharField(max_length=255)
    my_file=models.FileField(upload_to='')
class Events(models.Model):
    eventid=models.AutoField(primary_key=True)
    event=models.CharField(max_length=100)
    eventdate=models.CharField(max_length=100)
class Course(models.Model):
    course_name=models.CharField(max_length=50)
    question_number=models.PositiveIntegerField()
    total_marks=models.PositiveIntegerField()
    def __str__(self):
        return self.course_name
class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField()
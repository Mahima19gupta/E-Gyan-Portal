from django.urls import path
from . import views

urlpatterns=[
    path('adminwelcome/',views.adminhome,name="adminhome"),
    path('adminsessionred/',views.adminlogout,name="adminlogout"),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcomplain/',views.viewcomplain,name='viewcomplain'),
    path('studymaterial/',views.studymaterial,name='studymaterial'),
    path('move/',views.move,name='move'),
    path('viewstudymaterial/',views.viewstudymaterial,name='viewstudymaterial'),
    path('news/',views.news,name='news'),
    path('deleteevent/<eid>',views.deleteevent,name='deleteevent'),
    path('adminchangepassword/',views.adminchangepassword,name='adminchangepassword'),
    path('admincourse/',views.admincourse,name='admincourse'),
    path('adminaddcourse/',views.adminaddcourse,name='adminaddcourse'),
    path('adminviewcourse/',views.adminviewcourse,name='adminviewcourse'),
    path('deletecourse/<pk>',views.deletecourse,name='deletecourse'),
    path('adminquestion/',views.adminquestion,name='adminquestion'),
    path('adminaddquestion/',views.adminaddquestion,name='adminaddquestion'),
    path('adminviewquestion/',views.adminviewquestion,name='adminviewquestion'),
    path('viewquestion/<pk>',views.viewquestion,name='viewquestion'),
    path('deletequestion/<pk>',views.deletequestion,name='deletequestion'),
    
    
]
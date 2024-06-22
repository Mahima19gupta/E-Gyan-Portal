from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('studenthome/',views.studenthome,name='studenthome'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('response/',views.response,name='response'),
    path('postquestion/',views.postquestion,name='postquestion'), 
    path('postanswer/<qid>',views.postanswer,name='postanswer'), 
    path('postans/',views.postans,name='postans'),
    path('viewanswer/<qid>',views.viewanswer,name='viewanswer'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('viewmat/',views.viewmat,name='viewmat'),
    path('studentexam/',views.studentexam,name='studentexam'),
    path('takeexam/<pk>',views.takeexam,name='takeexam'),
    path('startexam/<pk>',views.startexam,name='startexam'),
    path('calculatemarks/',views.calculatemarks,name='calculatemarks'),
    path('viewresult/',views.viewresult,name='viewresult'),
    path('checkmarks/<pk>',views.checkmarks,name='checkmarks'),
]
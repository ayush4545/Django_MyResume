from django.urls import path
from . import views

urlpatterns = [
    path('skill/',views.skill,name='skill'),
    path('education/',views.education,name='education'),
    path('project/',views.project,name='project'),
    path('experience/',views.experience,name='experience'),
    path('training/',views.training,name='training'),
]

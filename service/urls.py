from django.urls import path
from . import views

urlpatterns = [
    path('service/',views.services,name='service'),
    path('achivement/',views.achivement,name='achivement'),
    path('personal_detail/',views.personal_detail,name='personal_detail'),
]

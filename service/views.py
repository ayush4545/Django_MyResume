from django.shortcuts import render

# Create your views here.
def services(request):
    context={'skill':'active'}
    return render(request,'service/services.html',context)


def achivement(request):
    context={'achivement':'active'}
    return render(request,'service/achivement.html',context)


def personal_detail(request):
    context={'detail':'active'}
    return render(request,'service/personal_detail.html',context)    
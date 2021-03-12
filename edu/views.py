from django.shortcuts import render

# Create your views here.
def skill(request):
    context={'skill':'active'}
    return render(request,'edu/skill.html',context)


def education(request):
    context={'education':'active'}
    return render(request,'edu/education.html',context)

def experience(request):
    context={'experience':'active'}
    return render(request,'edu/experience.html',context)

def project(request):
    context={'project':'active'}
    return render(request,'edu/project.html',context)        

def training(request):
    context={'training':'active'}
    return render(request,'edu/training.html',context)      
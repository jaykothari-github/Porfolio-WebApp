from urllib.request import Request
from django.shortcuts import redirect, render
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()[::-1]
    return render(request,'index.html',{'projects':projects})

def add_project(request):
    if request.method == 'POST':
        Project.objects.create(
            title = request.POST['title'],
            des = request.POST['des'],
            tech = request.POST['tech'],
            image = request.FILES['image'] if 'image' in request.FILES else None
        )
        projects = Project.objects.all()[::-1]
        return render(request,'index.html',{'projects':projects,'msg':'Project is Uploaded'})
    projects = Project.objects.all()[::-1]
    return render(request,'index.html',{'projects':projects})

def delete_project(request,pk):
    try:
        project = Project.objects.get(id=pk)
        project.delete()
    except:
        pass
    projects = Project.objects.all()[::-1]
    return render(request,'index.html',{'projects':projects})

def read_project(request,pk):
    project = Project.objects.get(id=pk)
    return render(request,'read-project.html',{'project':project})

def update_project(request,pk):
    project = Project.objects.get(id=pk)
    return
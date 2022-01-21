from django.contrib.auth.models import User
from django.shortcuts import render ,HttpResponseRedirect

from .admin import StudentAdmin
from .forms import  StudentRegistration
from .models import Student
# Create your views here.
def home(request):
    return render(request,'Admin/home.html')

def show_data(request):
    stud = Student.objects.all()
    return render(request,'Admin/viewstudent.html',{'stu':stud})


def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            # name=fm.cleaned_data['name']
            # email=fm.cleaned_data['email']
            # password=fm.cleaned_data['password']
            # reg=Student(name=name,email=email,password=password)
            # reg.save()
            fm.save()
            fm = StudentRegistration
    else:
        fm=StudentRegistration
    stud=Student.objects.all()

    return render(request,'Admin/addandshow.html',{'form':fm,'stu':stud})

def delete_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        # return HttpResponseRedirect('/')
        return render(request,'Admin/viewstudent.html')

def update_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
          fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'Admin/updatestudent.html',{'form':fm})
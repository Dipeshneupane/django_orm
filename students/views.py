from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.
def student(request):
    post = Student.objects.all()
    print(post.query)
    return render(request, 'output.html',{'post': post})

def student(request):
    Or = Student.objects.filter(Q (last_name__startswith = 'Neupane') |Q (last_name__startswith = 'Laamichhane'))
    return render(request, 'output.html', {'Or': Or})

def student(request):
    And = Student.objects.filter(classroom =1) & Student.objects.filter(last_name__startswith = 'Neupane')
    return render(request,'output.html',{'And':And})

def student(request):
    post = Student.objects.all().values_list('classroom').union(Teacher.objects.all().values_list('last_name'))
    return render(request,'output.html', {'post': post})


def student(request):
    post = Student.objects.exclude(age__gte=25)
    return render(request, 'output.html', {'post': post})

def student(request):
    post = Student.objects.filter(classroom = 1).only('first_name','last_name') 
    return render(request,'output.html',{'post':post.query})

def student(request):
    sql = "SELECT * FROM students_student"
    post = Student.objects.raw(sql)[1:]
    return render(request, 'output.html', {'post': post})

def student(request):
    post = Teacher.objects.all()
    return render(request,'output.html', {'post': post})
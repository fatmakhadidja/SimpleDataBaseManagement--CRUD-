from django.shortcuts import render
from .models import Student

def list_students(request):
        students = Student.objects.all()
        return render(request, "list_students.html", {'students': students})

def create_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        student=Student(name,age,email)
        Student.objects.create(name=name, age=age, email=email)
        return render(request, "create_student.html")
        pass
    elif request.method =="GET" :
       return render(request, "create_student.html")


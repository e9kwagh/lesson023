from django.shortcuts import render,redirect
from .models import Teacher ,Student
# Create your views here.

def home(request):
  return render(request,"base/home.html")

def career(request):
  return render(request,"base/career.html")

def curriculum(request):
  return render(request,"base/curriculum.html")

def trainer(request):
 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gamertag = request.POST.get('gamertag')
        rank = request.POST.get('rank')
        dob = request.POST.get('dob')

        trainer_instance = Teacher(
            name=name,
            email=email,
            gameid=gamertag,
            platform=rank,
            dob=dob
        )

        trainer_instance.save()

      
        return redirect('career')

    return render(request, "base/trainer.html")


def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gamertag = request.POST.get('gamertag')
        rank = request.POST.get('rank')
        dob = request.POST.get('dob')


        student_instance = Student(
            name=name,
            email=email,
            gameid=gamertag,
            platform=rank,
            dob=dob
        )

        student_instance.save()

        return redirect('curriculum')

    return render(request, "base/student.html")

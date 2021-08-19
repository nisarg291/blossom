from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    students=Student.objects.all();
    return render(request,"blossom.html",{'students':students})

def BlossomEducation(request):
    return render(request,"blossomEducation.html")


def BlossomImmigration(request):
    return render(request,"blossomEducation.html")


def BlossomCoaching(request):
    return render(request,"blossomCoaching.html")

def BlossomPersonalCoaching(request):
    return render(request,"blossomPersonalCoaching.html")


def Spoken(request):
    return render(request,"spoken.html")

def Ielts(request):
    return render(request,"ielts.html")

def Personality(request):
    return render(request,"personality.html")

def Courses(request):
    return render(request,"courses.html")

def AboutUs(request):
    return render(request,"aboutus.html")

def Contact(request):
    return render(request,"contact.html")

def UpCommingEvents(request):
    return render(request,"upcommingevents.html")

def Gallary(request):
    return render(request,"gallary.html")

def Canada(request):
    return render(request,"studyInCanada.html")

def USA(request):
    return render(request,"studyInUSA.html")

def UK(request):
    return render(request,"studyInUK.html")

def Poland(request):
    return render(request,"studyInPoland.html")

def Germany(request):
    return render(request,"studyInGermany.html")

def Australia(request):
    return render(request,"studyInAustralia.html")

def NewZealand(request):
    return render(request,"studyInNewZealand.html")

from django.shortcuts import render
from django.http import HttpResponse
from .models import Index2
# Create your views here.

def index(request):
    return render(request, 'job/index.html')


def about(request):
    return render(request, 'job/cont.html')


def search(request):
    return HttpResponse("we are at search")

def enter(request):
    return render(request, 'job/enterp.html')

def work(request):
    return render(request, 'job/job.html')

def mba(request):
    return render(request, 'job/cat.html')

def mtech(request):
    return render(request, 'job/GATE.html')

def gre(request):
    return render(request, 'job/gre.html')

def upsc(request):
    return render(request, 'job/upsc.html')

def inter(request):
    return render(request, 'job/interns.html')


def index2(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        index2 = Index2(name=name, email=email, phone=phone, desc=desc)
        index2.save()
    return render(request, "job/cont.html")



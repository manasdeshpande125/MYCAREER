from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('''<h1>Hello</h1>
    <a href="/job">Shop</a>
    <a href="/blog">blog</a>
    <a href="https://docs.google.com/forms/d/1n0efDXJm4618evf5gpksCiT0kXC8lf-bMSc72Xm3f3c/edit">bl</a>''')

def hhom(request):
    return render(request,'job/index.html')






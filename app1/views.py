from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
def lahari(request):
    return HttpResponse("<marquee><h1>hi lahari</marquee></h1>")
def add(request):
    return HttpResponse("<marquee><h1>add the link</marquee></h1>")
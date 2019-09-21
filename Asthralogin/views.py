from django.shortcuts import render
from django.http import HttpResponse
from .models import Event




def home(request):
    context = {
        'Events': Event.objects.all()
    }
    return render(request, 'Asthralogin/home.html',context)

def about(request):
   
    return render(request, 'Asthralogin/about.html',{'title': 'Volunteer'})
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'Bhumika': 'Django developer'}
    return render(request,'home.html',context)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tester(request):
    return render(request, "testy.html/")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('Hello there friend!!!')
    return render(request, 'generator/home.html', {'password': 'asdfasd223asdfas'})

def eggs(request):
    return HttpResponse('Eggs are Awesome!!!')
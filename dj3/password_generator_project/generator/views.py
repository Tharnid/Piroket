from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse('Hello there friend!!!')
    return render(request, 'generator/home.html', {'password': 'asdfasd223asdfas'})

def password(request):
    
    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = 10

    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})
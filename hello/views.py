import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('''
    <h1 style="color:green; font-family: Arial, sans-serif;">
        Hi, it is a first change to this project and I hope it works!
    </h1>
    ''')


def fancy_index(request):
    return render(request, "hello/index.html")


def hello_name(request, name):
    data = {
        'name': name.capitalize(),
        'time': datetime.datetime.now(),
        'show_time': True
    }
    return render(request, "hello/greet.html", data)

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from .models import Question
from django.template import loader

# Create your views here.

def stopItr(name):
    raise StopIteration

def home(request = HttpRequest):
    flag_middleware = ''
    # print([ value for middleware in settings.MIDDLEWARE for value in middleware.split('.')])
    for middleware in settings.MIDDLEWARE:
        middlewareNames = middleware.split('.')
        for name in middlewareNames:
            if name == 'AuthenticationMiddleware':
                flag_middleware = middleware
                break
    return HttpResponse("<h2>Vote Home page - %s </h2" % flag_middleware)

def about(request = HttpRequest):
    id = 6
    context = {
        "id": id
    }
    return render(request, 'blog/about.html', context)

def results(request = HttpRequest, question_id = None):
    question = ['Who is working?', 'How do you do?', 'What is use case?']
    context = {
        "heading": "Select Question",
        "question_list": question
    }
    return render(request, 'blog/results.html', context)

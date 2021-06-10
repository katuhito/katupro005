from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'This is sample pages',
        'goto':'next',
    }
    return render(request, 'katuapp005/index.html', params)

def next(request):
    params = {
        'title':'Hello/Index',
        'msg':'This is sample pages',
        'goto':'index'
    }
    return render(request, 'katuapp005/index.html', params)
    



from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict={'boldmessage':"I am bold font from the context"}
    return render(request,'rango/index.html',context_dict)

def about(request):
    context_dict={'boldmessage':"Cool treehouse, dude!"}
    return render(request,'rango/about.html',context_dict)
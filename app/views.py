from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    EFMO=TopicForm()
    d={ 'EFMO':EFMO }
    if request.method=='POST':
        DTFO=TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('Topic is created')


    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('Webpage is Created')
    return render(request,'insert_webpage.html',d)


    

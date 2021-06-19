# tasks/views.py
from django.forms.widgets import CheckboxInput
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def update(request,pk):
    item = Task.objects.get(id = pk)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if form.checked:
                item.complete = True
            form.save()
        return redirect('/')
    
    
    return render(request, 'tasks/update.html',{'todo': item})
from django.shortcuts import render, redirect
from .forms import TaskNameForm, TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Task


def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': sorted(Task.objects.all()),
        'msg': messages
    })

def delete(request):
    if request.method == "POST":
        f = TaskNameForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            d = Task.objects.get(title=task)
            if d is not None:
                d.delete()
                messages.success(request, f'Task {task} added.')
            else:
                messages.error(request, f'This task does not exist')
                return redirect('tasks:index')
        else:
            return render(request, 'tasks/delete.html', {"form": f})
    else:
        return render(request, "tasks/delete.html", {"form": TaskNameForm()})


def add(request):
    if request.method == "POST":
        f = TaskForm(request.POST)
        if f.is_valid():
            f.save()
            #task = f.cleaned_data["task"]
            #priority = f.cleaned_data["priority"]
            #t = Task(title=task, priority=priority)
            #t.save()
            messages.success(request, f'Task {f.cleaned_data("title")} added.')
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": TaskForm()})
    
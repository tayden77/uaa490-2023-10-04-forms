from django.shortcuts import render, redirect
from .forms import NewTaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


tasks = ['eat', 'sleep', 'pray'
]

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': sorted(tasks),
        'msg': messages
    })


def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            if task not in tasks:
                tasks.append(task)
                messages.success(request, f'Task {task} added.')
                return redirect('tasks:index')
            else:
                messages.error(request, f'Duplicate tasks are not allowed')
                return redirect('tasks:index')

        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def delete(request):
    if request.method == "DELETE":
        f = NewTaskForm(request.DELETE)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            if task in tasks:
                tasks.remove(task)
                messages.success(request, f'Task {task} removed.')
                return redirect('tasks:index')
            else:
                messages.error(request, f'This task does not exist')
                return redirect('tasks:index')

        else:
            return render(request, 'tasks/delete.html', {"form": f})
    else:
        return render(request, "tasks/delete.html", {"form": NewTaskForm()})

from django.shortcuts import render, redirect
from .forms import NewTaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = ['eat', 'sleep', 'pray'
]

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def add(request):
    return render(request, "tasks/add.html")

def add(request):
    return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        task = request.POST["task"]
        priority = request.POST["priority"]
        tasks.append(task)
        #return HttpResponseRedirect(reverse('tasks:index'))
        return redirect('tasks:index')
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = request.POST["task"]
            priority = request.POST["priority"]
            tasks.append(task)
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})


def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            tasks.append(task)
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            if task not in tasks:
                tasks.append(task)
                return redirect('tasks:index')
            else:
                return render(request, 'tasks/add.html', {
                    "form": f,
                    "errormessage": "Duplicate task not allowed"
                })
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})


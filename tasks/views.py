from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .form import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user).order_by("created_at")  # make sure can only see their own tasks
    return render(request, "tasks/task_list.html",{
        "tasks" : tasks
    })

@login_required
def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # connect task with present request user
            task.save()

            return HttpResponseRedirect(reverse("tasks:task_list"))
    
    else:
        form = TaskForm()
    
    return render(request, "tasks/add.html",{
        "form" : form
    })
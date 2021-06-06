from django.shortcuts import render, redirect
from app import models
from app import forms


def task(request):
    task_list = models.Tasks.objects.order_by('task_id')
    return render(request,'app/index.html', {'tasks': task_list})

def edit_task(request, pk):
    single_task = models.Tasks.objects.get(task_id= pk)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance= single_task)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = forms.TaskForm(instance= single_task) 
    return render(request, 'app/edit_task.html', {'form':form, 'single_task': single_task})

def add_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = forms.TaskForm()
    return render(request,'app/add_task.html',{'form': form})


def delete_task(request, pk):
    delete_task =  models.Tasks.objects.get(task_id= pk)
    if request.method=='POST':
        delete_task.delete()
        return redirect('task')
    return render(request, 'app/delete_task.html', {'delete_task':delete_task})
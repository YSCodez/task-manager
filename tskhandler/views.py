from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskAllocForm
from django.contrib import messages
from .models import TaskAllocA

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskAllocForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('add-task-db')  # Redirect to the task list or another page
    else:
        form = TaskAllocForm()

    return render(request, 'index.html', {'form': form})

def viewtask(request):
    taskList = TaskAllocA.objects.filter(status=TaskAllocA.Status.PENDING)
    return render(request, 'viewtask.html', {'taskList': taskList})

def mark_as_done(request, task_id):
    task = get_object_or_404(TaskAllocA, id=task_id)
    task.status = TaskAllocA.Status.COMPLETED
    task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('view-task-db')

def mark_edit_task(request, task_id):
    task = get_object_or_404(TaskAllocA, id=task_id)

    if request.method == 'POST':
        form = TaskAllocForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task details
            messages.success(request, 'Task updated successfully!')
            return redirect('view-task-db')  # Redirect to the appropriate page
    else:
        form = TaskAllocForm(instance=task)  # Pre-fill the form with existing task data

    return render(request, 'edittask.html', {'form': form})

def edittask(request):
    taskList = TaskAllocA.objects.all()
    return render(request, 'edittask.html', {'taskList': taskList})

def taskdelete(request, task_id):
    task = get_object_or_404(TaskAllocA, id=task_id)
    task.delete()  # Corrected from event.delete() to task.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('view-task-db')  # Redirect to the appropriate page, e.g., task list

def completedtask(request):
    taskList = TaskAllocA.objects.filter(status=TaskAllocA.Status.COMPLETED)
    return render(request, 'completedtask.html', {'taskList': taskList})

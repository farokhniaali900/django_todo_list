from django.shortcuts import render , redirect , get_object_or_404
from .models import todo_objects
from .forms import TodoForm

def task_list(request):
    tasks = todo_objects.objects.all()
    return render(request , 'todo_list.html' , {'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TodoForm()
    return render(request , 'add_task.html' , {'form' : form})

def task_done(request , pk):
    todo_objects.objects.filter(pk=pk).update(done=True)
    return redirect('task_list')

def delete_task(request , pk):
    obj = get_object_or_404(todo_objects, pk=pk)
    obj.delete()
    return redirect(task_list)

def un_do_task(request , pk):
    obj = todo_objects.objects.filter(pk=pk)
    obj.update(done=False)
    return redirect('task_list')
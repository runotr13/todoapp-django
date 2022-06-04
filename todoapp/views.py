from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm
# Create your views here.

def TodoCreate(request):
    todo = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('todocreate')
    context = {
        "todo" : todo,
        "form" : form
    }
    return render(request,'todos/todo_create.html',context)


def TodoUpdate(request,id):
    todos = Todo.objects.get(pk=id)
    # item = get_object_or_404(Todo,pk=id)
    form = TodoForm(instance=todos)
    todo = Todo.objects.all

    if request.method == 'POST':
        print("EMIR ABIIIIIIIIIIIIII ",request)
        form = TodoForm(request.POST,instance=todos)
        if form.is_valid():
            form.save()
            return redirect("todocreate")
    
                
    context = {
        "form" : form,
        "todo" : todo,
    }

    return render(request,'todos/todo_create.html',context)



def TodoDelete(request,id): #* sil.
    todos = Todo.objects.get(pk=id)
    todos.delete()
    return redirect('todocreate')
    

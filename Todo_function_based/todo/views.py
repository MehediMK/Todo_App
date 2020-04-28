from django.shortcuts import render,redirect
from .models import TodoModel
from .form import TodoForm



def home(request):
    form = TodoForm()
    todoitem = TodoModel.objects.all()
    context = {
        'todo':todoitem,'form':form,
    }
    
    return render(request,'index.html',context)

def addtodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        task = TodoModel(todos=request.POST['text'])
        task.save()            
        return redirect('home')
    else:
        return redirect('home')

def todocomplete(request,id):
    todocomp = TodoModel.objects.get(id=id)
    todocomp.complete = True
    todocomp.save()
    return redirect('home')

def todoupdate(request,id):
    todocomp = TodoModel.objects.get(id=id)
    todocomp.complete = False
    todocomp.save()
    return redirect('home')

def deleteCom(request):
    TodoModel.objects.filter(complete__exact = True).delete()
    return redirect('home')

def deleteAll(request):
    TodoModel.objects.all().delete()
    return redirect('home')
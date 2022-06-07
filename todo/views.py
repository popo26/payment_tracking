import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import RepayForm, TodoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_POST
from django.urls import reverse

YEAR = datetime.datetime.now().year

def index(request):
    total = 0
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    
    for item in todo_list:
        if not item.complete:
            total += item.amount

    context = {
        'todo_list': todo_list,
        'form' : form,
        'year' : YEAR,
        'total' : total,
    }
    return render(request, 'todo/index.html', context=context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        print(request.POST)
        form.save()
    return redirect('index')


class todoUpdate(UpdateView):
    model = Todo
    fields = ['text', 'amount', 'whose_account_to_repay']
    success_url = '/'
  
    
def updateTodo(request, todo_pk):
    todo = get_object_or_404(Todo, id=todo_pk)
    if request.method == 'POST':
        form = RepayForm(request.POST)
        
        if form.is_valid():  
           
            p = request.POST['repay']
            p= float(p)
            original_p = todo.amount
            new_p = original_p - p
            todo.amount = new_p
            
            if todo.amount == 0:
                todo.complete = True
                todo.save()
            todo.save()
            form.save()
            return redirect('index')
   
    form = RepayForm()
    context = {
        'form': form,
        'todo':todo,
        'year': YEAR,
    }
    return render(request, 'todo/repay.html', context=context)


def completeTodo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
    

import datetime
import random
from .gifs import gifs
from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo
from .forms import RepayForm, TodoForm
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.core.paginator import Paginator


YEAR = datetime.datetime.now().year

def index(request):
    total = 0
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    gif = random.choice(gifs)
    paginator = Paginator(todo_list, 5) # Show 5 items per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for item in todo_list:
        if not item.complete:
            total += item.amount

    context = {
        'todo_list': todo_list,
        'form' : form,
        'year' : YEAR,
        'total' : total,
        'gif': gif,
        'page_obj': page_obj,
    }
    return render(request, 'todo/index.html', context=context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')


class todoUpdate(UpdateView):
    model = Todo
    fields = ['text', 'amount', 'whose_account_to_repay']
    success_url = '/'
  
    
def updateTodo(request, todo_pk):
    todo = get_object_or_404(Todo, id=todo_pk)
    print(todo.id)
    if request.method == 'POST':  
        form = RepayForm(request.POST)
        if form.is_valid():  
            
            p = request.POST['repay']
            p= float(p)
            original_p = todo.amount
            new_p = original_p - p
            todo.amount = new_p

            if todo.amount < 0:
                message = "Too much, Coco!"
                form = RepayForm(initial={'todo': todo})
                context = {
                    'form': form,
                    'todo':todo,
                    'year': YEAR,
                    'message': message,
                    'original_p': original_p,
                }
                return render(request, 'todo/repay.html', context=context)
           
            if todo.amount == 0:
                todo.complete = True
                todo.save()
            todo.save()
            form.save()
            
            return redirect('index')
   
    form = RepayForm(initial={'todo': todo})
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
    

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import TodoItem
from .forms import TodoForm


def index(request):
    todo_list = TodoItem.objects.order_by('id')
    form = TodoForm()

    count_item = todo_list.count() + 1

    context = {
        'todo_list':  todo_list,
        'forms': form,
        'count_item': count_item
    }
    return render(request, 'index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_item = TodoItem(item=request.POST['item'])
        new_item.save()
    return redirect('index')


@require_POST
def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect('index')

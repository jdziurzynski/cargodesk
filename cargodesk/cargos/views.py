from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment, active, closed, Todo, clear, in_progres
from .forms import FormNewLoad, TodoForm
from datetime import datetime
from django.core.paginator import  Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

import pyperclip


class UserToDoList(LoginRequiredMixin, ListView): #####NOT IN USE
    model = Todo
    template_name = 'todo_page.html'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user).filter(status=active).order_by('-create_date')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def new_load(request):
    creat_load = FormNewLoad(request.POST)
    if creat_load.is_valid():
        n_load = creat_load.save(commit=False)
        n_load.author=request.user
        n_load.save()

    return redirect('/')


@login_required
def edit_save(request, pk):
    edit_save_object = Shipment.objects.get(pk=pk)
    creat_load = FormNewLoad(request.POST, instance=edit_save_object)
    if creat_load.is_valid():
        n_load = creat_load.save()

    return redirect('/')



@login_required
def display_loads(request):
    loads = Shipment.objects.all().order_by('unload_date_to').filter(status=active)
    creat_load = FormNewLoad()
    context = {
        'loads': loads,
        'creat_load':creat_load
    }
    return render(request, 'one_desk.html', context)

@login_required
def delete_load(request, pk):
    object_to_close = Shipment.objects.get(pk=pk)
    object_to_close.status = closed
    now = datetime.now
    object_to_close.closed_date = datetime.now()
    object_to_close.author = request.user
    object_to_close.status2 = in_progres
    object_to_close.save()

    return redirect('/')

@login_required
def edit_load(request, pk):
    loads = Shipment.objects.all().order_by('unload_date_to').filter(status=active)
    editing_load = Shipment.objects.get(pk=pk)
    form = FormNewLoad(instance=editing_load)

    context={
        'creat_load': form,
        'editing_load': editing_load,
        'current_pk' : pk,
        'loads': loads,
    }

    return render(request, 'edit_load_page.html', context)

@login_required
def copy_load(request, pk):
    loads = Shipment.objects.all().order_by('unload_date_to').filter(status=active)
    copy_load = Shipment.objects.get(pk=pk)
    form = FormNewLoad(instance=copy_load)
    if form.is_valid():
        form.save()

    context={
        'copy_load': copy_load,
        'creat_load' : form,
        'loads': loads,
    }

    return render(request, 'copy_load.html', context)

@login_required
def history(request):
    loads = Shipment.objects.all().order_by('-closed_date').filter(status=closed)
    paginator = Paginator(loads, 25)
    page = request.GET.get('page')
    history_loads = paginator.get_page(page)
    context= {
        'history_loads' : history_loads,
        'loads' : loads,
    }
    return render(request, 'history_desk.html', context)

@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user).filter(status=active).order_by('create_date')
    loads = Shipment.objects.filter(author=request.user).filter(status2=in_progres).order_by('-closed_date')
    new_post = TodoForm()
    context = {
        'todos':todos,
        'new_post':new_post,
        'loads':loads,
    }

    return render(request, 'todo_page.html', context)

@login_required
def new_todo(request):
    new_post = TodoForm(request.POST)
    if new_post.is_valid():
        n_post=new_post.save(commit=False)
        n_post.author=request.user
        n_post.save()
    return redirect('/todo')

@login_required
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status=closed
    todo.save()

    return  redirect('/todo')

@login_required
def delete_from_mydesk(request, pk):
    load = Shipment.objects.get(pk=pk)
    load.status2=clear
    load.save()

    return redirect('/todo')


def copy_to_cupboard(request, pk):
    load = Shipment.objects.get(pk=pk)
    pyperclip.copy("From:  {}\nTo:  {}\nWeight: {}t.\nType: {}\nReady: {}".format(load.loading_place, load.unloading_place, load.weight, load.truck_type, load.load_date_from ))
    return redirect('/')

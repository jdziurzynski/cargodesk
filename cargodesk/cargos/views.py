from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment, active, closed
from .forms import FormNewLoad
from datetime import datetime
from django.core.paginator import  Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required
def new_load(request):
    creat_load = FormNewLoad(request.POST)
    if creat_load.is_valid():
        n_load = creat_load.save()

    context={
        'creat_load': creat_load,
    }
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
    object_to_close.save()

    return redirect('/')

@login_required
def edit_load(request, pk):
    editing_load = Shipment.objects.get(pk=pk)
    form = FormNewLoad(instance=editing_load)              #jak jest bez request.POST to podaje instancje
    if form.is_valid():                                    #jak powinno ale zapisuje jako nowy ładunek
        form.save()                                        #jak podmienic ladunki poprzez pk????????

    context={
        'form': form,
        'editing_load': editing_load,
    }

    return render(request, 'test.html', context)

@login_required
def history(request):
    loads = Shipment.objects.all().order_by('-closed_date').filter(status=closed)
    paginator = Paginator(loads, 15)
    page = request.GET.get('page')
    history_loads = paginator.get_page(page)
    context= {
        'history_loads' : history_loads,
        'loads' : loads,
    }
    return render(request, 'history_desk.html', context)

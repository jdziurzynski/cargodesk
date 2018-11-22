from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment, active, closed
from .forms import FormNewLoad
from datetime import datetime
from django.core.paginator import  Paginator



def new_load(request):
    creat_load = FormNewLoad(request.POST)
    print("before")
    if creat_load.is_valid():
        n_load = creat_load.save()

    context={
        'creat_load': creat_load,
    }
    return redirect('/cargos')



def display_loads(request):
    loads = Shipment.objects.all().order_by('unload_date_to').filter(status=active)
    creat_load = FormNewLoad()
    context = {
        'loads': loads,
        'creat_load':creat_load
    }
    return render(request, 'one_desk.html', context)


def delete_load(request, pk):
    object_to_close = Shipment.objects.get(pk=pk)
    object_to_close.status = closed
    now = datetime.now
    object_to_close.closed_date = datetime.now()
    object_to_close.save()

    return redirect('/cargos')


def history(request):
    loads = Shipment.objects.all().order_by('-closed_date').filter(status=closed)
    paginator = Paginator(loads, 2)
    page = request.GET.get('page')
    history_loads = paginator.get_page(page)
    context= {
        'history_loads' : history_loads,
        'loads' : loads,
    }
    return render(request, 'history_desk.html', context)

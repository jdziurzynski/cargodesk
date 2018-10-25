from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment
from .forms import FormNewLoad



def new_load(request):
    creat_load = FormNewLoad(request.POST)
    if creat_load.is_valid():
        n_load = creat_load.save()

    context={
        'creat_load': creat_load,
    }

    return redirect('/cargos')



def display_loads(request):
    loads = Shipment.objects.all().order_by('unload_date_to')
    creat_load = FormNewLoad()
    context = {
        'loads': loads,
        'creat_load':creat_load
    }
    return render(request, 'one_desk.html', context)


def delete_load(request, pk):
    load = get_object_or_404(Shipment, pk=pk).delete()

    return redirect('/cargos')

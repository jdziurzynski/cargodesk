from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Shipment


def display_loads(request):
    loads = Shipment.objects.all()
    context = {
        'loads':loads
    }
    return render(request, 'display_loads.html', context)


def new_load(request):
    if(request.method== 'POST'):
        loading_place = request.POST['loading_place']
        unloading_place = request.POST['unloading_place']
        weight = request.POST['weight']

        shipment = Shipment(loading_place=loading_place, unloading_place=unloading_place, weight=weight)
        shipment.save()

        return redirect('/cargos')
    else:
        return render(request, 'new_load.html')

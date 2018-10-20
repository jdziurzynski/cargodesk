from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Shipment



def new_load(request):
    if(request.method== 'POST'):
        loading_place = request.POST['loading_place']
        unloading_place = request.POST['unloading_place']
        weight = request.POST['weight']
        price = request.POST['price']
        info = request.POST['info']


        shipment = Shipment(loading_place=loading_place, unloading_place=unloading_place, weight=weight, info=info, price=price)
        shipment.save()

        return redirect('/cargos')
    else:
        return render(request, 'one_desk.html')


def display_loads(request):
    loads = Shipment.objects.all()
    context = {
        'loads':loads
    }
    return render(request, 'one_desk.html', context)

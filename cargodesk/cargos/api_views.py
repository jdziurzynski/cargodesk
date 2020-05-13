import django_filters
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import permissions, status



class ShipmentViewSet(django_filters.FilterSet):
    status = django_filters.CharFilter(method='get_by_status', field_name='status')


    def get_by_status(self, queryset, field_name, value):
        if value in ['active']:
            return queryset.filter(status='active')
        elif value in ['closed']:
            return queryset.filter(status='closed')
        else:
            return queryset.none()
        return queryset





class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
    filterset_class = ShipmentViewSet




class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

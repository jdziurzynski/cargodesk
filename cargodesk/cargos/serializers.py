from rest_framework import serializers
from . import models



class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipment
        fields= ('id',
                'loading_place',
                'unloading_place',
                'price',
                'load_date_from',
                'load_date_to',
                'unload_date_from',
                'unload_date_to',
                'currency',
                'truck_type',
                'info',
                'status',
                'status2',
                'closed_date',
                'author'
                )

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields= ('title',
                'text',
                'create_date',
                'status',
                'author',
                )

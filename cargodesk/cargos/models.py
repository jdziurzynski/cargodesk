from django.db import models
from datetime import datetime



TAUTLINER = 'Tautliner'
FRIGO = 'Frigo'
TANK = "Tank"
truck_type_choices = (
( TAUTLINER, 'Tautliner'),
( FRIGO, "Frigo"),
( TANK, 'Tank'),
)

euro = 'euro'
sek = 'sek'
pln = 'pln'
currency_choices = (
    (euro,'euro'),
    (sek,'sek'),
    (pln, 'pln'),
)

class Shipment(models.Model):
    loading_place = models.CharField(max_length=70)
    unloading_place = models.CharField(max_length=70)
    weight = models.IntegerField(default=24)
    price = models.IntegerField(null=False)

    load_date_from = models.DateField(default=datetime.now)
    load_date_to = models.DateField(default=datetime.now)
    unload_date_from = models.DateField(default=datetime.now)
    unload_date_to = models.DateField(default=datetime.now)

    currency = models.CharField(max_length=10, choices=currency_choices, default=euro)
    truck_type = models.CharField(max_length=10, choices=truck_type_choices, default=TAUTLINER)
    info = models.TextField(max_length=100, default='')


    def title(self):
        ship_title = loading_place
        return ship_title

    def  __str__(self):
        return self.loading_place

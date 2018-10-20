from django.db import models


class Shipment(models.Model):
    loading_place = models.CharField(max_length=70)
    unloading_place = models.CharField(max_length=70)
    weight = models.IntegerField(default=24)
    price = models.IntegerField(default=1)

    def title(self):
        ship_title = loading_place
        return ship_title


    TAUTLINER = 'TR'
    FRIGO = 'FO'
    TANK = "TK"
    truck_type_choices = (
    ( TAUTLINER, 'Tautliner'),
    ( FRIGO, "Frigo"),
    ( TANK, 'Tank'),
    )

    truck_type = models.CharField(max_length=3, choices=truck_type_choices, default=TAUTLINER)

    info = models.TextField(max_length=100, default='')

    def  __str__(self):
        return self.loading_place

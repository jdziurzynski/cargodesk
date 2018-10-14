from django.db import models


class Shipment(models.Model):
    loading_place = models.CharField(max_length=100)
    unloading_place = models.CharField(max_length=100)
    weight = models.IntegerField(default=24)

    '''def title(self):
        ship_title =
        return ship_title

    FRIGO = 'FRIGO'
    TAUTLINER = 'TAUT'
    TANK = "TANK"
    truck_type_choices = (
    ( TAUTLINER, 'Tautliner'),
    ( FRIGO, "Frigo"),
    ( TANK, 'Tank'),
    )

    truck_type = models.CharField(max_length=10, choices=truck_type_choices, default=TAUTLINER)'''
    info = models.TextField(max_length=100, null=True, default= '<not required>')

    def  __str__(self):
        return self.loading_place

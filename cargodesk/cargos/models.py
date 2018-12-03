from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




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
active = 'active'
closed = 'closed'
status_choices = (
    (active, 'active'),
    (closed, 'closed'),
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
    status = models.CharField(max_length=10,  choices=status_choices, default=active)

    closed_date = models.DateTimeField(default=datetime.now)

    @property
    def date_close(self):
        date_difference = datetime.now().date() - self.unload_date_to
        if date_difference.days >= -1:
            return True
        else:
            return False

    def title(self):
        ship_title = loading_place
        return ship_title

    def  __str__(self):
        return self.loading_place

class Todo(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=100)
    create_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10,  choices=status_choices, default=active)

    def  __str__(self):
        return self.title

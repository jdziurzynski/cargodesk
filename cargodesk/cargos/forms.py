from django import forms
from .models import Shipment, Todo
from django.forms import ModelForm, Textarea, DateInput, SelectDateWidget, DateField
from django.contrib.admin import widgets





TAUTLINER = 'TR'
FRIGO = 'FO'
TANK = "TK"
truck_type_choices = (
( TAUTLINER, 'Tautliner'),
( FRIGO, "Frigo"),
( TANK, 'Tank'),
)

class FormNewLoad(ModelForm):
    class Meta:
        model = Shipment
        #fields =  '__all__'  #'['loading_place', 'unloading_place', 'weight', 'price', 'info', 'truck_type', 'currency', 'date']'
        exclude = ("date_close", "status", "closed_date", 'author', "status2")
        widgets={
            'info': Textarea(attrs={'cols':20, 'rows': 3, 'style':'resize:none;'}),
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['weight'].widget.attrs.update({ 'class': 'weight_class' })
        self.fields['loading_place'].widget.attrs.update({ 'class': 'loading_place' })
        self.fields['unloading_place'].widget.attrs.update({ 'class': 'unloading_place' })
        self.fields['price'].widget.attrs.update({ 'class': 'price' })
        self.fields['truck_type'].widget.attrs.update({ 'class': 'truck_type' })
        self.fields['currency'].widget.attrs.update({ 'class': 'currency' })
        self.fields['load_date_from'].widget.attrs.update({  'class':'date' })
        self.fields['load_date_to'].widget.attrs.update({  'class':'date' })
        self.fields['unload_date_from'].widget.attrs.update({  'class':'date' })
        self.fields['unload_date_to'].widget.attrs.update({  'class':'date' })
        #self.fields['date'].widget = widgets.AdminDateWidget()
        self.fields['info'].required = False

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('create_date', 'status', 'author')
        widgets={
            'text': Textarea(attrs={'cols':40, 'rows': 3, 'style':'resize:none;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({ 'class': 'todo_title' })
        self.fields['text'].widget.attrs.update({ 'class': 'todo_info' })

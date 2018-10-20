from django import forms

class NewLoad(forms.Form):
    loading_place = forms.CharField(label='Loading place', max_length=50)

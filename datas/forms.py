from django import forms

from .models import Data

class DataForm(forms.Form):
    data = forms.DateField()

class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["data"]
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control date'})
        }
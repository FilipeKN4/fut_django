from django import forms

from .models import Data

class DataForm(forms.Form):
    data = forms.DateField()

class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["data_string"]
        widgets = {
            'data_string': forms.TextInput(attrs={'class': 'form-control date'})
        }
    
    def clean(self):
        pass
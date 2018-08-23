from django import forms

from .models import Data

class DataForm(forms.Form):
    data = forms.CharField()

class DataModelForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["data"]
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control date'})
        }
    
    def clean(self):
        pass
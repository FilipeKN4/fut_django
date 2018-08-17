from django import forms

from liga.models import Time

class TimeForm(forms.Form):
    nome = forms.CharField()
    #cidade = forms.CharField()
    sigla_estado = forms.CharField()
    #numero_de_torcedores = forms.IntegerField()
    #numero_de_titulos = forms.IntegerField()

class TimeModelForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ["nome", "sigla_estado"]

    def clean_sigla_estado(self):
        sigla_estado = self.cleaned_data.get("sigla_estado")
        if len(sigla_estado) > 2:
            raise forms.ValidationError("Cara, somente siglas de estados! Vlw")
        return sigla_estado

class UserLoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)

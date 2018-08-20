from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    nome_usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        nome_usuario = self.cleaned_data.get("nome_usuario")
        senha = self.cleaned_data.get("senha")
        
        if nome_usuario and senha:
            usuario = authenticate(username=nome_usuario, password=senha)
            if not usuario:
                raise forms.ValidationError("Este usuario nao existe")
            if not usuario.check_password(senha):
                raise forms.ValidationError("Senha incorreta")
            if not usuario.is_active:
                raise forms.ValidationError("Usuario inativo")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        campos = {
            'nome_usuario',
            'email',
            'senha'
        }
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
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'senha',
            'confirmar_senha',
            'email'
        ]

    def clean_confirmar_senha(self):
        print(self.cleaned_data)
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        print(confirmar_senha)
        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas diferentes')
        
        return senha
from django.core.validators import RegexValidator
from users.models import CustomUser
from django import forms
import re

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", required=True, error_messages={'invalid': 'E-mail invalido'})
    password = forms.CharField(widget=forms.PasswordInput, label="Senha", required=False)


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}),
        label="Senha",
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}),
        label="Confirmar Senha",
        required=False
    )
    
    first_name = forms.CharField(
        label="Nome",
        validators=[RegexValidator(r'^[A-Za-zÀ-ÿ\s]+$', "O nome deve conter apenas letras.")],
        required=False
    )
    email = forms.EmailField(
        label="E-mail",
        error_messages={'invalid': 'E-mail invalido'},
        required=False
    )



    class Meta:
        model = CustomUser
        fields = ["first_name", "email", "password1", "password2"]
        labels = {
            "first_name": "Nome",
            "email": "E-mail",
        }



    def clean_first_name(self):
        name = self.cleaned_data.get("first_name")
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', name):
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return name


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado. Tente outro")
        return email


    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("A senha deve conter pelo menos um número.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("A senha deve conter pelo menos um caractere especial.")
        return password


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if not password2:
            self.add_error('password2', "O campo confirmar senha é obrigatório.")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "As senhas não coincidem.")
        
        email = cleaned_data.get('email')
        if email:
            cleaned_data['username'] = email
        
        return cleaned_data

from django import forms


class RegistroForm(forms.Form):

    nome = forms.CharField(required=False)
    email = forms.CharField(required=False)
    telefone = forms.CharField(required=False)

    marca_vender = forms.CharField(required=False)
    modelo_vender = forms.CharField(required=False)
    ano_vender = forms.CharField(required=False)
    valor_vender = forms.CharField(required=False)

    marca_comprar = forms.CharField(required=False)
    modelo_comprar = forms.CharField(required=False)
    ano_comprar = forms.CharField(required=False)
    valor_comprar = forms.CharField(required=False)



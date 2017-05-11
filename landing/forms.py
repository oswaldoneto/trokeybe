from django import forms


class RegistroForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.CharField(required=False)
    telefone = forms.CharField(required=True)
    marca_vender = forms.CharField(required=False)
    modelo_vender = forms.CharField(required=False)
    ano_vender = forms.CharField(required=False)
    valor_vender = forms.CharField(required=False)
    marca_comprar = forms.CharField(required=False)
    modelo_comprar = forms.CharField(required=False)
    ano_comprar = forms.CharField(required=False)
    valor_comprar = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(RegistroForm, self).clean()

        marca_vender = cleaned_data.get('marca_vender')
        modelo_vender = cleaned_data.get('modelo_vender')
        ano_vender = cleaned_data.get('ano_vender')
        valor_vender = cleaned_data.get('valor_vender')

        if len(marca_vender) > 0 or len(modelo_vender) > 0 or len(ano_vender) > 0 or len(valor_vender) > 0:
            bloco_vender_valido = len(marca_vender) > 0 and len(modelo_vender) > 0 and len(ano_vender) > 0 and len(
                valor_vender) > 0
            if not bloco_vender_valido:
                raise forms.ValidationError('Preencha os dados do seu carro ou deixe os campos em branco.')

        marca_comprar = cleaned_data.get('marca_comprar')
        modelo_comprar = cleaned_data.get('modelo_comprar')
        ano_comprar = cleaned_data.get('ano_comprar')
        valor_comprar = cleaned_data.get('valor_comprar')

        if len(marca_comprar) > 0 or len(modelo_comprar) > 0 or len(ano_comprar) > 0 or len(valor_comprar) > 0:
            bloco_comprar_valido = len(marca_comprar) > 0 and len(modelo_comprar) > 0 and len(ano_comprar) > 0 and len(
                valor_comprar) > 0
            if not bloco_comprar_valido:
                raise forms.ValidationError('Preencha os dados do carro que deseja ou deixe os campos em branco.')

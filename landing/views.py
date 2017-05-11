from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from landing.forms import RegistroForm
from landing.models import Registro, Anuncio


class IndexView(TemplateView):
    template_name = 'index.html'


class RegistroView(FormView):
    template_name = 'register.html'
    form_class = RegistroForm
    success_url = '/landing/index?register=success'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']

        marca_vender = form.cleaned_data['marca_vender']
        modelo_vender = form.cleaned_data['modelo_vender']
        ano_vender = form.cleaned_data['ano_vender']
        valor_vender = form.cleaned_data['valor_vender']

        marca_comprar = form.cleaned_data['marca_comprar']
        modelo_comprar = form.cleaned_data['modelo_comprar']
        ano_comprar = form.cleaned_data['ano_comprar']
        valor_comprar = form.cleaned_data['valor_comprar']

        registro = Registro.objects.create(nome=nome, email=email, telefone=telefone)

        venda = Anuncio.objects.create(marca=marca_vender, modelo=modelo_vender, ano=ano_vender, valor=valor_vender,
                                       tipo=Anuncio.VENDER, registro=registro)

        compra = Anuncio.objects.create(marca=marca_comprar, modelo=modelo_comprar, ano=ano_comprar,
                                        valor=valor_comprar, tipo=Anuncio.COMPRAR, registro=registro)

        return super(RegistroView, self).form_valid(form)

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from landing import forms
from landing.forms import RegistroForm
from landing.mailing import send_welcome
from landing.models import Registro, Anuncio


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'registered': self.request.GET['registered'] if 'registered' in self.request.GET else 'false'})
        return context



class RegistroView(FormView):
    template_name = 'register.html'
    form_class = RegistroForm
    success_url = '/?registered=true'

    def form_valid(self, form):

        cleaned_data = super(RegistroView, self).form_valid(form)


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

        Anuncio.objects.create(marca=marca_vender, modelo=modelo_vender, ano=ano_vender, valor=valor_vender,
                                       tipo=Anuncio.VENDER, registro=registro)

        Anuncio.objects.create(marca=marca_comprar, modelo=modelo_comprar, ano=ano_comprar,
                                        valor=valor_comprar, tipo=Anuncio.COMPRAR, registro=registro)

        send_welcome(email, nome)

        return cleaned_data



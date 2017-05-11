from django.db import models


class Registro(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150)
    email = models.EmailField()


class Anuncio(models.Model):
    VENDER = 'V'
    COMPRAR = 'C'
    TIPO = (
        (VENDER, 'VENDER'),
        (COMPRAR, 'COMPRAR'),
    )
    registro = models.ForeignKey(Registro)
    tipo = models.CharField(max_length=1, choices=TIPO)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    valor = models.CharField(max_length=100)








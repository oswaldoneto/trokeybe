from django.contrib import admin

from landing.models import Registro, Anuncio


class VendoAdmin(admin.TabularInline):
    model = Anuncio


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email',)
    inlines = [VendoAdmin, ]


admin.site.register(Registro, RegistroAdmin)

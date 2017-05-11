from django.contrib import admin
from landing.models import Registro, Anuncio


class VendoAdmin(admin.TabularInline):
    model = Anuncio


class RegistroAdmin(admin.ModelAdmin):
    inlines = [VendoAdmin,]


admin.site.register(Registro, RegistroAdmin)

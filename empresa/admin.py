from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas, Nicho_mercado
# Register your models here.

admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)
admin.site.register(Nicho_mercado)
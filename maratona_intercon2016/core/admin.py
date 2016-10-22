from django.contrib import admin
from .models import Bairro, Eleitor, Voto


@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    search_fields = ('bairro',)


admin.site.register(Eleitor)
admin.site.register(Voto)

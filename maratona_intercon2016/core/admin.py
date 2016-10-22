from django.contrib import admin
from .models import Bairro, Eleitor, Voto


admin.site.register(Bairro)
admin.site.register(Eleitor)
admin.site.register(Voto)

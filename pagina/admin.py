from django.contrib import admin

from .models import filme
from .models import projeto
from .models import Categoria

class projetoAdmin(admin.ModelAdmin):
    list_display = ('nome', "ano", "categoria")
admin.site.register(Categoria)
admin.site.register(projeto, projetoAdmin)
admin.site.register(filme)

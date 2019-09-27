from django.contrib import admin
from .models import Pessoa, Autor, PessoaJuridica, PessoaFisica, Evento, ECientifico, ArtigoCientifico

admin.site.register(Pessoa)
admin.site.register(Autor)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(ECientifico)
admin.site.register(ArtigoCientifico)

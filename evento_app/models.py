from django.db import models
from django.contrib.auth.models import User

class Pessoa (models.Model):
    nome = models.CharField( max_length=128)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.nome

class Autor (models.Model):
    curriculo = models.TextField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    # artigos = models.ManyToManyField(ArtigoCientifico, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return "{} ({})".format(self.pessoa, self.curriculo)
        # ac = ''
        # for i in self.artigos.all():
        #     ac = ac + ',' + i.titulo + ','
        # return str (self.curriculo) + ac

class PessoaJuridica (Pessoa):
    cnpj = models.CharField(max_length=11, null=True, blank=True)
    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=11, null=True, blank=True)
    def __str__(self):
        return self.nome

class Evento (models.Model):
    nome = models.CharField(max_length=150)
    evento_principal = models.CharField(max_length=150)
    sigla = models.CharField(max_length=30)
    data_hora = models.DateTimeField(null = True , blank= True)
    palavra_chave = models.CharField(max_length=150)
    logo_tipo = models.CharField(max_length=150)
    realizador= models.ForeignKey(Pessoa, on_delete=models.SET_NULL, blank= True, null=True)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=18)
    endereco = models.CharField(max_length=150)
    cep = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class ECientifico(Evento):
    issn = models.CharField(max_length=13)

    def __str__(self):
        return self.nome

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=150)
    autores = models.ManyToManyField(Autor)
    evento = models.ForeignKey(ECientifico, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        a = ''
        for i in self.autores.all():
            a = a + ',' + i.nome + ','
        return str (self.titulo) + 'Autores:' + a + 'Evento:' + self.evento

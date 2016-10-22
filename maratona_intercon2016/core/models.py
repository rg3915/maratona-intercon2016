from django.db import models


class Eleitor(models.Model):
    uf = models.CharField(blank=True, null=True, max_length=2)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    cod_municipio_tse = models.IntegerField()
    zona = models.ForeignKey(
        'Bairro', verbose_name='zona_eleitor', null=True, blank=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    faixa_etaria = models.CharField(max_length=50, blank=True, null=True)
    grau_de_escolaridade = models.CharField(
        max_length=50, blank=True, null=True)
    qtd_eleitores_no_perfil = models.IntegerField()

    class Meta:
        verbose_name = 'eleitor'
        verbose_name_plural = 'eleitores'


class Voto(models.Model):
    zona = models.ForeignKey(
        'Bairro', verbose_name='zona_voto', null=True, blank=True)
    nome_candidato = models.CharField(max_length=50)
    total_votos = models.IntegerField()


class Bairro(models.Model):
    zona = models.IntegerField(unique=True)
    bairro = models.CharField(
        unique=True, max_length=50, blank=True, null=True,)

    def __str__(self):
        return self.bairro

    class Meta:
        ordering = ('bairro',)

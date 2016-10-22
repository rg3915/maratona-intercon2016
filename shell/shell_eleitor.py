import csv
from maratona_intercon2016.core.models import Eleitor, Bairro

eleitor_list = []

''' Lendo os dados de sao_paulo.csv '''
with open('maratona_intercon2016/sao_paulo.csv', 'r') as f:
    r = csv.DictReader(f, delimiter=';')
    for dct in r:
        eleitor_list.append(dct)
    f.close()


obj = [Eleitor(
    uf=i['UF'],
    municipio=i['MUNICIPIO'],
    cod_municipio_tse=i['COD_MUNICIPIO_TSE'],
    zona=Bairro.objects.get(zona=i['ZONA']),
    sexo=i['SEXO'],
    faixa_etaria=i['FAIXA_ETARIA'],
    grau_de_escolaridade=i['GRAU_DE_ESCOLARIDADE'],
    qtd_eleitores_no_perfil=i['QTD_ELEITORES_NO_PERFIL'],
) for i in eleitor_list]
Eleitor.objects.bulk_create(obj)

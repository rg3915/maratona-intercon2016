import csv
from maratona_intercon2016.core.models import Voto, Bairro

voto_list = []

''' Lendo os dados de sao_paulo.csv '''
with open('maratona_intercon2016/detalhe_votacao_candidato_municipio_zona_2016_SP.txt', 'r') as f:
    r = csv.DictReader(f, delimiter=';')
    for dct in r:
        voto_list.append(dct)
    f.close()


obj = [Voto(
    zona=Bairro.objects.get(zona=i['NUMERO_ZONA']),
    nome_candidato=i['NOME_CANDIDATO'],
    total_votos=i['TOTAL_VOTOS'],
) for i in voto_list]
Voto.objects.bulk_create(obj)

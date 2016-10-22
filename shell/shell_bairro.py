import csv

bairro_list = []

''' Lendo os dados de zona_bairro.csv '''
with open('maratona_intercon2016/zona_bairro.csv', 'r') as f:
    r = csv.DictReader(f, delimiter=';')
    for dct in r:
        bairro_list.append(dct)
    f.close()

for i in range(len(bairro_list)):
    print(bairro_list[i]['ZONA'], bairro_list[i]['BAIRRO'])


# done

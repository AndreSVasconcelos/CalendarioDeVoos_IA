# Cria estrutura com informações de origem, destino e base de dados de voos
origem = [('Lisboa', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Bruxelas', 'BRU'),
          ('Londres', 'LHR')]

destino = 'FCO'

voos = {}
for linha in open('db_data/flights.txt'):
    a, b,c, d, e =linha.strip().split(',')
    voos.setdefault((a,b),[]).append((c,d,e))

print(voos[('BRU','FCO')])
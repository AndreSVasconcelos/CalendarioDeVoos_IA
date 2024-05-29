import mlrose as ml

# Funções úteis
def fitness_function(agenda):
  id_voo = -1
  total_preco = 0
  for i in range(len(agenda) // 2):
    origem = pessoas[i][1]
    id_voo += 1
    ida = voos[(origem, destino)][agenda[id_voo]]
    total_preco += ida[2]
    id_voo += 1
    volta = voos[(destino, origem)][agenda[id_voo]]
    total_preco += volta[2]

  return total_preco

# Cria estrutura com informações de origem, destino e base de dados de voos
# Aeroporto de origem de cada pessoa
pessoas = [('Lisboa', 'LIS'),
          ('Madrid', 'MAD'),
          ('Paris', 'CDG'),
          ('Dublin', 'DUB'),
          ('Bruxelas', 'BRU'),
          ('Londres', 'LHR')]

destino = 'FCO'

voos = {}
for linha in open('db_data/flights.txt'):
    a, b,c, d, e =linha.strip().split(',')
    voos.setdefault((a,b),[])
    voos[(a,b)].append((c,d,int(e)))


# Atribuindo função de fitness ao mlrose
fitness = ml.CustomFitness(fitness_function)
problema = ml.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

# Executa algoritmo Simulated Annealing
melhor_solucao, melhor_custo = ml.genetic_alg(problema, 
                                              pop_size=500, 
                                              random_state=1,
                                              mutation_prob=0.2)
print(melhor_solucao, melhor_custo)
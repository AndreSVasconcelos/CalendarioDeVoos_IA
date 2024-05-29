# Libs
import mlrose as ml

# Funções úteis
def imprimir_produtos(lista_produtos):
    valor_total = 0
    espaco_total = 0
    for i in range(len(lista_produtos)):
        if lista_produtos[i] == 1:
            valor_total += produtos[i][2]
            espaco_total += produtos[i][1]
            print(produtos[i][0])

def fitness_function(lista_produtos):
    valor_total = 0
    espaco_total = 0
    for i in range(len(lista_produtos)):
        if lista_produtos[i] == 1:
            espaco_total += produtos[i][1]
            valor_total += produtos[i][2]
    if espaco_total > capacidade_caminhao:
        valor_total = 1
    return valor_total

# Dados
produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2199.12),
            ('TV 55"', 0.400, 4346.99),
            ('TV 50"', 0.290, 3999.90),
            ('TV 42"', 0.200, 2999.90),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

capacidade_caminhao = 3

# Representação do problema 
# lista = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
# imprimir_produtos(lista)


# Atribuindo função de fitness e detalhando problema ao mlrose
fitness = ml.CustomFitness(fitness_function)
problema = ml.DiscreteOpt(length=14, 
                          fitness_fn=fitness, 
                          maximize=True, 
                          max_val=2)

# Executa algoritmo Hill Climbing
melhor_solucao, maior_lucro = ml.hill_climb(problema)
print('Hill Climb: Melhor Solução = %s, Lucro = %s' % (melhor_solucao, maior_lucro))
print('Produtos transportados:')
print(imprimir_produtos(melhor_solucao))
print('=============================================================:')
# Executa algoritmo Simulated Annealing
melhor_solucao, maior_lucro = ml.simulated_annealing(problema,
                                                     schedule=ml.GeomDecay(init_temp=10000),
                                                     random_state=3)
print('Simulated Annealing: Melhor Solução = %s, Lucro = %s' % (melhor_solucao, maior_lucro))
print('Produtos transportados:')
print(imprimir_produtos(melhor_solucao))
print('=============================================================:')

# Executa algoritmo Genetic Algorithm
melhor_solucao, maior_lucro = ml.genetic_alg(problema,
                                             pop_size=500,
                                             random_state=1,
                                             mutation_prob=0.2)

print('Genetic Algorithm: Melhor Solução = %s, Lucro = %s' % (melhor_solucao, maior_lucro))
print('Produtos transportados:')
print(imprimir_produtos(melhor_solucao))
print('=============================================================:')
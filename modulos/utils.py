# Funções úteis

def imprimir_voos(agenda, origem, destino, voos):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = origem[i][0]
        sigla = origem[i][1]
        id_voo += 1
        ida = voos[(sigla, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, sigla)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, sigla, 
                                                    ida[0], ida[1], ida[2], 
                                                    volta[0], volta[1], volta[2]))

    print('Total: %d' % total_preco)


# Fitness Function

# def fitness_function(agenda, origem, destino, voos):
#     id_voo = -1
#     total_preco = 0
#     for i in range(len(agenda) // 2):
#         sigla = origem[i][1]
#         id_voo += 1
#         ida = voos[(sigla, destino)][agenda[id_voo]]
#         total_preco += ida[2]
#         id_voo += 1
#         volta = voos[(destino, sigla)][agenda[id_voo]]
#         total_preco += volta[2]

#     return total_preco

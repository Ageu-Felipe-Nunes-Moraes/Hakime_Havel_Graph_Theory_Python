
#Hakime Havel


# Função que verifica se é um vetor gráfico por meio dos princípios de Hakime Havel
def vetorGraficoAtualizado(vetor):
    contador = 0
    maiorValor = 0 # Vai receber o maior valor do vetor
    vetor.sort(reverse=True)

    # Aplicando todas as iterações necessárias para chegar a uma conclusão satisfatória
    if len(vetor) > vetor[0]: # Verificando se há algum vértice de grau maior que o tamanho do vetor
        print(vetor)
        for i in range(len(vetor)):
            maiorValor = vetor[0]
            del(vetor[0]) # Deleta o primeiro item do vetor
            for j in range(maiorValor):
                vetor[j] = vetor[j] - 1 # Subtrai 1 de cada posição
            print(vetor)
            vetor.sort(reverse=True)
            print(vetor)
            if vetor[0] == 0: # Verifica se a primeira posição é igual a "0"
                for k in range(len(vetor)):
                    if vetor[k] == 0: # Verfica se todas as outras posições também são iguais a "0"
                        contador += 1
                        if contador == len(vetor): # Cofere a contagem dos zeros 
                            print(f"É um vetor gráfico: [{vetor}]")
                            break
                    if vetor[k] == -1: # Verifica se há algum valor dentro do vetor igual a "-1"
                        print(f"Não é um vetor gráfico: [{vetor}]")
                        break
                break
    else:
        print("Tipo de lista inválida")

vetorGraficoAtualizado([3,2,2,2,2]) # Lista de entrada


#não gráfico
'''[6, 5, 4, 4, 4, 4, 4, 2]
[4, 3, 3, 3, 3, 3, 2]
[2, 2, 2, 2, 3, 2]
[3, 2, 2, 2, 2, 2]
[1, 1, 1, 2, 2]
[2, 2, 1, 1, 1]
[1, 0, 1, 1]
[1, 1, 1, 0]
[0, 1, 0]
[1, 0, 0]
[-1, 0]
[0, -1]
'''

'''#gráfico
[5, 4, 3, 3, 3, 3, 3, 2]
[3, 2, 2, 2, 2, 3, 2]
[3, 3, 2, 2, 2, 2, 2]
[2, 1, 1, 2, 2, 2]
[2, 2, 2, 2, 1, 1]
[1, 1, 2, 1, 1]
[2, 1, 1, 1, 1]
[0, 0, 1, 1]
[1, 1, 0, 0]
[0, 0, 0]
[0, 0, 0]
'''


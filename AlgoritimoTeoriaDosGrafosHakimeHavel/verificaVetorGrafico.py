
#Hakime Havel

def reorganizar_vetor(vetor): # Organiza a lista em ordem decrescente
    vetor.sort(reverse=True)

def mostra_vetor(vetor):
    print(vetor)
    
# Função que verifica se é um vetor gráfico por meio dos princípios de Hakime Havel
def vetor_grafico(vetor):
    contador = 0
    maior_valor = 0 # Vai receber o maior valor do vetor
    reorganizar_vetor(vetor)

    # Aplicando todas as iterações necessárias para chegar a uma conclusão satisfatória
    if len(vetor) > vetor[0]: # Verificando se há algum vértice de grau maior que o tamanho do vetor
        mostra_vetor(vetor)
        for _ in range(len(vetor)):
            maior_valor = vetor[0]
            del(vetor[0]) # Deleta o primeiro item do vetor
            for j in range(maior_valor):
                vetor[j] = vetor[j] - 1 # Subtrai 1 de cada posição
            mostra_vetor(vetor)
            reorganizar_vetor(vetor)
            mostra_vetor(vetor)
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

vetor_grafico([3,2,2,2,2]) # Lista de entrada
    

#não gráfico
#[6, 5, 4, 4, 4, 4, 4, 2]
#[4, 3, 3, 3, 3, 3, 2]
#[2, 2, 2, 2, 3, 2]
#[3, 2, 2, 2, 2, 2]
#[1, 1, 1, 2, 2]
#[2, 2, 1, 1, 1]
#[1, 0, 1, 1]
#[1, 1, 1, 0]
#[0, 1, 0]
#[1, 0, 0]
#[-1, 0]
#[0, -1]

# gráfico
#[5, 4, 3, 3, 3, 3, 3, 2]
#[3, 2, 2, 2, 2, 3, 2]
#[3, 3, 2, 2, 2, 2, 2]
#[2, 1, 1, 2, 2, 2]
#[2, 2, 2, 2, 1, 1]
#[1, 1, 2, 1, 1]
#[2, 1, 1, 1, 1]
#[0, 0, 1, 1]
#[1, 1, 0, 0]
#[0, 0, 0]
#[0, 0, 0]


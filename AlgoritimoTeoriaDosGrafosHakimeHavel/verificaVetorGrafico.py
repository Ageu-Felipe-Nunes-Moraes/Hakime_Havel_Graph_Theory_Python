
#Hakime Havel

class HakimeHavel:
    
    def __init__(self):
        self.contador = 0 # Contador para auxilixar
        self.maior_valor = 0 # Vai receber o maior valor do vetor

    def reorganizar_vetor(self, vetor): # Organiza a lista em ordem decrescente
        vetor.sort(reverse=True)

    def mostra_vetor(self, vetor): # Imprime na tela
        print(vetor)

    def subtrai_posicoes(self, vetor): # Vai subtrair 1 de cada posição
        for j in range(self.maior_valor):
            vetor[j] = vetor[j] - 1 # Subtrai 1 de cada posição

    def verifica_condicoes(self, vetor): # Verifica se é um vetor gráfico ou não
        for k in range(len(vetor)):
            if vetor[k] == 0: # Verfica se todas as outras posições também são iguais a "0"
                self.contador += 1
                if self.contador == len(vetor): # Cofere a contagem dos zeros 
                    print(f"É um vetor gráfico: [{vetor}]")
                    break
            if vetor[k] == -1: # Verifica se há algum valor dentro do vetor igual a "-1"
                print(f"Não é um vetor gráfico: [{vetor}]")
                break

        
    # Função que verifica se é um vetor gráfico por meio dos princípios de Hakime Havel
    def vetor_grafico(self, vetor):
        self.reorganizar_vetor(vetor)
        # Aplicando todas as iterações necessárias para chegar a uma conclusão satisfatória
        if len(vetor) > vetor[0]: # Verificando se há algum vértice de grau maior que o tamanho do vetor
            self.mostra_vetor(vetor)
            for _ in range(len(vetor)):
                self.maior_valor = vetor[0]
                del(vetor[0]) # Deleta o primeiro item do vetor
                self.subtrai_posicoes(vetor)
                self.mostra_vetor(vetor)
                self.reorganizar_vetor(vetor)
                self.mostra_vetor(vetor)
                if vetor[0] == 0: # Verifica se a primeira posição é igual a "0"
                    self.verifica_condicoes(vetor)
                    break
        else:
            print("Tipo de lista inválida")

hakime = HakimeHavel()
hakime.vetor_grafico([3,2,2,2,2]) # Lista de entrada
    

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


import random

lista_de_palavras_facil = ['livro', 'bacia', 'regua', 'prato','tenis', 'carro']
lista_de_palavras_moderado = ['cadeira', 'mochila', 'tesoura', 'espelho', 'relogio', 'abobora']
lista_de_palavras_dificil = ['velocidade', 'prateleira', 'biblioteca', 'prateleira', 'ventilador', 'patrimonio']

# Criar a classe de Dificuldade e a escolha do nível, randomizando com a lista escolhida
class Dificuldade:
    @staticmethod
    def escolher_dificuldade():  
        def escolher():
            while True:  
                try:  
                    escolha = int(input("Escolha o nível de dificuldade (1 = fácil, 2 = moderado, 3 = difícil): "))
                    if escolha == 1:
                        palavra_escolhida = random.choice(lista_de_palavras_facil)
                        return palavra_escolhida
                    elif escolha == 2:
                        palavra_escolhida = random.choice(lista_de_palavras_moderado)
                        return palavra_escolhida
                    elif escolha == 3:
                        palavra_escolhida = random.choice(lista_de_palavras_dificil)
                        return palavra_escolhida
                    else:
                        print("Opção inválida. Escolha novamente.")
                except ValueError: 
                    print("Por favor, digite um número válido.") 
        return escolher  
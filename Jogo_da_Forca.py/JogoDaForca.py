from GeradorDePalavra import Dificuldade

# Criador da Forca e funções para adivinhar palavras
class Forca:
    
    jogadores = []

    def __init__ (self, palavra, incremento_ponto = 0):
        self.palavra = palavra
        self.maximo_tentativas = 5 # vidas do jogador
        self.letras_corretas = []
        self.letras_erradas = []
        self.palavra_oculta = ['_' if letra.isalpha() else letra for letra in self.palavra]
        self.incremento_ponto = incremento_ponto

    def adivinhar(self, letra):
        letra = letra
        if letra in self.palavra:
            self.letras_corretas.append(letra)
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.palavra_oculta[i] = letra
                    self.incremento_ponto += 10
        else:
            self.letras_erradas.append(letra)
            self.incremento_ponto -= 5

    def mostrar_status(self):
        print('Palavra:', ' '.join(self.palavra_oculta))
        print('Tentativas restantes:', self.tentativas_restantes())
        print('Letras erradas:', ', '.join(self.letras_erradas))

    def tentativas_restantes(self):
        return self.maximo_tentativas - len(self.letras_erradas)

    def verificar_fim_jogo(self):
        if all(letra != '_' for letra in self.palavra_oculta):
            print('Parabéns, você ganhou!')
            print(f'A palavra era {self.palavra}')
            print(f'Você conseguiu a pontuação: {self.incremento_ponto}')
            return True
        elif self.tentativas_restantes() <= 0:
            print(f'Game over! A palavra era: {self.palavra}')
            print(f'Você conseguiu a pontuação: {self.incremento_ponto}')
            return True
        return False
    
    @staticmethod
    def novo_jogo():
        escolha = Dificuldade.escolher_dificuldade()
        palavra_escolhida = escolha()
        jogo = Forca(palavra_escolhida)
        print(palavra_escolhida)
        while not jogo.verificar_fim_jogo():
            jogo.mostrar_status()
            letra = input('Digite uma letra: ')
            jogo.adivinhar(letra)
        return jogo.get_incremento_ponto()    

    def get_incremento_ponto(self):
        return self.incremento_ponto

    def set_incremento_ponto(self, valor):
        self.incremento_ponto = valor
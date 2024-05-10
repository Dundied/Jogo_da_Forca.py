from JogoDaForca import Forca

# cadastro e apresentação do jogador
class Jogador:
    codigo_jogador_inicial = 0

    def __init__(self, nome_jogador = '', codigo_jogador = 0):
        self.nome_jogador = nome_jogador
        if codigo_jogador == 0:
            Jogador.codigo_jogador_inicial += 1
            self.codigo_jogador = Jogador.codigo_jogador_inicial
        else:
            self.codigo_jogador = codigo_jogador

    def input_jogador(self):
        self.nome_jogador = input('Entre com o nome: ')

    def __str__(self):
        aux = "Jogador \n********\n"
        aux += f'Nome do jogador.........: {self.nome_jogador}\n'
        aux += f'Codigo do jogador.......: {self.codigo_jogador}\n'
        aux += f'Pontuação...............: {Forca.get_incremento_ponto}\n'
        return aux
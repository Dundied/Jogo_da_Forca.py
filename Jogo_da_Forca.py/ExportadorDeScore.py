from CadastroJogador import Jogador
from JogoDaForca import Forca

# Exportador e leitor de pontuação do jogador (savegame)
class GerenciadorDePontuacao:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def salvar_score(self):
        jogo = Forca('')
        jogadores = jogo.jogadores 
        jogadores_ordenados = sorted(jogadores, key=lambda jogador: jogador.pontuacao, reverse=True)

        with open(self.arquivo, 'w') as file:
            for jogador in jogadores_ordenados:
                file.write(f"{jogador.nome_jogador}: {jogador.pontuacao} pontos\n")

    def mostrar_scores(self):
        with open(self.arquivo, 'r') as file:
            scores = file.readlines()
            for score in scores:
                print(score.strip())  # strip para remover espaços em branco e quebras de linha
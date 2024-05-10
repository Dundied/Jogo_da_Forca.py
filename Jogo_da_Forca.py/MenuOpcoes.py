import os
from CadastroJogador import Jogador
from GeradorDePalavra import Dificuldade
from JogoDaForca import Forca
from ExportadorDeScore import GerenciadorDePontuacao

# Menu de opções da tela inicial
def exibir_nome_programa():
    print("""
░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ███████╗░█████╗░██████╗░░█████╗░░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║  █████╗░░██║░░██║██████╔╝██║░░╚═╝███████║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\n""")

def exibir_opcoes():
    print('1. Novo jogo')
    print('2. Mostrar pontuações')
    print('3. Sair\n')

def escolher_opcoes():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            # print('Novo jogo')
            novo_jogo()
        elif opcao_escolhida == 2:
            # print('Mostrar pontuações')
            mostrar_pontuacao()
        elif opcao_escolhida == 3:
            sair_do_jogo()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def novo_jogo():
    os.system('cls')
    num_jogadores = int(input("Digite a quantidade de jogadores: "))
    jogadores = []
    for i in range(num_jogadores):
        jogador = Jogador()
        jogador.input_jogador()
        jogadores.append(jogador)

    for jogador in jogadores:
        escolha = Dificuldade.escolher_dificuldade()
        palavra_escolhida = escolha()
        jogo = Forca(palavra_escolhida)
        print(f'\n\nJogador: {jogador.nome_jogador}')
        while not jogo.verificar_fim_jogo():
            jogo.mostrar_status()
            letra = input('Digite uma letra: ')
            jogo.adivinhar(letra)
        jogador.pontuacao = jogo.get_incremento_ponto()
        print(f'\nPontuação de {jogador.nome_jogador}: {jogador.pontuacao}')
    Forca.jogadores = jogadores

    exportador = GerenciadorDePontuacao('pontuacoes.txt')
    exportador.salvar_score()    
    voltar_ao_menu_principal()

def mostrar_pontuacao():
    print("\n\n|-----RANKING DE PONTUAÇÕES-----|")
    mostrar = GerenciadorDePontuacao('pontuacoes.txt')
    mostrar.mostrar_scores()  
    voltar_ao_menu_principal() 

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_subtitulo('Encerrado o app')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    exibir_opcoes()
    escolher_opcoes()

def sair_do_jogo():
    finalizar_app()
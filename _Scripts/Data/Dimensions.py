import pygame

Xis = pygame.image.load('_Imagens/X.png')  # carrega a imagem para X.
Ball = pygame.image.load('_Imagens/O.png')  # carrega a imagem para O.
Reload = pygame.image.load('_Imagens/reiniciar.png')  # carrega a imagem para o botão de jogar novamente

Symbol_X = list()  # lista de jogadas de X.
Symbol_O = list()  # lista de jogadas de O.

WIN = list()  # lista de condições de vitória.

(width, height) = [400, 400]  # dimeções da janela de jogo.
(w_home, h_home) = [200, 200]  # dimeções complementares para alguns calculos.

dimensions = [(width / 3), width / (3 / 2), width]  # dimeções para desenhar a grade.
dimensions_win = [int(w_home * 2), int(h_home * 2)]  # dimenções da janela de vitória.
dimensions_home_screen = [int(w_home * 2), int(h_home * (5 / 3))]  # dimenções da janela inicial.
dimensions_pos = width * 0.3  # valor complementar para alguns calculos.
dimensions_render = [int(width * 0.27), int(height * 0.27)]  # dimensões para colocar simbolos em tela.

Color_White = (255, 255, 255)  # codificação da cor branca.
Color_Black = (0, 0, 0)  # codificação da cor preta.

lista_temporaria = list()  # lista temporária para armazenamento das combinações  para vitória.
lista_temporaria_reverse = list()  # lista temporária

for i in dimensions:  # calcula as vitórias na vertical e horizontal.
    for j in dimensions:
        pos = [i - dimensions_pos, j - dimensions_pos]  # calcula as posições de vitória horizontais.
        pos_reverse = [j - dimensions_pos, i - dimensions_pos]  # calcula as posições de vitória verticais.
        lista_temporaria.append(pos)  # atribui a posição a uma lista temporária.
        lista_temporaria_reverse.append(pos_reverse)  # atribui a posição a uma lista temporária.

        if len(lista_temporaria) == 3:  # atribui uma das compinações completas à lista de vitórias.
            WIN.append(lista_temporaria_reverse[:])
            WIN.append(lista_temporaria[:])

    lista_temporaria.clear()  # limpa a lista temporária.
    lista_temporaria_reverse.clear()  # limpa a lista temporária.

cont = 2  # inicializa o contador.
for i in dimensions:  # loop que calcula as vitórias nas diagonais.
    pos = [i - dimensions_pos, i - dimensions_pos]
    lista_temporaria.append(pos)
    pos = [i - (width * 0.3), dimensions[cont] - (width * 0.3)]
    lista_temporaria_reverse.append(pos)
    cont -= 1

WIN.append(lista_temporaria[:])  # atribui uma combinação de vitória da diagonal à lista de combinações.
WIN.append(lista_temporaria_reverse[:])  # atribui uma combinação de vitória da diagonal à lista de combinações.
del lista_temporaria_reverse  # deleta uma lista temporária.
del lista_temporaria  # deleta uma lista temporária.

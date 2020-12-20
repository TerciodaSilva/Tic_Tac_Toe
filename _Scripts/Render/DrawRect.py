import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import pygame


def Draw_Rect(s):
    """
    Função desenha os quadros em tela, quais formam a grade do jogo.
    :param s:
    :return:
    """

    for i in DIM.dimensions:  # verifica a posição do y.
        for j in DIM.dimensions:  # verifica a posição de x.
            pygame.draw.rect(s, DIM.Color_Black, (0, 0, j, i), 6)  # desenha a grade em tela.

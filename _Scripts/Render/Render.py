import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import pygame


def Render(s):  # função para renderizar os simbolos marcados em tela.
    """
    Essa função mantém as jogadas realizadas anteriormente em tela.
    :param s:
    :return:
    """

    for i in DIM.Symbol_X:  # verifica todas as posições de X.
        imgX = pygame.transform.smoothscale(DIM.Xis,
                                            DIM.dimensions_render)  # dimensiona a imagem do simbolo.
        s.blit(imgX, i)  # marca os simbolos em tela.

    for i in DIM.Symbol_O:  # verifica todas as posições de X.
        imgO = pygame.transform.smoothscale(DIM.Ball,
                                            DIM.dimensions_render)  # dimensiona a imagem do simbolo.
        s.blit(imgO, i)  # marca os simbolos em tela.

import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import _Scripts.Render.ScreenText as ST  # importa a função que exibe textos em tela.
import pygame


def Reload(s):
    """
    Essa função cria o botão reiniciar em posições predeterminadas.
    :param s:
    :return:
    """

    pygame.draw.rect(s, DIM.Color_Black, (100, 320, 200, 50), 2)  # cria o botão reiniciar.
    Text = ST.Screen_Text('Jogar novamente', 20)  # instancia o texto que será impresso.
    imgX = pygame.transform.smoothscale(DIM.Reload, (30, 30))  # dimensiona a imagem do simbolo.
    s.blit(imgX, (129, 330))  # posiciona o simbolo de reiniar em tela.
    s.blit(Text, (163, 339))  # Posiciona o texto do botão em tela.

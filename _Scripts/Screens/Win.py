import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import _Scripts.Render.ScreenText as ST  # importa a função que exibe textos em tela.
import _Scripts.Screens.HomeScreen as HS  # importa a função que exibe a tela inicial.
import _Scripts.Render.ButtonReload as BR  # importa a função que cria o botão jogar novamente em tela.
import pygame


def Win(value):
    """
    Essa função cria uma janela e exibe o vencedor ou empate caso ocorra, e retorna um valor booleano
    que determina o próximo jogador caso exista valor que é retornado da função HomeScreen.
    :param value:
    :return bool:
    """

    while True:
        screen = pygame.display.set_mode(DIM.dimensions_win)  # dimensões da janela do jogo.
        screen.fill(DIM.Color_White)  # cor de fundo da janela.
        pygame.display.set_caption('Congratulations')  # titulo da janela.

        BR.Reload(screen)  # cria o botão reiniciar.

        if pygame.event.get(pygame.MOUSEBUTTONDOWN):  # evento que captura o evento de click.
            (x, y) = pygame.mouse.get_pos()  # armazema as posições de x e y.
            if 100 < x < 300:  # limites do botão jogar novamente em x.
                if 320 < y < 370:  # limites do botão jogar novamente em y.
                    DIM.Symbol_X.clear()  # limpa as listas de jogadas.
                    DIM.Symbol_O.clear()  #
                    return HS.Home_Screen()  # retorna o próximo a jogar se houver.

        if value is None:  # caso ocorra empate.
            ScreenText = ST.Screen_Text('Empate!', 60)  # renderiza a mensagem.
            screen.blit(ScreenText, (120, 150))  # exibe a mensagem de empate em tela.

        else:
            ScreenText = ST.Screen_Text('Vencedor', 60)  # renderiza a mensagem.
            screen.blit(ScreenText, (106, 50))  # exibe a mensagem de vencedor em tela.
            if value:
                imgX = pygame.transform.smoothscale(DIM.Xis, (200, 200))  # dimensiona a imagem do simbolo.
                screen.blit(imgX, (96, 100))  # exibe simbolo em tela.
            else:
                imgO = pygame.transform.smoothscale(DIM.Ball, (200, 200))  # dimensiona a imagem do simbolo.
                screen.blit(imgO, (96, 100))  # exibe simbolo em tela.

        pygame.display.update()  # atualiza a tela.

        if pygame.event.get(pygame.QUIT):  # fecha o programa.
            pygame.quit()
            exit(0)

        pygame.time.delay(100)  # delay para evitar falhas no programa.

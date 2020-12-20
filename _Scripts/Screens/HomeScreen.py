import _Scripts.Render.ScreenText as ST  # importa a função que escreve textos em tela.
import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import pygame


def Home_Screen():
    """
    Essa função cria uma janela que permite escolher o simbolo do primeiro jogador e retorna um valor booleano para X.
    :return bool:
    """

    while True:
        H_Screen = pygame.display.set_mode(DIM.dimensions_home_screen)  # cria a janela do programa.
        H_Screen.fill(DIM.Color_White)  # cor de fundo da janela.
        pygame.display.set_caption('Selecione')  # titulo da janela.
        pygame.draw.line(H_Screen, DIM.Color_Black, (DIM.w_home, DIM.h_home / (3 / 2)),
                         (DIM.w_home, DIM.h_home * 2), width=5)  # desenha a linha vertical.
        pygame.draw.line(H_Screen, DIM.Color_Black, (0, DIM.h_home / (3 / 2)),
                         (DIM.w_home * 2, DIM.h_home / (3 / 2)), width=5)  # desenha a linha horizontal.
        ScreenText = ST.Screen_Text('Selecione o primeiro jogador:', 35)  # texto que será exibido em tela.
        H_Screen.blit(ScreenText, (25, 50))  # exibe o texto em tela.
        H_Screen.blit(DIM.Xis, (20, 155))  # exibe simbolo de X.
        H_Screen.blit(DIM.Ball, (220, 155))  # exibe simbolo de O.
        pygame.display.update()  # atualiza a tela.

        if pygame.event.get(pygame.MOUSEBUTTONDOWN):  # evento de click de mouse.
            (a, b) = pygame.mouse.get_pos()  # atribui as variáveis as posições do mouse.
            if b > 133:  # posição de y.
                if a < 200:  # posição de X.
                    return True  # retorno para a definir o próximo jogador.
                else:
                    return False  # retorno para a definir o próximo jogador.

        if pygame.event.get(pygame.QUIT):  # fecha o programa.
            pygame.quit()
            exit(0)

        pygame.time.delay(100)  # delay no loop para evitar falhas.

import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import _Scripts.Render.DrawRect as DR  # importa a função que irá desenhar as grades na tela.
import _Scripts.Screens.HomeScreen as HS  # importa a função que cria a janela inicial.
import _Scripts.Render.MarkSymbol as MS  # importa a função que marca as jogadas na tela.
import _Scripts.Verification.Verification as VF  # importa a função que verifica se algum jogador já venceu.
import _Scripts.Render.Render as R  # importa a função que atualiza a tela depois de cada jogada.
import _Scripts.Screens.Win as win  # importa a função que exibe a janela do vencedor.
import pygame

pygame.init()
valueX: bool = HS.Home_Screen()  # valor para o jogador X e consequentemente para o jogador O de forma inversa.

while True:
    screen = pygame.display.set_mode((DIM.width, DIM.height))  # dimesões da janela de jogo.
    pygame.display.set_caption('Tic-Tac-Toe')  # titulo da janela.
    screen.fill(DIM.Color_White)  # cor de fundo da janela.

    if pygame.event.get(pygame.QUIT):  # fecha o programa.
        pygame.quit()
        exit(0)

    if pygame.event.get(pygame.MOUSEBUTTONDOWN):  # captura a posição de click do mouse.
        if valueX:
            pos = MS.Mark_symbol(pygame.mouse.get_pos())  # retorna a posição que o simbolo deve ser marcado.
            if pos in DIM.Symbol_X or pos in DIM.Symbol_O:  # verifica se a posição já está sendo utilizada.
                pass
            else:
                DIM.Symbol_X.append(pos)  # adiciona a posição a lista de posições de X.
                valueX = VF.Verification(DIM.Symbol_X, True)  # verifica se esse jogador já venceu.

        else:
            pos = MS.Mark_symbol(pygame.mouse.get_pos())  # retorna a posição que o simbolo deve ser marcado.
            if pos in DIM.Symbol_X or pos in DIM.Symbol_O:  # verifica se a posição já está sendo utilizada.
                pass
            else:
                DIM.Symbol_O.append(pos)  # adiciona a posição a lista de posições de X.
                valueX = VF.Verification(DIM.Symbol_O, False)  # verifica se esse jogador já venceu.

        if len(DIM.Symbol_O) + len(DIM.Symbol_X) == 9:  # verifica o caso de empate.
            valueX = win.Win(None)  # retorna o próximo a jogar se houver.

    DR.Draw_Rect(screen)  # desenha as grades na tela.
    R.Render(screen)  # renderiza os simbolos marcados na tela.
    pygame.display.update()  # atualiza a tela.
    pygame.time.delay(100)  # cria um delay do loop para evitar falhas no python.

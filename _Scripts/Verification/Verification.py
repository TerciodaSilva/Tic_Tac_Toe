import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.
import _Scripts.Screens.Win as W  # importa a função que exibe a vencedor.


def Verification(verification_list, value):
    """
    Essa função verifica se algum jogador já venceu a partida,
    retorna um valor booleano que determina o próximo jogador.
    :param verification_list:
    :param value:
    :return bool:
    """

    cont = 0  # define um contador.
    for i in DIM.WIN:  # verifica todas as possíveis posições de vitória.
        for j in verification_list:  # verifica as jogadas realizadas para esse simbolo.
            if j in i:
                cont += 1  # inicializa o contador
                if cont == 3:  # se três jogadas realizadas forem realizada em um caso de vitória.
                    return W.Win(value)  # exibe o vencedor e retorna o próximo a jogar se houver.
        cont = 0  # reinicia o contador.

    if value:  # inverte o quem será próximo à jogar.
        return False
    else:
        return True

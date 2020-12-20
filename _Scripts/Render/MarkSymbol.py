import _Scripts.Data.Dimensions as DIM  # importa as dimesões e dados que serão utilizados no projeto.


def Mark_symbol(pos):
    """
    Função determina a posição que os simbolos devem ser colocados, analisando a as coordenadas do click do mouse,
    retorna a posição que será exibido o simbolo.
    :param pos:
    :return pos_symbol:
    """

    (x, y) = pos  # atribui a x e y as coordenadas de do mouse.
    for i in DIM.dimensions:  # verifica todas as linhas da grade.
        for j in DIM.dimensions:  # verifica todas as colunas da grade.
            if x < i and y < j:  # confirma a posição para marcar a jogada.
                pos_symbol = [(i - DIM.dimensions_pos),
                              (j - DIM.dimensions_pos)]  # define a posição para marcar.
                return pos_symbol  # retorna a posição.

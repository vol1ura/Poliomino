from typing import List

from poliomino.poliomino import Poliomino
from poliomino.tiling import TableTiling


def make_tiling(t_tiling: TableTiling, pols: List[Poliomino]):
    """
    Algorithm for finding a tiling of a rectangular area by a set of polyominoes.

    :param t_tiling: table tiling object with required width and height
    :param pols: list of poliominos
    :return: True if tiling is exists and False in other case
    """
    states = [t_tiling.position(pol) for pol in pols]
    k = 0
    while 0 <= k < len(pols):
        if next(states[k]):
            k += 1
        else:
            t_tiling.tables.pop()
            states[k] = t_tiling.position(pols[k])
            k -= 1
    print(t_tiling.tables)
    if len(t_tiling.tables) - 1 == len(pols):
        print('The tiling exists.')
        return True
    else:
        print('There is no tiling of a rectangle with the given polyominoes.')
        return False

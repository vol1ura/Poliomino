from typing import List

from poliomino.poliomino import Poliomino, LPoliomino
from poliomino.tiling import TableTiling


def make_tiling(t_tiling: TableTiling, pols: List[Poliomino]):
    """
    Algorithm for finding a tiling of a rectangular area by a set of polyominoes.

    :param t_tiling: table tiling object with required width and height
    :param pols: list of poliominos
    :return: True if tiling is exists and False in other case
    """
    states = [t_tiling.put(pol) for pol in pols]
    k = 0
    while 0 <= k < len(pols):
        if next(states[k]):
            k += 1
        else:
            t_tiling.tables.pop()
            states[k] = t_tiling.put(pols[k])
            k -= 1
    if len(t_tiling.tables) - 1 == len(pols):
        print('The tiling exists.')
        return True
    else:
        print('There is no tiling of a rectangle with the given polyominoes.')
        return False


def parse_params(f_name: str):
    with open(f_name) as fd:
        tuples = lambda: map(int, fd.readline().split())

        t_tiling = TableTiling(*tuples())  # read table dimension, make object
        poliominos = []

        h1 = int(fd.readline())  # number of poliomino
        for i in range(h1):
            n = int(fd.readline())  # power of poliomino set
            for j in range(n):
                poliominos.append(Poliomino(*tuples()))  # substitution of s1 s2

        h2 = int(fd.readline())  # number of L-poliomino
        for i in range(h2):
            n = int(fd.readline())  # power of L-poliomino set
            for j in range(n):
                poliominos.append(LPoliomino(*tuples()))  # substitution of q1 q2
    return t_tiling, poliominos

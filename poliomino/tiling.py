import numpy as np

from poliomino.poliomino import Poliomino, LPoliomino


class TableTiling:
    def __init__(self, m1: int, m2: int):
        """
        Defining table area and empty tiling

        :param m1: width of rectangular table
        :param m2: height of rectangular table
        """
        self.tables = [np.array([], dtype=int).reshape(-1, 2)]
        self.__m1 = m1
        self.__m2 = m2

    def position(self, pol: Poliomino):
        """
        Generator to place poliomino.

        :param pol: poliomino object
        :return: True if poliomino can be placed properly and False if not
        """
        turns = 4 if isinstance(pol, LPoliomino) else 2
        for _ in range(turns):
            for i in range(self.__m1):
                for j in range(self.__m2):
                    arr = np.vstack([self.tables[-1], pol.shift(j, i)])
                    if self.__is_fit(arr):
                        self.tables.append(arr)
                        yield True
            pol.rotate()
        yield False

    def __is_fit(self, arr: np.ndarray) -> bool:
        """
        Check that such array can be a right tiling

        :param arr: numpy array to check
        :return: True if added poliomino if well fit to table and False in other case
        """
        return np.all(arr >= 0) and \
               np.all(arr[:, 0] < self.__m2) and np.all(arr[:, 1] < self.__m1) and \
               np.all(np.unique(arr, axis=0, return_counts=True)[1] == 1)

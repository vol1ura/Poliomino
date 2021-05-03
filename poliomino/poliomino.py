import numpy as np


class Poliomino:
    __T = np.array([0, 1, -1, 0]).reshape(2, -1)  # rotation matrix

    def __init__(self, s1: int, s2: int):
        self._pol = np.array([[i, j] for i in range(s2) for j in range(s1)])

    def rotate(self):
        self._pol = np.dot(self._pol, Poliomino.__T)

    def shift(self, a: int, b: int):
        return self._pol + np.array([a, b])


class LPoliomino(Poliomino):
    def __init__(self, q1: int, q2: int):
        """
        L-poliomino consists of a bottom and left strips of cell, just like the letter L.

        :param q1: parameter Q_1 from the task corresponds to the size of left strip
        :param q2: parameter Q_2 from the task corresponds to the size of right strip
        """
        super().__init__(q1, q2)
        self._pol = np.array([[0, i] for i in range(q1)] + [[j, 0] for j in range(1, q2)])

from poliomino import solver, tiling
from poliomino.poliomino import Poliomino, LPoliomino

tt = tiling.TableTiling(3, 5)
poliominos = [
    Poliomino(2, 2),
    LPoliomino(3, 2),
    LPoliomino(2, 2),
    # LPoliomino(2, 2)
]

solver.make_tiling(tt, poliominos)

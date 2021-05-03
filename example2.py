from poliomino import solver, tiling
from poliomino.poliomino import Poliomino, LPoliomino

tt = tiling.TableTiling(4, 4)
poliominos = [
    Poliomino(2, 3),
    Poliomino(1, 2),
    LPoliomino(3, 2),
    LPoliomino(3, 2)
]

answer = solver.make_tiling(tt, poliominos)

print(answer)

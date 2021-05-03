from poliomino import solver


args = solver.parse_params('parameters.txt')
answer = solver.make_tiling(*args)

print(answer)

grid = ["Hamilton", "Leclerc", "Senna"] # 0 , 1 , 2 

grid.append("Bortoleto")

grid.append("Piquet")

grid.append("Massa")

grid.append("Mansell")

print(grid[0])

print(grid[1]) 

print(grid[2]) 

print(grid[3])

print(grid[4])

print(grid[5])

print(grid[6])

#pole = grid[0]

pit_stop = grid[1]

print("Quem parou no pit stop foi: ", pit_stop)

piloto_a_realizar_passagem = grid[2] # Senna

grid.pop(1)
grid.pop(1)

print("O piloto a realizar a passagem é: ", piloto_a_realizar_passagem)

grid.insert(1, piloto_a_realizar_passagem)

grid.insert(2, pit_stop) # "Leclerc"

print("A posição de cada piloto é: ", grid)

pit_stop = grid[0]
piloto_a_realizar_passagem = grid[1]
print("Quem parou no pit stop foi: ", pit_stop)
print("O piloto a realizar a passagem é: ", piloto_a_realizar_passagem)

grid.pop(0)

grid.insert(1, pit_stop)
print("A posição de cada piloto é: ", grid)


""" tupla = ("Hamilton", "Leclerc", "Senna")

print("A tupla de pilotos é: ", tupla)

tupla.append("Bortoleto") # Tuplas são imutáveis, não é possível adicionar elementos a uma tupla

print("A tupla de pilotos é: ", tupla) """

""" for position in grid:
    print(f"A posição de cada piloto é: {grid.index(position)} - {position}") """
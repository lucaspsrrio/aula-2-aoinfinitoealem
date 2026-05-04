grid = ["Hamilton", "Leclerc", "Senna"] # 0 , 1 , 2 

grid.append("Bortoleto")

grid.append("Piquet")

grid.append("Massa")

grid.append("Mansell")

grid.append("Sennna")

frutas = ["banana", "maçã", "laranja", "maçã", "banana", "maçã"]

for piloto in grid:
    print(f"A posição desse piloto é: {grid.index(piloto) + 1}, e o corredor é {piloto}")
    if piloto == "Senna":
        ano = 1994
        ano_atual = 2026
        print(f"Hoje, faz {ano_atual - ano} anos que o nosso ídolo {piloto} virou uma estrela.")
        
        
for fruta in frutas:
    print(f"A posição dessa fruta é: {frutas.index(fruta) + 1}, e a fruta é {fruta}")

for posicao in range(len(frutas)):
    print(f"A posição dessa fruta é: {posicao + 1}, e a fruta é {frutas[posicao]}")
    
## print the numbers from 0 through 99
for i in range(100):
    print(f"i + 1 = {i}")
    
## Aqui vai printar os numeros de 100 a 1, de forma decrescente
for i in range(100, 0, -1):
    print(f"i - 1 = {i}") 
    
    
if "Senna" in grid:
    print("O piloto Senna está presente na lista de pilotos.")
    print("A posição do Senna é: ", grid.index("Senna") + 1)
lados = list()
for v in range(0, 3):
    lado = int(input(f"digite lado{v} do seu triangulo : "))
    lados.append(lado)
lados.sort()
if lados[2] <= lados[0] + lados[1]:
    print("é um triangulo")
else:
    print("nao È um triangulo")
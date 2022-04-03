print("se voce nao quiser compra digite 0")
kgDeMaças=float(input("quantos quilosgramas de maças você quer : "))
KgDeMorango=float(input("quantos quilosgramas de morango você quer : "))
peçoTotal= kgDeMaças+KgDeMorango
if kgDeMaças <= 5 :
    valor = kgDeMaças*1.50
else:
    valor = kgDeMaças*1.10
if KgDeMorango <= 5:
    valor += KgDeMorango*2
else:
    valor+= kgDeMaças*1.80
if (peçoTotal >= 8) or (valor >=25):
    print(peçoTotal, valor)

    desconto = valor*0.10
    valor -= desconto
    

print(f"você comprou {kgDeMaças} de maça e {KgDeMorango} de morango . custo total foi de {valor}R$")
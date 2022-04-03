combustivel = str(input("qual o combustivel meu patrao? so tem alcool e gasolina. : "))[0].lower()
quantidadeEmLitros = float(input("quantos litros chefes? "))
if combustivel in "Aa":
    if quantidadeEmLitros <= 20 :
        presoTotal = (quantidadeEmLitros*0.90)
        desconto = presoTotal-(presoTotal*0.04)
        print(f"voce comprou {quantidadeEmLitros} litros  de alcool e o valor total é de {desconto}")
    else:
        presoTotal = (quantidadeEmLitros*0.90)
        desconto = presoTotal-(presoTotal*0.06)
        print(f"voce comprou {quantidadeEmLitros} litros  de alcool e o valor total é de {desconto}")
if combustivel in "Cc":
    if quantidadeEmLitros <= 20 :
        presoTotal = (quantidadeEmLitros*1.20)
        desconto = presoTotal-(presoTotal*0.03)
        print(f"voce comprou {quantidadeEmLitros} litros  de gasolina e o valor total é de {desconto}")
    else:
        presoTotal = (quantidadeEmLitros*1.20)
        desconto = presoTotal-(presoTotal*0.05)
        print(f"voce comprou {quantidadeEmLitros} litros  de gasolina e o valor total é de {desconto}")
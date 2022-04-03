from datetime import datetime
anoNascimento = int(input("digite seu ano de nascimento : "))
l = datetime.now()
anoAtual= int(l.strftime("%y")) + 2000
ideda =  anoAtual - anoNascimento 
print(ideda)
if ideda <= 16: 
    print("voce ainda nao tem idade para votar.")
else:
    print("voce pode votar ,entao estude bem em quem voce vai votar.")

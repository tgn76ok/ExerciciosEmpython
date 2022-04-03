#ler as 3 notas obtidas por um aluno nas 3 verificaçoes e a media dos exercicios ue fazem parte da avaliaçao. calcular a media aproietamento
prova1 = float(input("digite a sua nota na primeira prova :"))
prova2 = float(input("digite a sua nota na segunda prova :")) * 2
prova3 = float(input("digite a sua nota na terceira prova :"))* 3
media_exercicios = int(input("digite nota da media de exercicios :"))


mediaDeAproveitamento = (prova1+prova2+prova3+media_exercicios)/7
if mediaDeAproveitamento >= 9.0:
    nota = "A"
if 7.5 >= mediaDeAproveitamento< 9.0:
    nota = "B"
if 6.0 >= mediaDeAproveitamento < 7.5:
    nota = "c"
if mediaDeAproveitamento < 6.0:
    nota = "D"    
print (f"a sua nota foi {nota}")
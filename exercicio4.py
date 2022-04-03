valores = list()
for v in range(0, 3):
    valor = int(input(f"digite um valor{v} : "))
    valores.append(valor)
valores.sort()
valores.__delitem__(0)
soma = valores[0]+valores[1]
print(f"os dois miores valores somados são: {soma}")
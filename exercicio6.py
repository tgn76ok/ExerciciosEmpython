quantasmacas=int(input("digite qunatas maças foram compradas : "))
if quantasmacas < 12:
    valordamaça=quantasmacas * 1.30
else:
    valordamaça = quantasmacas
print (f"voce comprou {quantasmacas} maças e custou r${valordamaça}")
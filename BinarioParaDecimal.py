binario = input("Digite o número binário: ")
decimal = 0
cont = len(binario)
for i in binario:
  decimal += 2**(cont-1) * int(i)
  cont -= 1
print(decimal)

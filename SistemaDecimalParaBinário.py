numero = int(input("Digite um número: "))

quociente = numero 
lista = []

while quociente >= 2:
  quociente = numero // 2
  resto = numero % 2
  numero = quociente
  lista.append(resto)  
lista.append(quociente)
s = ''
for i in reversed(lista):
  s += str(i)
print(s)

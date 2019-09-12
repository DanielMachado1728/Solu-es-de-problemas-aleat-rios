l = [('a','b'), ('a','f'), ('a','c'), ('a','d'), ('b','a'), ('f','a'), ('c','a'), ('c','g'),('g','c'), ('d','a'), ('d','e'), ('e','d'), ('e','h'),('h','e') ]
def ordena_lista_tuplas(lista):
  l2 = []
  for parentese in l:
    for letra in parentese:
      l2.append(letra)
  #print(l2)
  d = {}
  for i in l2:
    d[i] = l2.count(i)
  #print(d)
  #print()
  lista = sorted(d.values())
  lista = lista[::-1]
  #print(lista)
  d2 = {}
  for numero in lista:
    for chave,valor in d.items():  
      if numero == valor:
        d2[chave] = numero
  #print(d2)
  ordenamento_vertices = []
  for chave in d2:
    ordenamento_vertices.append(chave)
  return ordenamento_vertices
lista_ordenada = (ordena_lista_tuplas(l))
print(lista_ordenada)

def adjacencias(lista,vertice):
  adjacentes = []
  for parentese in lista:
    if  parentese[0] == vertice:
      adjacentes.append(parentese[1])
  return adjacentes
#print(adjacencias(l,'a'))
def naoadjacencia(lista,vertice):
  naoadjacencia = []
  a = adjacencias(lista,vertice)
  for i in lista_ordenada:
    if (i in a) or i == vertice:
      continue
    else:
      naoadjacencia.append(i)
  return naoadjacencia
print(naoadjacencia(l,'a'))

#def vizinho_pintado(d,vertice):

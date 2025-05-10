# 1
listaDeNumeros = list(range(4, 101, 4))
print(listaDeNumeros)

# 2
listaFavoritos = ["Surf", "Programar","Anime", "Mate", "Musica"]
print(listaFavoritos[len(listaFavoritos) - 2]) 

# 3
listaVacia = []
listaVacia.append(13)
listaVacia.append(True)
listaVacia.append("Bateria")
print(listaVacia)

# 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5
numeros = [8, 15, 3, 22, 7] 
numeros.remove(max(numeros))
print(numeros)

# 6
numeros10al30 = list(range(10, 31, 5))
print(numeros10al30[0:2])

# 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "yaris"
autos[2] = "fox"
print(autos)

# 8
dobles = []
dobles.append(2 * 5)
dobles.append(2 * 10)
dobles.append(2 * 15)
print(dobles)

# 9
compras = [["huevo", "leche"], ["arroz", "fruta", "gaseosa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# 10
listaAnidada = [15, True, [25.5, 57.9, 30.6], False]
print(listaAnidada)

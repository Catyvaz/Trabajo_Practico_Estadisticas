
def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

# En esta funcion se ingresa una lista, y se devuelve otra lista con las frecuencias relativas de cada elemento de la lista (elementos no repetidos)
def CALCULAR_FRECUENCIA_RELATIVA(lista):
    # 1. lista para utilizar al final. 2. Una lista con los elementos sin repetir. 3. El diccionario con las frecuencias absolutas de la lista
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
# se evaluan los elementos que estan en la lista, y utilizando el elemento como key, se busca el valor absoluto del elemento
# Al tener la frecuencia absoluta, se la divide por la cantidad de elementos en la lista original. Se agrega SOLO el valor relativo a la lista
# en la posicion del elemento 
    for elemento in lista:
        absoluta = frecuencia_absoluta[(elemento)]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(round(frecuencia, 4)) #ver si hay que redondearlo o no
# Devuelve una LISTA
    return frecuencia_relativa

def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    # se crea una lista nueva, vacia, que es donde se van a guardar los datos de la acumulada
    frecuencia_relativa_acumulada = []
    # se crea una variable tipo lista que almacena las frecuencias relativas de los elementos de la lista
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    total = 0

    # Se pasa por cada elemento de la lista, y se lo suma al total, el cual va acumulando todos los valores
    for i in range (len(frecuencia_relativa)):
        total += frecuencia_relativa[i]
        frecuencia_relativa_acumulada.append(total)
    # La funcion devuelve una LISTA con todos los valores de la aumulada, en la posicion de los elementos de la lista, ya ordenados de mayor a menor.
    return frecuencia_relativa_acumulada
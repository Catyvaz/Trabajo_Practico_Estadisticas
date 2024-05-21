def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias


# En esta funcion, se ingresa una lista de elementos, y se va a asegurar de que no se repitan los elementos.
def SOLO_UN_ELEMENTO(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# LA KEY ES IGUAL AL ELEMENTO
# La lista al llegar aca ya está ordenada

# En esta funcion se ingresa una lista, y se devuelve otra lista con las frecuencias relativas de cada elemento de la lista (elementos no repetidos)
def CALCULAR_FRECUENCIA_RELATIVA(lista):
    # 1. lista para utilizar al final. 2. Una lista con los elementos sin repetir. 3. El diccionario con las frecuencias absolutas de la lista
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
# se evaluan los elementos que estan en la lista sin duplicado, y utilizando el elemento como key, se busca el valor absoluto del elemento
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
    # La funcion devuelve una LISTA con todos los valores de la aumulada, en la posicion de los elementos de la lista, sin duplicar y ya ordenados de mayor a menor.
    return frecuencia_relativa_acumulada

print("\n")
lis = [1,1,1,2,2,5,5,5,6,7,7,8]
absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lis)
frecuencia_1 = CALCULAR_FRECUENCIA_RELATIVA(lis)
frecuencia_rela_acum = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lis)
# frecuencia_2= CALCULAR_FRECUENCIA_RELATIVA_2(lis)
print("absoluta  " , absoluta)
print("lista: ", lis)
print("frecuencia en lista  ", frecuencia_1)
print("frecuencia relativa acumulada: ", frecuencia_rela_acum)
# print("frecuencia en diccionario  ", frecuencia_2)
print("\n")

# # En esta funcion se ingresa una lista, y se devuelve un diccionario
# def CALCULAR_FRECUENCIA_RELATIVA_2(lista):
# # Se guarda el diccionario de las frecuencias absolutas
#     diccionario_abso_rela = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
# #Para cada elemento del diccionario.
#     for elemento in diccionario_abso_rela:
# # se guarda en la variable la divicion de valor absoluto del elemento en el diccionario y se lo divide por la cantida de elementos en a lista original
# # Se agrega al diccionario un nuevo parametro que es F_relativa, con el valor de la frecuencia relativa del elemento
#         frecuencia_relativa = diccionario_abso_rela[elemento] / len(lista)
#         diccionario_abso_rela[elemento] = {"F_relativa": frecuencia_relativa}
# # Se devuelve un DICCIONARIO
#     return diccionario_abso_rela
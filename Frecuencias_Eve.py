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
def CALCULAR_FRECUENCIA_RELATIVA_1(lista):
    # 1. lista para utilizar al final. 2. Una lista con los elementos sin repetir. 3. El diccionario con las frecuencias absolutas de la lista
    frecuencia_relativa = []
    lista_sin_duplicados = SOLO_UN_ELEMENTO(lista)
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
# se evaluan los elementos que estan en la lista sin duplicado, y utilizando el elemento como key, se busca el valor absoluto del elemento
# Al tener la frecuencia absoluta, se la divide por la cantidad de elementos en la lista original. Se agrega SOLO el valor relativo a la lista
# en la posicion del elemento 
    for elemento in lista_sin_duplicados:
        absoluta = frecuencia_absoluta[(elemento)]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(frecuencia)
# Devuelve una LISTA
    return frecuencia_relativa

#En esta funcion se calcula la frecuencia porcentual de cada elemento en la lista
def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    #Se llama a la funcion CALCULAR_FRECUENCIA_RELATIVA para obtener la frecuencia relativa
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA_1(lista)
    #La expresion "elemento * 100" se aplica a cada elemento de la frecuencia relativa
    #Y se guarda en la lista frecuencia porcentual
    frecuencia_porcentual = [elemento * 100 for elemento in frecuencia_relativa]

    #Devuelve la lista de frecuencias porcentuales
    return frecuencia_porcentual

#En esta funcion se calcula la frecuencia porcentual acumulada
def CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista):
    #Se llama a la funcion frecuencia porcentual para obtener la frecuencia porcentual acumulada
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    #Inicializa una lista vacia para almacenar las frecuencias porcentuales acumuladas
    frecuencia_porcentual_acumulada = []
    #Esta variable se utiliza para mantener el total acumulado de las frecuencias porcentuales.
    #Inicia con valor 0 para que acumule todas las frecuencias porcentuales.
    acumulada = 0

    #Inicia bucle for que itera en cada elemento en frecuencia porcentual
    for elemento in frecuencia_porcentual:
        #Suma el elemnto actual al total acumulado
        acumulada += elemento
        #Agrega el valor acumulado actual a la lista de frecuencias porcentuales acumuladas
        frecuencia_porcentual_acumulada.append(acumulada)
    #Devuelve la lista de frecuencias porcentuales acumuladas
    return frecuencia_porcentual_acumulada


print("\n")
lis = [1,1,1,2,2,5,5,5,6,7,7,8]
absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lis)
frecuencia_1 = CALCULAR_FRECUENCIA_RELATIVA_1(lis)
#frecuencia_2= CALCULAR_FRECUENCIA_RELATIVA_2(lis)
frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lis)
frecuencia_porcentual_acumulada = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lis)
print("absoluta  " , absoluta)
print("frecuencia en lista  ", frecuencia_1)
#print("frecuencia en diccionario  ", frecuencia_2)
print("porcentual  ", frecuencia_porcentual)
print("porcentual acumulada  ", frecuencia_porcentual_acumulada)
print("\n")
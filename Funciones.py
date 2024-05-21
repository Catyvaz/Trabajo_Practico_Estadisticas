
#FRECUENCIAS

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

def AGREGAR_ELEMENTOS_INPUT(lista):
    numero_muestra = 0
    print("Ingrese las muestras una por una. Cuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        # Se ingresan los numeros uno por uno y mediante el "numero_muestra + 1" se va incrementando en la terminal el numero que se ingresa.
        valor = input(f"Ingrese número de muestra {numero_muestra + 1}: ")
        # Aca se evalua si el elemento ingresado es de valor numerico. 
        # Si es un valor numerico, se lo agrega a la lista "lista_muestras".
        # Si el valor es NO numerico, se evalua; si es la palabra "FIN" no se desean agregar mas números a la lista, si es una letra random marca no valido y deja volver a intentar.
        if valor.isdigit():
            lista_muestras.append(valor)
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de las muestras")
                break
            else:
                print("Comando no válido, intente de nuevo.")
    lista_muestras = sorted(lista_muestras)
    return lista_muestras
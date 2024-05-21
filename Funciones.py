
#FRECUENCIAS

def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

#En esta funcion se calcula la frecuencia porcentual de cada elemento en la lista
def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    #Se llama a la funcion CALCULAR_FRECUENCIA_RELATIVA para obtener la frecuencia relativa
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA_1(lista)
    #La expresion "elemento * 100" se aplica a cada elemento de la frecuencia relativa
    #Y se guarda en la lista frecuencia porcentual
    frecuencia_porcentual = [elemento * 100 for elemento in frecuencia_relativa]

    #Devuelve la lista de frecuencias porcentuales
    return frecuencia_porcentual

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

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    Frecuencias_Absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    Frecuencia_Absoluta_Acumulada = {}
    Acumulador = 0
    for elemento, frecuencia in Frecuencias_Absolutas.items():
        acumulador += frecuencia
        Frecuencia_Absoluta_Acumulada[elemento] = acumulador
    return Frecuencia_Absoluta_Acumulada

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

#INTERVALOS

def CALCULAR_AMPLITUD_INTERVALOS(datos, numero_intervalos):
    Minimo = min(datos)  # Encontrar el valor mínimo en los datos
    Maximo = max(datos)  # Encontrar el valor máximo en los datos
    Amplitud = (Maximo - Minimo) / numero_intervalos  # Calcular la amplitud del intervalo
    return Amplitud

def CALCULAR_INTERVALOS_CLASE(datos):
    import math # Se utiliza la función math para luego sacar el logaritmo 2 lineas más abajo
    Cantidad_Datos = len(datos)
    Numero_Intervalos = (1+ 3.322) * math.log(Cantidad_Datos) # Determinar el número de intervalos utilizando la fórmula de Sturges
    Amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos, Numero_Intervalos)  # Calcular la amplitud del intervalo

    Limite_Inferior = min(datos)
    Limite_Superior = Limite_Inferior + Amplitud
    Intervalos = []

    while Limite_Superior <= max(datos):
        Intervalos.append((Limite_Inferior, Limite_Superior)) # Se unen los límites para crear el intervalo
        Limite_Inferior = Limite_Superior
        Limite_Superior += Amplitud

    return Intervalos 



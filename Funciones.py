#MEDIDAS DE POSICION

def MEDIA(lista):
    media = sum(lista)/len(lista)
    return media 

def CALCULAR_MODA(lista):
    frequencia= {}
    for elemento in lista:
        if elemento in frequencia:
            frequencia[elemento] +=1
        else:
            frequencia[elemento] = 1
    moda = None
    maxFrequencia= 0
    for elemento, frequencia in frequencia.items():
        if frequencia>maxFrequencia:
            moda=elemento
            maxFrequencia=frequencia
              
    return moda

def CALCULAR_MEDIANA(lista):
    listaOrdenada=sorted(lista)
    longitudLista=len(listaOrdenada)
    
    if longitudLista % 2 == 0:
        medioIzq = listaOrdenada[longitudLista // 2 -1 ]
        medioDer = listaOrdenada[longitudLista // 2 ]
        mediana = (medioIzq + medioDer) / 2
    else:
        mediana = listaOrdenada [longitudLista // 2]
        return mediana

# calcular promedio(sumatoria de todos los datos / cantidad de datos)
def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# calcular desviacion estandar((sumatoria de todos los datos - prom)**2/cant de datos -1)
def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    suma_resta_cuadrado = (sum(lista) - promedio) ** 2
    desviacion = (suma_resta_cuadrado / (n -1)) ** 0.5
    return desviacion 


def CALCULAR_CUARTILES(lista):
    #Ordena la lista de menor a mayor y la guarda en la variable lista_ordenada
    lista_ordenada=sorted(lista)
    #Calcula la logitud de la lista y la guarda en variable longitus_lista
    longitud_lista=len(lista)

    q1_index= int(0.25 * (longitud_lista + 1))
    q2_index= int(0.5 * (longitud_lista + 1))
    q3_index= int(0.75 * (longitud_lista + 1))

    q1= lista_ordenada[q1_index]
    q2= lista_ordenada[q2_index]
    q3= lista_ordenada[q3_index]

    return q1, q2, q3 

def RANGO(n_mayor, n_menor):
    # en la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
    valor_rango = n_mayor - n_menor
    return valor_rango

#FRECUENCIAS

def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    Frecuencias_Absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    Frecuencia_Absoluta_Acumulada = {}
    Acumulador = 0
    for elemento, frecuencia in Frecuencias_Absolutas.items():
        acumulador += frecuencia
        Frecuencia_Absoluta_Acumulada[elemento] = acumulador
    return Frecuencia_Absoluta_Acumulada

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


#En esta funcion se calcula la frecuencia porcentual de cada elemento en la lista
def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    #Se llama a la funcion CALCULAR_FRECUENCIA_RELATIVA para obtener la frecuencia relativa
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
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


#####################################################################################################################################

# Converti el input en una funcion, para que si en algun momento se desean agregar mas elementos, se pueda reutilizar
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
            lista.append(int(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de las muestras")
                break
            else:
                print("Comando no válido, intente de nuevo.")
    lista = sorted(lista)
    return lista

lista_muestras = []
lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
numero_muestra = len(lista_muestras)
print(lista_muestras)
print(numero_muestra)

#CATY terminar la funcionalidad de modificar la lista
# while True:
#     cambios = input("Desea realizar algun cambio? \n 1 = SI | 2 = NO: ")
#     if cambios == 1:
#         si = input("Que cambio desea realizar? 1 = eliminar | 2 = modificar | 3 = agregar")

#Funciones que evaluan cositas, lo tengo que terminar, lo hago funcion para que quede mas limpio el codigo, lo hablamos
def MEDIDAS_POSICION(lista):
    comando = int(input("¿Que desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MINIMO.\n 6 = RANGO.\n 7 = DESVIO ESTANDAR.\n 8 = CUARTILES.\n ==>"))
    # if comando == 1:

 #def TABLAS_FRECUENCIAS(lista):
    # comando = int(input("¿Que frecuencia desea conocer?\n 1 = ABSOLUTA. \n 2 = ABSOLUTA ACUMULADA.\n 3 = RELATIVA.\n 4 = RELATIVA ACUMULADA.\n 5 = PORCENTUAL.\n 6 = PORCENTUAL ACUMULADA.\n 7 = INTERVALOS.\ 8 = AMPLITUD DE INTERVALOS.\n ==> "))
        
# esto seria lo unico que queda en el main, pero podemos dejar tambien las funciones que ordenan al input, hay que hablarlo
while True:    
    #Este print le permite al usuario seleccionar que tipo de informacion desea recibir de la lista de muestras
    # CATY, hay que hacer que esto sea mas util para el usuario (agregar numeros olvidados, que no se termine de una, etc)
    respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = FRECUENCIAS: ")
    if int(respuesta) == 1:
        print("Seleccionaste < medidas de posición >")
        resultado = MEDIDAS_POSICION(lista_muestras)
    elif int(respuesta) == 2:
        print("Seleccionaste < frecuencias >")
        #resultado = TABLAS_FRECUENCIAS(lista_muestras)

    #Aca se evalua si se quiere seguir utilizando el programa o no
    # CATY, ver que va a hacer el programa en caso de escribir un comando no valido, en todo caso, hacer que cualquier letra signifique fin del programa 
    continuacion = input("¿Desea volver a empezar? Y = si, N = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "N":
            break
        elif continuacion.upper == "Y":
            print("Volvemos a empezar!")
        else: #arreglar esta linea
            print("Comando no válido.")
    else:
        print("Comando no válido")
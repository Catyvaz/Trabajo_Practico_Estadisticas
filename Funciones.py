import math
#MEDIDAS DE POSICION

def MEDIA(lista):
    media = sum(lista)/len(lista)
    return media 
    
def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    
    for Numero in lista:
        Cont = 0
        for Elem in lista:
            if Elem == Numero:
                Cont += 1
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)

    if len(Modas) == len(set(lista)): #set elimina automáticamente los elementos duplicados y conserva solo uno de cada elemento
        return "No hay moda"
    else:
        return Modas
    
def CALCULAR_MEDIANA(lista):
    listaOrdenada=sorted(lista) # Ordena la lista de mayor a menor para luego poder obtener el valor del medio
    longitudLista=len(listaOrdenada) # Almacena la longitud de la lista (ya ordenada)
    
    if longitudLista % 2 == 0: #Verifica si la longitud de la lista ordenada es par
        medioIzq = listaOrdenada[longitudLista // 2 -1 ] #Define el indice del medio izquierdo de la lista dividiendo por dos (division entra )y restando 1 para posicionarse a la izquierda
        medioDer = listaOrdenada[longitudLista // 2 ] #Define el indice del medio dercho de la lista 
        mediana = (medioIzq + medioDer) / 2 #Suma las variables del medio y las divide por dos respetando la formula para calcular la mediana en listas con una longitud par
        return mediana
    else:
        mediana = listaOrdenada [longitudLista // 2] #En caso de ser impar se obtiene el indice central 
        return mediana

# calcular promedio(sumatoria de todos los datos / cantidad de datos)
def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# calcular desviacion estandar: raíz cuadrada ((suma((elemento - media)**2))/cantidad de datos - 1)
def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    #Calcula la suma de los cuadrados de las diferencias entre cada elemento y el promedio
    suma_resta_cuadrado = sum((x- promedio) ** 2 for x in lista)
    #Calcula la desviación estandar dividiendo la suma de las diferencias cuadradas entre n-1
    #y tomando la raiz cuadrada del resultado
    desviacion = (suma_resta_cuadrado / (n -1)) ** 0.5
    return desviacion

def CALCULAR_CUARTILES(lista):
     Longitud_Lista = len(lista)
     mediana = CALCULAR_MEDIANA (lista)   #se define la mediana para ser utilizada como q2

     if Longitud_Lista % 2 == 0:
        mitad_inferior = lista[:Longitud_Lista//2] #obtiene la mitad inferior de la lista utilizando el slicing (comienza al principio de la lista y finaliza en la mitad Longitud_lista//2)
        mitad_superior = lista[Longitud_Lista//2:] #obtiene la mitad superior de la lista utilizando el slicing (comienza en la mitad Longitud_lista//2 finaliza en el ultimo indice de la lista)
     else:
        mitad_inferior = lista[:Longitud_Lista//2] #obtiene la mitad inferior de la lista utilizando el slicing (comienza al principio de la lista y finaliza en la mitad Longitud_lista//2)
        mitad_superior = lista[Longitud_Lista//2 + 1:] #obtiene la mitad superior de la lista utilizando el slicing (comienza en la mitad Longitud_lista//2 finaliza en el ultimo indice de la lista)

     q1 = CALCULAR_MEDIANA(mitad_inferior) #se calcula la mediana de la mitad inferior
     q2 = mediana #se define a q2 como la mediana
     q3 = CALCULAR_MEDIANA(mitad_superior) #se calcula la mediana de la mitad superior
    
     return print("Cuartil 1:", q1 , "// Cuartil 2:",q2,"// Cuartil 3:", q3) #SE PRINTEAN LOS 3 CUARTILES COMO 

def RANGO(lista):
    # en la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
    valor_rango = lista[-1] - lista[0]
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
    Frecuencias_Absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista) #Se obtienen las frecuencias absolutas con la función ya creada
    Frecuencia_Absoluta_Acumulada = {} # Diccionario para almacenar la frecuencia absoluta acumulada de cada elemento
    Acumulador = 0 #Variable acumuladora para almacenar la frecuencia acumulada actual
    for elemento, frecuencia in Frecuencias_Absolutas.items(): # Recorrer las frecuencias absolutas y calcular la frecuencia absoluta acumulada
        Acumulador += frecuencia # Incrementar el acumulador con la frecuencia actual
        Frecuencia_Absoluta_Acumulada[elemento] = Acumulador # Asignar la frecuencia absoluta acumulada al elemento
    return Frecuencia_Absoluta_Acumulada

def SOLO_UN_ELEMENTO(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# En esta funcion se ingresa una lista, y se devuelve otra lista con las frecuencias relativas de cada elemento de la lista (elementos no repetidos)
def CALCULAR_FRECUENCIA_RELATIVA(lista):
    # 1. lista para utilizar al final. 2. Una lista con los elementos sin repetir. 3. El diccionario con las frecuencias absolutas de la lista
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    lista_simple = SOLO_UN_ELEMENTO(lista)
    # se evaluan los elementos que estan en la lista, y utilizando el elemento como key, se busca el valor absoluto del elemento
    # Al tener la frecuencia absoluta, se la divide por la cantidad de elementos en la lista original. Se agrega SOLO el valor relativo a la lista
    # en la posicion del elemento 
    for elemento in lista_simple:
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
    import math
    
    Cantidad_Datos = len(datos)
    Numero_Intervalos = 1 + 3.322 * math.log10(Cantidad_Datos) #se utiliza la formula de Sturges para usar la función de logaritmo
    Amplitud = CALCULAR_AMPLITUD_INTERVALOS(datos, Numero_Intervalos) #Se llama la función "CALCULAR_AMPLITUD_INTERVALOS" que creamos antes
    
    Limite_Inferior = min(datos)
    Limite_Superior = Limite_Inferior + Amplitud
    Intervalos = [] #se crea la variable intervalos

    while Limite_Superior <= max(datos): 
        Intervalos.append((Limite_Inferior, Limite_Superior)) #se crea el intervalo uniendo los dos límites
        Limite_Inferior = Limite_Superior
        Limite_Superior += Amplitud
    return Intervalos
    
# Funciones del input

# Converti el input en una funcion, para que si en algun momento se desean agregar mas elementos, se pueda reutilizar
def AGREGAR_ELEMENTOS_INPUT(lista):
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y aprete enter para confirmar y continuar agregando mas datos. \nCuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        # Se ingresan los numeros uno por uno y mediante el "numero_muestra + 1" se va incrementando en la terminal el numero que se ingresa.
        valor = input(f"Ingrese dato número {numero_muestra + 1}: ")
        # Aca se evalua si el elemento ingresado es de valor numerico. 
        # Si es un valor numerico, se lo agrega a la lista "lista_muestras".
        # Si el valor es NO numerico, se evalua; si es la palabra "FIN" no se desean agregar mas números a la lista, si es una letra random marca no valido y deja volver a intentar.
        if valor.isdigit():
            lista.append(float(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de la muestra")
                break
            else:
                print("Comando no válido, intente de nuevo.")
        else: #Se va a intentar pasar el valor a un elemento float, en caso de no poder, en vez de frenar el código, aparecerá la exepcion pero podemos continuar
            try:
                valor = float(valor)
                lista.append(valor)
                numero_muestra += 1
            except:
                print("Comando no válido, intente de nuevo.")

    lista = sorted(lista)
    return lista

#Funciones que evaluan cositas, lo tengo que terminar, lo hago funcion para que quede mas limpio el codigo, lo hablamos
def MEDIDAS_POSICION(lista): #Aca se ve que funcion de las medidad de posicion es la que se va a aplicar, de acuerdo a los numeros.
    while True:
        comando = int(input("¿Que desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MINIMO.\n 6 = RANGO.\n 7 = DESVIO ESTANDAR.\n 8 = CUARTILES.\n ==> "))
        if comando == 1:
            valor = "La > Media Aritmérica < de la lista es "
            resultado = MEDIA(lista)
            break
        elif comando == 2:
            valor = "La > Moda < de la lista es "
            resultado = CALCULAR_MODA(lista)
            break
        elif comando == 3:
            valor = "La > Mediana < de la lista es "
            resultado = CALCULAR_MEDIANA(lista)
            break
        elif comando == 4:
            valor = "El > Máximo < de la lista es "
            resultado = lista[-1]
            break
        elif comando == 5:
            valor = "El > Mínimo < de la lista es "
            resultado = lista[0]
            break
        elif comando == 6:
            valor = "El > Rango < de la lista es "
            resultado = RANGO(lista)
            break
        elif comando == 7:
            valor = "El > Desvio Estandar < de la lista es "
            resultado = DESVIACION_ESTANDAR(lista)
            break
        elif comando == 8:
            valor = "Los > Cuartiles < de la lista son "
            resultado = CALCULAR_CUARTILES(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    
    print(lista)
    print(f"{valor}: ", resultado)

def TABLAS_FRECUENCIAS(lista):  #Aca se ve que funcion de las tablas de frecuencia es la que se va a aplicar, de acuerdo a los numeros.
    while True:
        comando = int(input("¿Que frecuencia desea conocer?\n 1 = ABSOLUTA. \n 2 = ABSOLUTA ACUMULADA.\n 3 = RELATIVA.\n 4 = RELATIVA ACUMULADA.\n 5 = PORCENTUAL.\n 6 = PORCENTUAL ACUMULADA.\n 7 = INTERVALOS.\n 8 = AMPLITUD DE INTERVALOS.\n ==> "))
        if comando == 1:
            valor = "La > Frecuencia Absoluta < de la lista es "
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
            break
        elif comando == 2:
            valor = "La > Frecuencia Absoluta Acumulada < de la lista es "
            resultado = CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista)
            break
        elif comando == 3:
            valor = "La > Frecuencia Relativa < de la lista es "
            resultado = CALCULAR_FRECUENCIA_RELATIVA(lista)
            break
        elif comando == 4:
            valor = "La > Frecuencia Relativa Acumulada < de la lista es "
            resultado = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista)
            break
        elif comando == 5:
            valor = "La > Frecuencia Porcentual < de la lista es "
            resultado = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
            break
        elif comando == 6:
            valor = "La > Frecuencia Porcentual Acumulada < de la lista es "
            resultado = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista)
            break
        elif comando == 7:
            valor = "Los > Intervalos < de la lista son "
            resultado = CALCULAR_INTERVALOS_CLASE(lista)
            break
        elif comando == 8:
            valor = "La > Amplitud de Intervalos < de la lista es "
            resultado = CALCULAR_AMPLITUD_INTERVALOS(lista)
            break
        else:
            print("Comando incorrecto, intente de nuevo")
    print(lista)
    print(f"La {valor}: ", resultado)   

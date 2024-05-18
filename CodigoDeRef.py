def CALCULAR_MENOR(lista):
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo


def SUMA(lista):
    suma = sum(lista)
    return suma


def MEDIA(lista):
    media = SUMA(lista) / len(lista)
    return media


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
    promedio = CALCULAR_PROMEDIO(lista)
    suma_resta_cuadrado = sum((x - promedio) ** 2 for x in lista)
    desviacion = (suma_resta_cuadrado / (n - 1)) ** 0.5
    return desviacion


def CALCULAR_MEDIANA(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(listaOrdenada)

    if longitudLista % 2 == 0:
        medioIzq = listaOrdenada[longitudLista // 2 - 1]
        medioDer = listaOrdenada[longitudLista // 2]
        mediana = (medioIzq + medioDer) / 2
    else:
        mediana = listaOrdenada[longitudLista // 2]
    return mediana


def CALCULAR_CUARTILES(lista):
    listaOrdenada = sorted(lista)
    longitudLista = len(lista)

    q1_index = int(0.25 * (longitudLista + 1)) - 1
    q2_index = int(0.5 * (longitudLista + 1)) - 1
    q3_index = int(0.75 * (longitudLista + 1)) - 1

    q1 = listaOrdenada[q1_index]
    q2 = listaOrdenada[q2_index]
    q3 = listaOrdenada[q3_index]

    return q1, q2, q3


def RANGO(n_mayor, n_menor):
    # en la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
    valor_rango = n_mayor - n_menor
    return valor_rango


def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias


while True:
    numero_muestra = 0
    lista_muestras = []
    print("Ingrese las muestras una por una. Cuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        valor = input(f"Ingrese número de muestra {numero_muestra + 1}: ")
        if valor.isdigit():
            lista_muestras.append(int(valor))
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de las muestras")
                break
            else:
                print("Comando no válido, intente de nuevo.")
    
    print(lista_muestras)

    print("¿Qué desea conocer sobre esta lista?\n 1. MEDIA ARITMÉTICA.\n 2. MODA.\n 3. MEDIANA.\n 4. MÁXIMA.\n 5. MÍNIMA.\n 6. RANGO.\n 7. CUARTILES.\n 8. DESVIO ESTÁNDAR.\n 9. FRECUENCIA ABSOLUTA.")
    calculo = input("¿Qué desea calcular?: ")
    comando = int(calculo)
    
    if comando == 1:
        value = MEDIA(lista_muestras)
        print("Media Aritmética:", value)
    elif comando == 2:
        # Aquí podrías agregar la lógica para calcular la moda si es necesario
        value = "No implementado"
        print("Moda:", value)
    elif comando == 3:
        value = CALCULAR_MEDIANA(lista_muestras)
        print("Mediana:", value)
    elif comando == 4:
        value = max(lista_muestras)
        print("Máxima:", value)
    elif comando == 5:
        value = CALCULAR_MENOR(lista_muestras)
        print("Mínima:", value)
    elif comando == 6:
        value = RANGO(max(lista_muestras), CALCULAR_MENOR(lista_muestras))
        print("Rango:", value)
    elif comando == 7:
        q1, q2, q3 = CALCULAR_CUARTILES(lista_muestras)
        print("Cuartiles: Q1 =", q1, ", Q2 =", q2, ", Q3 =", q3)
    elif comando == 8:
        value = DESVIACION_ESTANDAR(lista_muestras)
        print("Desvío Estándar:", value)
    elif comando == 9:
        frecuencias = CALCULAR_FRECUENCIA_ABSOLUTA(lista_muestras)
        print("Frecuencia Absoluta:", frecuencias)
    else:
        print("Comando no válido.")
    
    continuacion = input("¿Desea volver a empezar? Y = si, N = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "N":
            break
        elif continuacion.upper() == "Y":
            print("Volvemos a empezar!")
        else:
            print("Comando no válido.")
    else:
        print("Comando no válido.")

# def MEDIA(lista):
#     media = sum(lista)/len(lista)
#     return media 

# def CALCULAR_MODA(lista):
#     frequencia= {}
#     for elemento in lista:
#         if elemento in frequencia:
#             frequencia[elemento] +=1
#         else:
#             frequencia[elemento] = 1
#     moda = None
#     maxFrequencia= 0
#     for elemento, frequencia in frequencia.items():
#         if frequencia>maxFrequencia:
#             moda=elemento
#             maxFrequencia=frequencia
              
#     return moda

# # calcular promedio(sumatoria de todos los datos / cantidad de datos)
# def CALCULAR_PROMEDIO(lista):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)

# # calcular desviacion estandar((sumatoria de todos los datos - prom)**2/cant de datos -1)
# def DESVIACION_ESTANDAR(lista):
#     n = len(lista)
#     if n <= 1:
#         return 0
#     promedio = CALCULAR_PROMEDIO(lista)
#     suma_resta_cuadrado = (sum(lista) - promedio) ** 2
#     desviacion = (suma_resta_cuadrado / (n -1)) ** 0.5
#     return desviacion 

# def CALCULAR_MEDIANA(lista):
#     listaOrdenada=sorted(lista)
#     longitudLista=len(listaOrdenada)
    
#     if longitudLista % 2 == 0:
#         medioIzq = listaOrdenada[longitudLista // 2 -1 ]
#         medioDer = listaOrdenada[longitudLista // 2 ]
#         mediana = (medioIzq + medioDer) / 2
#     else:
#         mediana = listaOrdenada [longitudLista // 2]
#         return mediana

# def CALCULAR_CUARTILES(lista):
#     listaOrdenada=sorted(lista)
#     longitudLista=len(lista)

#     q1_index= int(0.25 * (longitudLista + 1))
#     q2_index= int(0.5 * (longitudLista + 1))
#     q3_index= int(0.75 * (longitudLista + 1))

#     q1= listaOrdenada[q1_index]
#     q2= listaOrdenada[q2_index]
#     q3= listaOrdenada[q3_index]

#     return q1, q2, q3 

# def RANGO(n_mayor, n_menor):
#     # en la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
#     valor_rango = n_mayor - n_menor
#     return valor_rango

numero_muestra = 0
lista_muestras = []


while True:
    cambios = input("Desea realizar algun cambio? \n 1 = SI | 2 = NO: ")
    if cambios == 1:
        si = input("Que cambio desea realizar? 1 = eliminar | 2 = modificar | 3")



while True:    
    #Este print le permite al usuario seleccionar que tipo de informacion desea recibir de la lista de muestras
    # CATY, hay que hacer que esto sea mas util para el usuario (agregar numeros olvidados, que no se termine de una, etc) 
    print("¿Qué desea conocer sobre esta lista?\n 1. MEDIA ARITMÉRICA.\n 2. MODA.\n 3. MEDIANA. \n 4. MÁXIMA.\n 5. MÍNIMA.\n 6. RANGO.\n 7. CUARTILES.\n 8. DESVIO ESTANDAR")
    calculo = input("¿Qué desea calcular?: ")
    comando = int(calculo)
    if comando == 1:
        value = MEDIA(lista_muestras)
        print(value)
    elif comando == 2:
        value = 00000
        
    #Aca se evalua si se quiere seguir utilizando el programa o no
    # CATY, ver que va a hacer el programa en caso de escribir un comando no valido, en todo caso, hacer que cualquier letra signifique fin del programa 
    continuacion = input("¿Desea volver a empezar? Y = si, N = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "N":
            break
        elif continuacion.upper == "Y":
            print("Volvemos a empezar!")
        else:
            print("Comando no válido.")
    else:
        print("Comando no válido")
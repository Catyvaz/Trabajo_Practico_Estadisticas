import math
from Funciones import *

while True:
    print("******************************************")
    print("****      SOFTWARE DE ESTADISTICA     ****")
    print("****          VERSIÓN INICIAL         ****")
    print("******************************************")

    # Estas lineas son las que permiten que el usuario ingrese los datos, los cuales se almacenan en una lista, la cual se ordena de menor a mayor, y solo permite valores numéricos.
    lista_muestras = []
    lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
    numero_muestra = len(lista_muestras)
    #En pantalla se imprime la lista de los elementos dados por el usuario y la cantidad de elementos que se ingresaron
    print(lista_muestras)
    print(numero_muestra)
    
    # Este es el main del código, aca se ejecuta todo el programa y se hacen las llamadas al documento "Funciones", del cual extraemos las funciones necesarias   
    while True: #Este while le permite al usuario utilizar tantas veces quiera las opciones que se ofrecen
        #La variable respuesta le permite al usuario escribir el valor de que tipo de informacion desea recibir de la lista de muestras
        respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = FRECUENCIAS | 3 = Finalizar. \n ==> ")
        if int(respuesta) == 1:
            print("Seleccionaste < Medidas de Posición >")
            resultado = MEDIDAS_POSICION(lista_muestras)
        elif int(respuesta) == 2:
            print("Seleccionaste < Frecuencias >")
            #resultado = TABLAS_FRECUENCIAS(lista_muestras)

            lista_muestra_norep = SOLO_UN_ELEMENTO(lista_muestras)
            F_A = CALCULAR_FRECUENCIA_ABSOLUTA(lista_muestras)
            F_A_A = CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista_muestras)
            F_R = CALCULAR_FRECUENCIA_RELATIVA(lista_muestras)
            F_R_A = CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista_muestras)
            F_P = CALCULAR_FRECUENCIA_PORCENTUAL(lista_muestras)
            F_P_A = CALCULAR_FREC_PORCENTUAL_ACUMULADA(lista_muestras)

            print(F_A)
            print("Dato \t F_A \t F_A_A \t F_R \t F_R_A \t F_P \t F_P_A")
            for i in range(len(lista_muestra_norep)):
                n = lista_muestra_norep[i]
                print(f"{n} \t {F_A[(n)]} \t {F_A_A[n]} \t {F_R[i]} \t {F_R_A[i]} \t {F_P[i]} \t {F_P_A[i]} ")

        elif int(respuesta) == 3:
            print("Finalizando...")
            break
        else:
            print("Comando no válido, intente de nuevo")

    #Falta aclarar algunos aspectos de esta parte del código
    #Aca se evalua si se quiere seguir utilizando el programa o no. En caso de que si, se escribe la Y, en caso de que no, se ingresa cualquier valor.
    continuacion = input("¿Desea volver a empezar? Y = si, cualquier cosa = no : ")
    if continuacion.isalpha():
        if continuacion.upper() == "Y":
            print("Volvemos a empezar!")
        else:
            print("Fin del programa.")
            break
    else:
        print("Fin del programa.")
        break


#CATY terminar la funcionalidad de modificar la lista
# while True:
#     cambios = input("Desea realizar algun cambio? \n 1 = SI | 2 = NO: ")
#     if cambios == 1:
#         si = input("Que cambio desea realizar? 1 = eliminar | 2 = modificar | 3 = agregar")

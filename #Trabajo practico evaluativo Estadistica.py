from Funciones import *
import math

while True:
    print("******************************************")
    print("*****     SOFTWARE DE ESTADISTICA    *****")
    print("*****         VERSIÓN INICIAL        *****")
    print("******************************************")

    # Estas lineas son las que permiten que el usuario ingrese los datos, los cuales se almacenan en una lista, la cual se ordena de menor a mayor, y solo permite valores numéricos.
    lista_muestras = []
    lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
    numero_muestra = len(lista_muestras)
    #En pantalla se imprime la lista de los elementos dados por el usuario y la cantidad de elementos que se ingresaron
    print("Muestra: ", lista_muestras)
    print("Cantidad de datos: ", numero_muestra)
    
    # Este es el main del código, aca se ejecuta todo el programa y se hacen las llamadas al documento "Funciones", del cual extraemos las funciones necesarias   
    while True: #Este while le permite al usuario utilizar tantas veces quiera las opciones que se ofrecen
        #La variable respuesta le permite al usuario escribir el valor de que tipo de informacion desea recibir de la lista de muestras
        respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = MEDIDAS DE DISPERCIÓN  | 3 = FRECUENCIAS | 4 = Finalizar. \n ==> ")
        if int(respuesta) == 1:
            print("Seleccionaste < Medidas de Posición >")
            resultado = MEDIDAS_POSICION(lista_muestras)
        elif int(respuesta) == 2:
            print("Seleccionaste < Medidas de Disperción >")
            resultado = MEDIDAS_DISPERCION(lista_muestras)
        elif int(respuesta) == 3:
            print("Seleccionaste < Frecuencias >")
            resultado = TABLAS_FRECUENCIAS(lista_muestras)
        elif int(respuesta) == 4:
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
from Funciones import *

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

 
# esto seria lo unico que queda en el main, pero podemos dejar tambien las funciones que ordenan al input, hay que hablarlo
while True:    
    while True:
        #Este print le permite al usuario seleccionar que tipo de informacion desea recibir de la lista de muestras
        respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = FRECUENCIAS | 3 = Finalizar. \n ==> ")
        if int(respuesta) == 1:
            print("Seleccionaste < medidas de posición >")
            resultado = MEDIDAS_POSICION(lista_muestras)
        elif int(respuesta) == 2:
            print("Seleccionaste < frecuencias >")
            resultado = TABLAS_FRECUENCIAS(lista_muestras)
        elif int(respuesta) == 3:
            print("Finalizando...")
            break
        else:
            print("Comando no válido, intente de nuevo")

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
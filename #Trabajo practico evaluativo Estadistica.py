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

def MEDIDAS_POSICION(lista):
    comando = int(input("¿Que desea conocer sobre la lista?\n 1 = MEDIA ARITMÉTICA.\n 2 = MODA.\n 3 = MEDIANA.\n 4 = MÁXIMO.\n 5 = MINIMO.\n 6 = RANGO.\n 7 = DESVIO ESTANDAR.\n 8 = CUARTILES.\n ==>"))
    # if comando == 1:

def TABLAS_FRECUENCIAS(lista):
    comando = int(input("¿Que frecuencia desea conocer?\n 1 = ABSOLUTA. \n 2 = ABSOLUTA ACUMULADA.\n 3 = RELATIVA.\n 4 = RELATIVA ACUMULADA.\n 5 = PORCENTUAL.\n 6 = PORCENTUAL ACUMULADA.\n 7 = INTERVALOS.\ 8 = AMPLITUD DE INTERVALOS.\n ==> "))
        

while True:    
    #Este print le permite al usuario seleccionar que tipo de informacion desea recibir de la lista de muestras
    # CATY, hay que hacer que esto sea mas util para el usuario (agregar numeros olvidados, que no se termine de una, etc)
    respuesta = input("¿Que medidas desea conocer? 1 = MEDIDAS DE POSICIÓN | 2 = FRECUENCIAS: ")
    if int(respuesta) == 1:
        print("Seleccionaste < medidas de posición >")
        resultado = MEDIDAS_POSICION(lista_muestras)
    elif int(respuesta) == 2:
        print("Seleccionaste < frecuencias >")
        resultado = TABLAS_FRECUENCIAS(lista_muestras)


def CONTINUAR_PROGRAMA(valor):
    
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
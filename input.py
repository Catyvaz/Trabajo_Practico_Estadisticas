def RANGO(n_mayor, n_menor):
    # en la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
    valor_rango = n_mayor - n_menor
    return valor_rango

while True:
    numero_muestra = 0
    lista_muestras = []
    print("Ingrese las muestras una por una. Cuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        # Se ingresan los numeros uno por uno y mediante el "numero_muestra + 1" se va incrementando en la terminal el numero que se ingresa.
        valor = input(f"Ingrese número de muestra {numero_muestra + 1}: ")
        # Aca se evalua si el elemento ingresado es de valor numerico. 
        # Si es un valor numerico, se lo agrega a la lista "lista_muestras".
        # Si el valor es NO numerico, se evalua; si es la palabra "FIN" no se desean agregar mas números a la lista, si es una letra random marca no valido y deja volver a intentar.
        # CATY, tratar de hacer las lineas complejas en funciones reutilizables. 
        if valor.isdigit():
            lista_muestras.append(valor)
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de las muestras")
                break
            else:
                print("Comando no válido, intente de nuevo.")
    print(lista_muestras)
    
    #Este print le permite al usuario seleccionar que tipo de informacion desea recibir de la lista de muestras
    # CATY, hay que hacer que esto sea mas util para el usuario (agregar numeros olvidados, que no se termine de una, etc) 
    print("¿Qué desea conocer sobre esta lista?\n 1. MEDIA ARITMÉRICA.\n 2. MODA.\n 3. MEDIANA. \n 4. MÁXIMA.\n 5. MÍNIMA.\n 6. RANGO.\n 7. CUARTILES.\n 8. DESVIO ESTANDAR")

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
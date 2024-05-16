while True:
    numero_muestra = 0
    lista_muestras = []
    print("Ingrese las muestras una por una. Cuando ya no desee agregar más, coloque la palabra FIN")
    while True:
        valor = input(f"Ingrese número de muestra {numero_muestra + 1}: ")
        if valor.isdigit():
            lista_muestras.append(valor)
            numero_muestra += 1
        elif valor.isalpha():
            if valor.upper() == "FIN":
                print("Fin de las muestras")
                break
            else:
                print("Comando no válido, intente de nuevo.")
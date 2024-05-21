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
def Media (SumaDatos,CantDatos):
    Media = SumaDatos/CantDatos
    print("La media de su muestra es: ", Media)


#El usuario ya cargo todos los datos
Media(SumaDatos,CantDatos)

#kdkdk

'''
def calcular_min(lista):
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo   

num_str = input("Ingrese los números separados por como: ")
numeros = [float(num) for num in num_str.split(",")]

minimo = calcular_min(numeros)
print(f"El mínimo es: {minimo})
'''
#1° calcular promedio(sumatoria de todos los datos / cantidad de datos)
def calcular_promedio(datos):
    if len(datos) == 0:
        return 0
    return sum(datos) / len(datos)

#2° calcular desviacion estandar((sumatoria de todos los datos - prom)**2/cant de datos -1)
def desviacion_estandar(datos):
    n = len(datos)
    if n <= 1:
        return 0
    promedio = calcular_promedio(datos)
    suma_resta_cuadrado = (sum(datos) - promedio) ** 2
    desviacion = (suma_resta_cuadrado / (n -1)) ** 0.5
    return desviacion 

#desviacion = desviacion_estandar(lista)
#print(desviacion) 
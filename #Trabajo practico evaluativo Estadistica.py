#Trabajo practico evaluativo Estadisticas y probabilidad

'''PAUTAS
DATOS TIPO FLOAT TODOS
La longitud de la muestra la determina el usuario ingresando por teclado
datos almacenados para la muestra almacenados en vectores (LOS QUE INGRESA EL USUARIO)
El vector se recorre para determinar la mediana
EL Programa primero debe determinar las medidas de posicion para poder obtener las medidas de dispersion 
Que se puedan cargar los datos de la muestra de forma desordenada y que el programa los ordene de menor a mayor
Navegacion del usuario mediante numeros ej: 1) para ver la mediana 2) para ver la moda ... 5) para volver atras 

Determinar:
Medidas de posicion 
*media suma de todos los datos / la cantidad de datos
mediana la mediana es el valor que separa la muestra en un 50% a la izquierda y un 50% a la derecha. En caso de par, se suman los valores centrales y se los divide por 2
moda el valor que mas se repite dentro de la muestra
cuartiles se separa en porcentajes del 25%
media recortada es el numero de datos por el porcentaje a recortar / 100 

medidas de dispersion
Varianza
Desviacion estandard 
Frecuencia absoluta es la cantidad de veces que aparece un dato en la muestra
Frecuencia relativa es la proporcion de veces que aparece ese dato respectoa al total FA/N'''

def Media (SumaDatos,CantDatos):
    Media = SumaDatos/CantDatos
    print("La media de su muestra es: ", Media)


#El usuario ya cargo todos los datos
Media(SumaDatos,CantDatos)

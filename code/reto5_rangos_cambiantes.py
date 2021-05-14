""" Reto 5 - Rangos cambiantes

Ejercicios realizados por Orlando Chaparro. 
https://platzi.com/p/orlandochr

Para este reto final juguemos con números.
En tu programa pide al usuario ingresar 3 números:
un límite inferior, un límite superior y uno de comparación.

Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

En caso de estar por debajo del inferior o arriba del superior, 
también muéstralo en pantalla y pide ingresar otro número para repetir el proceso. """


def comparar_rango_numreros(numero_1,numero_2,comparador):
    finalizar = False
    if numero_1 >= numero_2:
        limite_superior = numero_1
        limite_inferior = numero_2
    elif numero_1 < numero_2:
        limite_superior = numero_2
        limite_inferior = numero_1
 
    if comparador >= limite_inferior and comparador <= limite_superior:
        resultado = "El numero está Dentro del rango Inferior - Superior"
        finalizar = True
    else:
        resultado = "El numero está Fuera del rango Inferior - Superior"
        finalizar = False
    
    return [resultado,finalizar]
finalizar = False
while not finalizar:
    nro_1 = int(input("Ingresar nro :")) 
    nro_2 = int(input("Ingresar nro :")) 
    compara = int(input("Ingresar nro :")) 
    
    resultado,finalizar = comparar_rango_numreros(nro_1,nro_2,compara)
    print(resultado)
    print("Rango " +str(nro_1) + " - " + str(nro_2) + " Comparador = " + str(compara))
print("fin")

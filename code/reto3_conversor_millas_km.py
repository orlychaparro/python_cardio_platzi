""" Reto 3 - Conversor de millas a kilómetros

Ejercicios realizados por Orlando Chaparro. 
https://platzi.com/p/orlandochr

Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. Para no estar repitiendo este cálculo escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.
Toma en cuenta que en cada milla hay 1.609344 Km
Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.¶

 """

def conversor_millas_km(valor_a_convertir, tipo_conversion):
    valor_km    = 0.999997
    valor_milla = 1.609344
    
    if tipo_conversion == '1':
        tipo_conversion = 'Km'
        operacion = 'Millas a Kilómetros'
        conversion = valor_a_convertir * valor_km
        
    if tipo_conversion == '2':
        tipo_conversion = 'Millas'
        operacion = 'Kilómetros a Millas'
        conversion = valor_a_convertir * valor_milla
                
    unidad_medida = tipo_conversion    
    return [operacion,conversion,unidad_medida]
valor_ingresado = float(input ("Ingresa el valor a convertir :"))
tipo_conversion_ingresado = input ("""
 elegir el tipo de conversion deseado: 
 1 - Millas a Kilometros
 2 - Km`s a Millas
""")

operacion,conversion,unidad_medida = conversor_millas_km(valor_ingresado,tipo_conversion_ingresado)

print( str(valor_ingresado)+ ' ' +  operacion + ' ' + str(conversion) + ' '+ unidad_medida )
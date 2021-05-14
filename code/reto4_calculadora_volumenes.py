""" Reto 4 - Calculadora de volúmenes

Ejercicios realizados por Orlando Chaparro. 
https://platzi.com/p/orlandochr

Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.
Recuerda que la base del cilindro es un círculo y necesitarás calcular su área.
Aplica las fórmulas en tu programa recibiendo datos como altura y radio.
Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.¶
 """

def calcular_area_figura_geometrica(p_tipo_figura_geometrica,p_altura,p_radio):
    pi = 3.1416
    
    if p_tipo_figura_geometrica == '1':
        figura = 'Cilindro'
        volumen_figura_geometrica = (pi * p_radio**2)*p_altura
        
    if p_tipo_figura_geometrica == '2':
        figura = 'Pirámide'
        volumen_figura_geometrica = (p_radio*p_altura)/3
    if p_tipo_figura_geometrica == '3':
        figura = 'Cono'
        volumen_figura_geometrica = (pi*p_radio**2*p_altura)/3
           
    return [figura,volumen_figura_geometrica]

tipo_figura_seleccionada = input(""" Ingrese el tipo de Figura Geometrica 
1- Cilindro
2- Pirámide
3- Cono""")

if tipo_figura_seleccionada == '1':
    valor_1_texto = 'Altura'
    valor_2_texto = 'Radio'
if tipo_figura_seleccionada == '2':
    valor_1_texto = 'Altura'
    valor_2_texto = 'Area Base'  
if tipo_figura_seleccionada == '3':
    valor_1_texto = 'Altura'
    valor_2_texto = 'radio'  

altura_seleccionada = float(input("ingrese "+ valor_1_texto + " :"))
radio_seleccionada = float(input("Ingrese "+ valor_2_texto + " :"))
figura, volumen_figura_geometrica = calcular_area_figura_geometrica(tipo_figura_seleccionada,altura_seleccionada,radio_seleccionada)
print('el valor del Volumen de la Figura ' + figura + ' es ' + str(volumen_figura_geometrica))

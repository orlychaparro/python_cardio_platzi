
""" Reto 1 - Área de un triángulo

Ejercicios realizados por Orlando Chaparro. 
https://platzi.com/p/orlandochr

Es momento de poner ese conocimiento a la práctica. El área de un triángulo se describe de la siguiente manera:
𝐴=(𝑏∗ℎ)/2. 

Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.
Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno.
 """

# Definición de Funciones
def calcular_area_triangulo(p_base, p_altura):
    area_triangulo = (p_base * p_altura)/2
    return area_triangulo

def tipo_triangulo(p_base, p_altura,lado_c):
    if p_base == p_altura and p_base == lado_c:
        tipo_triangulo = "Todos los Lados iguales - Triángulo Equilatero"
    elif p_altura == lado_c and p_altura != p_base :
        tipo_triangulo = "Dos Lados iguales - Triángulo Isosceles"
    elif p_altura != lado_c and p_altura != p_base :
        tipo_triangulo = "Todos los Lados desiguales - Triángulo Escaleno"
    return tipo_triangulo

nro_base =   float(input("Ingresar el Número Base      :"))
nro_altura = float(input("Ingregar el Número de Altura :"))
lado_c= float(input("Ingregar el valor del lado restante del triángulo :"))
valor_area = calcular_area_triangulo(nro_base,nro_altura)
print("el Area del Triángulo es ")
print(str(valor_area))
print(tipo_triangulo(nro_base,nro_altura,lado_c))

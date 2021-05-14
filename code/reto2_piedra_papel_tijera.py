""" Reto 2 - Piedra, papel o tijera

Ejercicios realizados por Orlando Chaparro. 
https://platzi.com/p/orlandochr

Escribe un programa que reciba como parámetro
“piedra”, “papel”, o “tijera”
y determine si ganó el jugador 1 o el jugador 2.
Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.
Ejemplo:
ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2
 """

def seleccion_opcion_jugador(p_opcion_jugador):
    opciones_piedra_papel_tijera = {'1' : 'Piedra', '2' : 'Papel', '3': 'Tijera' }
    opcion_seleccionada = opciones_piedra_papel_tijera[p_opcion_jugador]
    return opcion_seleccionada

def piedra_vs_papel_vs_tijera(p_jugador1,p_jugador2):
       
    msg_empate = "El resultado es empate"
    msg_gana_1 = "El ganador es el jugador 1"
    msg_gana_2 = "El ganador es el jugador 2"
    
    if p_jugador1 == "Piedra":
        if p_jugador2 == 'Piedra':
            resultado = '0'
            msg = msg_empate
        elif p_jugador2 == 'Papel':
            resultado = '2'
            msg = msg_gana_2
        else :
            resultado = '1'
            msg = msg_gana_1
            
    if p_jugador1 == "Papel":
        if p_jugador2 == 'Piedra':
            resultado = '1'
            msg = msg_gana_1
        elif p_jugador2 == 'Papel':
            resultado = '0'
            msg = msg_empate
        else :
            resultado = '2'
            msg = msg_gana_2
    if p_jugador1 == "Tijera":
        if p_jugador2 == 'Piedra':
            resultado = '2'
            msg = msg_gana_2
        elif p_jugador2 == 'Papel':
            resultado = '1'
            msg = msg_gana_1
        else :
            resultado = '0'
            msg = msg_empate
    return [resultado,msg]    
partidas_ganadas = 0
msg_final = ""
jugador1_ganadas = 0
jugador2_ganadas = 0
finalizar_juego = False
while not finalizar_juego:
    jugador_1 = input(""" Seleccione una opcion 
    1 - Piedra
    2 - Papel
    3 - Tijera
    : """)
    jugador_2 = input(""" Seleccione una opcion 
    1 - Piedra
    2 - Papel
    3 - Tijera
    : """)
    jugador_1 = seleccion_opcion_jugador(jugador_1)
    jugador_2 = seleccion_opcion_jugador(jugador_2)

    resultado,msg = piedra_vs_papel_vs_tijera(jugador_1,jugador_2)
    
    print("Jugador 1  x Jugador 2          Resultado")
    print("  " + jugador_1 + " " + "  -   " + jugador_2 + ' -   ' + "" + msg )
    
    if resultado == '1':
        jugador1_ganadas +=1
        if jugador1_ganadas == 3:
            finalizar_juego = True
            msg_final = "Con tres juegos victoriosos el Ganador es el Jugador 1"
            
    if resultado == '2':
        jugador2_ganadas +=1
        if jugador2_ganadas == 3:
            finalizar_juego = True
            msg_final = "Con tres juegos victoriosos el Ganador es el Jugador 2"
    print(resultado)
    print(jugador1_ganadas)
    print(jugador2_ganadas)
print(finalizar_juego)
print(msg_final)   

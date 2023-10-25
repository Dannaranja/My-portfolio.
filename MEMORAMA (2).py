import random
def lista_cartas(cartas):
    lista_inicial=[]
    for i in range(cartas):
        lista_inicial.append(i+1)
        lista_inicial.append(i+1)
    random.shuffle(lista_inicial)
    return lista_inicial

def matriz_tablero_cartas(lista):
    matriz_cartas=[]
    submatriz_cartas=[]
    cnt=0
    for i in range(len(lista)):
        if cnt==5:
            submatriz_cartas.append(lista[i])
            matriz_cartas.append(submatriz_cartas)
            submatriz_cartas=[]
            cnt=0
        else:
            submatriz_cartas.append(lista[i])
            cnt=cnt+1
    return matriz_cartas

def matriz_tablero_asteriscos(num_asteriscos):
    matriz_asteriscos=[]
    for i in range(num_asteriscos):
        submatriz_asteriscos=[]
        for j in range(num_asteriscos):
            submatriz_asteriscos.append("*")
        matriz_asteriscos.append(submatriz_asteriscos)
    return matriz_asteriscos

def construir_tablero(contenido_tablero):
    print("    {:^4} {:^4} {:^4} {:^4} {:^4} {:^4}".format(1,2,3,4,5,6))
    print('  |__________________\n')  
    for i in range(len(contenido_tablero)):
        print(i+1, "|", end=' ' )
        for j in range(len(contenido_tablero[i])):
            print("{0:^4}".format(contenido_tablero[i][j]), end=' ')
        print('    \n')    

def fila_columna(matriz,numeros_usados):
    try:
        repeticion=0
        fila=int(input("Seleccione una fila: "))
        columna=int(input("Seleccione una columna: "))
        if not 1<=fila<=6 or not 1<=columna<=6:
            print("Elige coordenadas entre 1 y 6")
        elif matriz[fila-1][columna-1] in numeros_usados:
            print("Elige otra casilla")
        else:
            repeticion=1
        return fila,columna,repeticion
    except:
        print("Ingresa un número entero")
        return 0,0,0
    
def jugar(matriz,numeros_usados,contenido_tablero):
    repeticion=0
    acierto=0
    puntos_agregados=0
    while repeticion==0:
        fila1,columna1,repeticion=fila_columna(matriz,numeros_usados)
    print("La casilla tiene el número ",matriz[fila1-1][columna1-1])
    repeticion=0
    while repeticion==0:
        fila2,columna2,repeticion=fila_columna(matriz,numeros_usados)
        if fila2==fila1 and columna2==columna1:
            print("Elige dos casillas distintas")
            repeticion=0
    print("La casilla tiene el número ",matriz[fila2-1][columna2-1])
    if matriz[fila1-1][columna1-1]==matriz[fila2-1][columna2-1]:
        print("\n ¡Le atinaste! \n")
        contenido_tablero[fila1-1][columna1-1]=matriz[fila1-1][columna1-1]
        contenido_tablero[fila2-1][columna2-1]=matriz[fila2-1][columna2-1]
        numeros_usados.append(matriz[fila1-1][columna1-1])
        puntos_agregados+=1
        acierto=1
    return puntos_agregados,acierto,numeros_usados,contenido_tablero

def main():
    numeros_usados=[]
    print("MEMORAMA")
    lista=lista_cartas(18)
    matriz=matriz_tablero_cartas(lista)
    asteriscos=matriz_tablero_asteriscos(6)
    construir_tablero(matriz)
    construir_tablero(asteriscos)
    turnojugador=1
    puntos_jugador1=0
    puntos_jugador2=0
    nombre_jugador1=input("Introduce el nombre del jugador 1: ")
    nombre_jugador2=input("Introduce el nombre del jugador 2:")
    while True:
        if len(numeros_usados)==18:
            print("\n", nombre_jugador1," Logró ",puntos_jugador1," puntos")
            print(nombre_jugador2," Logró ",puntos_jugador2," puntos \n")
            if puntos_jugador1==puntos_jugador2:
                print("\n Empate")
            elif puntos_jugador1>puntos_jugador2:
                print("\n Ganó ",nombre_jugador1)
            else:
                print("\n Ganó ",nombre_jugador2)
            break
        elif turnojugador==1:
            print("\n Turno de",nombre_jugador1, "\n")
            puntos_agregados,acierto,numeros_usados,asteriscos=jugar(matriz,numeros_usados,asteriscos)
            puntos_jugador1+=puntos_agregados
            print("Logró",puntos_jugador1,"puntos")
            if acierto!=1:
                turnojugador+=1
        else:
            print("\n Turno de",nombre_jugador2, "\n")
            puntos_agregados,acierto,numeros_usados,asteriscos=jugar(matriz,numeros_usados,asteriscos)
            puntos_jugador2+=puntos_agregados
            print("Logró",puntos_jugador2,"puntos")
            if acierto!=1:
                turnojugador-=1
        construir_tablero(asteriscos)
main()
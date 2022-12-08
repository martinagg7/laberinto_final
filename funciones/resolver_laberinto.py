
from laberintof import laberintof
#esta funcion recorre el laberinto y devuelve una lista con los movimientos que hay que hacer para salir del laberinto
#abajo explicacion de cómo funciona
def resolver_laberinto():
    laberinto_recorrer=laberintof()
    x=0 #posicion vertical
    y=0 #posicion horizontal
    movimientos=[]
    while (x,y)!=(4,4):
        if y-1<0 and laberinto_recorrer [x][y+1]=='x':
            movimientos.append('↓')
            x+=1
        elif  laberinto_recorrer[x+1][y]=='x' and laberinto_recorrer[x][y+1]==' ':
            movimientos.append('→')
            y+=1
        elif y+1>4:
            movimientos.append('↓')
            x=x+1
        elif y-1>0 and laberinto_recorrer[x][y+1]=='x':
            movimientos.append('↑')
            x=x-1
        elif laberinto_recorrer[x-1][y]=='x'and laberinto_recorrer[x][y+1]==' ' and y+1<4:
            movimientos.append('→')
            y+=1

    return movimientos

#FUNCION RECORRE EL LABERINTO:
#En primer lugar llamo 'x' a las coordenadas verticales y 'y 'a las coordenadas horizontales
#(1)Si tengo un borde a la izquierda y un muro a la derecha , entonces me muevo hacia abajo y añado uno a las x
#(2)Si tengo un muro debajo y no hay muro a la derecha, ento ces el moviento que hago es derecha y añado uno a la y
#(3)Si tengo un borde a la dercha ,bajo y añado uno  las x
#(4)Si no hay borde a la izquierda y hay un muro a la derecha el moviento es arriba y restar uno a las x
#(5)Si hay un muro arriba hy no hay un muro a la derecha ni borde a la dercha, me desplazo hacia la derecha y añado uno a las y


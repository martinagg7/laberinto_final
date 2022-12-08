from dibujo_laberinto import *
from resolver_laberinto import *
##BLOQUE PRINCIPAL####
if __name__=="__main__":
    for i in range(5):
        print(laberintof()[i])
print('MOVIENTOS PARA SALIR DEL LABERINTO:')
print(resolver_laberinto())
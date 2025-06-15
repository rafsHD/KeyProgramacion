'''
Clase:        Fortalecimiento lógico clase 10
Tema:         Fortalecimiento lógico 
Ejercicio:    10.2.1
Descripción:  Diagonal principal y secundaria 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-06-14
Estado:       [Terminado]   

'''

dimension = int(input("Ingrese la dimension de la matriz: "))

numeros = list(range(1, dimension*dimension + 1))

matriz = []
for i in range (dimension):
    filas = numeros[i*dimension : (i+1)*dimension]
    matriz.append(filas)

    
print(matriz)
    
    
    

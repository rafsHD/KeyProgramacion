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

matriz = []

for i in range (dimension):
    filas = []
    for j in range(dimension):
        filas.append(i)
    matriz.append(filas)
    
print(matriz)
    
    
    

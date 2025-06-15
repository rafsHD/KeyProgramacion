'''
Clase:        Fortalecimiento lógico clase 10
Tema:         Fortalecimiento lógico 
Ejercicio:    10.2.1
Descripción:  Diagonal principal y secundaria 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-06-14
Estado:       [Terminado]   

'''

def obtener_valores(valores):
    print("Ingrese cada fila separando los números con comas:")
    return [
        list(map(int, input(f"Fila {i + 1}: ").replace(' ', '').split(',')))
        for i in range(valores)
    ]
    
def obtener_diagonales(matriz):
    n = len(matriz)
    d1 = [matriz[i][i] for i in range(n)]
    d2 = [matriz[i][n - i - 1] for i in range(n)]
    return d1, d2

dimensiones = int(input("Ingrese la dimensión de la matriz: "))
matriz = obtener_valores(dimensiones)
diag1, diag2 = obtener_diagonales(matriz)

print(f"Diagonal principal: {diag1}")
print(f"Diagonal secundaria: {diag2}")
    
    
print(matriz)
    
    
    

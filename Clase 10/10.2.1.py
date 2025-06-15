'''
Clase:        Fortalecimiento lógico clase 10
Tema:         Fortalecimiento lógico 
Ejercicio:    10.2.1
Descripción:  Diagonal principal y secundaria 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-06-14
Estado:       [Terminado]   

'''

def obtener_matriz(n):
    print("Ingrese cada fila separando los números con comas:")
    return [
        list(map(int, input(f"Fila {i + 1}: ").replace(' ', '').split(',')))
        for i in range(n)
    ]
    

    
    
print(matriz)
    
    
    

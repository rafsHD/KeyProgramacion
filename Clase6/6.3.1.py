'''
Clase:        Fortalecimiento lógico clase 5
Tema:         Fortalecimiento lógico 
Ejercicio:    5.4.1 
Descripción:  Numero lider 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-30
Estado:       [Terminado]   
'''

entrada = [1, 65, 1, 1, 16, 5, 6, 8, 6, 4]
print(f"Entrada: {entrada}")
lider = []

for i in entrada: 
    entrada.remove(max(entrada))
    lider.append(max(entrada))
    
print(f"los numeros lideres son: {lider}")

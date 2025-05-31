'''
Clase:        Fortalecimiento lógico clase 5
Tema:         Fortalecimiento lógico 
Ejercicio:    5.4.1 
Descripción:  Numero lider 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-30
Estado:       [Terminado]   
'''

entrada = input("Escriba una serie de numeros: ")
entrada = entrada.split()
print(max(entrada))



print(f"Entrada: {entrada}")
lider = []

for i in entrada:
    lider.append(max(entrada))
    entrada.remove(max(entrada))
    
    
    
    
print(f"los numeros lideres son: {lider}")

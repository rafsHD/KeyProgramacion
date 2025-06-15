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
entrada = list(map(int, entrada))
print(max(entrada))
print(f"Entrada: {entrada}")
max = 0

lider = []

for i in reversed(entrada):
    if i > max:
        lider.append(i)
        max = i
        
lider.reverse()
    
print(f"los numeros lideres son:", *lider)
    
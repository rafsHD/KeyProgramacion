'''
Clase:        Fortalecimiento lógico clase 3
Tema:         Fortalecimiento lógico 
Ejercicio:    5.4.1 y 5.4.2
Descripción:  Numero secreto y Sumador de valores posicionales

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-16
Estado:       [Terminado]   
'''

print("Ejercicio 5.4.2")

numero = input(("Esribe un numero al azar: "))      

for i in numero:
    i = int(i)
    i += [i] + 1
    
print(i)
        
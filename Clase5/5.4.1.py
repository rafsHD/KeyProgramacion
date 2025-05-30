'''
Clase:        Fortalecimiento lógico clase 5
Tema:         Fortalecimiento lógico 
Ejercicio:    5.4.1 
Descripción:  Numero secreto 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-30
Estado:       [Terminado]   
'''
import random

print("Ejercicio 5.4.1")

n = random.randint(1,100)

acierto = True

while acierto:
    intento = int(input("Ingrese un numero: "))
    if intento < n:
        print("El numero secreto es mayor!")
    elif intento > n:
        print("El numeor secreto es menor!")
    elif intento == n:
        print(f"Felicidades! Has encontrado el numero secreto! ({n})")
        acierto == False
        break
        

'''
Clase:        Fortalecimiento lógico clase 6
Tema:         Fortalecimiento lógico 
Ejercicio:    6.2.1
Descripción:  Eliminando valores dupliados

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-30
Estado:       [Terminado]   
'''

lista = input("Ingrese una serie de numeros: ")
lista = lista.split()

singulares = []

for i in lista:
    singulares.append(i)
    if singulares.count(i) > 1:
        singulares.remove(i)  
        
singulares_output = str(singulares)
print(singulares_output)
    
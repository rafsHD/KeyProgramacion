'''
Clase:        Fortalecimiento lógico clase 5
Tema:         Fortalecimiento lógico 
Ejercicio:    5.4.2
Descripción:  Sumador de valores posicionales

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-16
Estado:       [Terminado]   
'''

print("Ejercicio 5.4.2")

numero = input(("Esribe un numero al azar: "))    

igualdad = True  

while igualdad: 
        original = numero 
        if len(numero) > 1:
            sumatorias = []
        for digito in numero: 
            digito = int(digito)
            sumatorias.append(digito)
        numero = str(sum(sumatorias))
        if len(numero) == 1:
            print (f"La sumatoria de {original} equivale a {numero}")
            igualdad = False
        
            
            
print(f"La sumatoria de los digitos es: {numero}")
        
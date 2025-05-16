'''
Clase:        Fortalecimiento lógico clase 2
Tema:         Fortalecimiento lógico 
Ejercicio:    Ver si la contrasña es segura, calculadora de impuestos y numero magico 
Descripción:  Contraseña, Calculadora de impuestos y numero magico 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-16
Estado:       [Terminado]   
'''

password = "Abcd1234"
numero = False
mayuscula = False 

for i in password:
    if i.isupper() and len(password) >= 8:
        mayuscula = True 
    if i.isdigit():
        numero = True 
    
if mayuscula and numero:
    print("Contrasena valida")
    
'---------------------------------------------------------'
u = float(201)
if u <= 100:
    print("No aplican impuestos")
elif u <= 101 and u <= 200:
    print(f"El total de impuestos a pagar es {u*0.5}$")
else: 
    print(f"El total de impuestos a pagar es {u*0.7}$")
    
'---------------------------------------------------------'

n = int(input("Ingrese un numero: "))
if n % 7 == 0 and n%5 != 0:
    print("Es un numero magico!")

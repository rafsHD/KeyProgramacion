'''
Clase:        Fortalecimiento lógico clase 2
Tema:         Fortalecimiento lógico 
Ejercicio:    Ver si la contrasña es segura, calculadora de impuestos y numero magico 
Descripción:  Contraseña, Calculadora de impuestos y numero magico 

Autor:        Jose Rafael Santos Reyes
Fecha:        2025-05-16
Estado:       [Terminado]   
'''

'---------------------------------------------------------'
print("EJERCICIO 1")
cuenta = int(input("Ingrese el monto de la cuenta: "))
propina = cuenta*0.1

print(f"Total de la cuenta: {cuenta}$ \nPropina: {propina}$\n Total de la cuenta con propina: {cuenta+propina}$")

'---------------------------------------------------------'
print("EJERCICIO 2")
nombre1 = input("Primer nombre: ")
nombre2 = input("Segundo nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

print(f"El correo que se debe asignar al usuario ingresado es \n{nombre1}.{apellido1}@keyinstitute.edu.sv")

'---------------------------------------------------------'
print("EJERCICIO 4")
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

print("EJERCICIO 5")
u = float(201)
if u <= 100:
    print("No aplican impuestos")
elif u <= 101 and u <= 200:
    print(f"El total de impuestos a pagar es {u*0.5}$")
else: 
    print(f"El total de impuestos a pagar es {u*0.7}$")
    
'---------------------------------------------------------'

print("EJERCICIO BONUS (6)")
n = int(input("Ingrese un numero: "))
if n % 7 == 0 and n%5 != 0:
    print("Es un numero magico! :D")
else: 
    print("No es un numero magico :(")

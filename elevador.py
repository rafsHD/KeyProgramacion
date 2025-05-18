print("Ejercicio Bonus 2.5.1")

while True:
    n = int(input("Bienvenido, actualmente se encuentra en el lobby\n A que piso desea ir?\n \n1.S3 \n2.S2 \n3.S1 \n4. Lobby \n5. Primer piso \n6. Segundo Piso \n7. Tercer piso\n"))

    elevadorA = 2
    elevadorB = 7
    
    difA = abs(elevadorA - n)
    difB = abs(elevadorB - n)
    


    if (difA) > (difB):
        print("Llamando al elevador B...")
    elif(difA) < (difB):
        print("Llamando al elevador A...")
    else:
        print("Llamando al elevador A...")
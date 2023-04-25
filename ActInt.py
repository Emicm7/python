import random
import matplotlib.pyplot as plt
import numpy as np

class Juego:
    def jugarPPT(play):
        opciones = ["piedra", "papel", "tijera"]
        usuario = input("Elige piedra, papel o tijera: ").lower()
        computadora = random.choice(opciones)

        print(f"Vos elegiste {usuario}, y la computadora eligio {computadora}.")

        if usuario == computadora:
            print("Es un empate!")
        elif usuario == "piedra":
            if computadora == "papel":
                print("La computadora te ha ganado!")
            else:
                print("Has ganado!")
        elif usuario == "papel":
            if computadora == "tijera":
                print("La computadora te ha ganado!")
            else:
                print("Has ganado!")
        elif usuario == "tijera":
            if computadora == "piedra":
                print("La computadora te ha ganado!")
            else:
                print("Has ganado!")
        else:
            print("Eleccion incorrecta, por favor elige piedra, papel o tijera.")



    def jugarNRO(play):
        numero_a_adivinar = random.randint(1, 50)
        num_intentos = 5

        print("¡Adivina el número entre 1 y 50!")
        while num_intentos > 0:
            numero_usuario = int(input("Ingresa un número: "))

            if numero_usuario == numero_a_adivinar:
                print("¡Felicitaciones! Adivinaste el número.")
                break
            elif numero_usuario < numero_a_adivinar:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            numero_computadora = random.randint(1, 50)
            print("La computadora piensa que el número es:", numero_computadora)
            if numero_computadora == numero_a_adivinar:
                print("¡La computadora adivinó el número!")
                break

            num_intentos -= 1
            print("Intentos restantes:", num_intentos)

        if num_intentos == 0:
            print("Se acabaron los intentos. El número a adivinar era:", numero_a_adivinar)
    

    def jugarDADO(play):
        dado = random.randint(1, 6)
        print("El valor del dado es:", dado)


    def jugarGRAF(play):
        funcion = input("Ingresa una función matemática (utiliza la variable x): ")
        funcionDos = input("Ingresa una función matemática (utiliza la variable x): ")
        funcionTres = input("Ingresa una función matemática (utiliza la variable x): ")

        x = np.arange(-10, 10, 0.1)

        y1 = eval(funcion)
        y2 = eval(funcionDos)
        y3 = eval(funcionTres)

        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.plot(x, y3)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico de la función')

        plt.show()
        
            
juego = Juego()
print("Bienvenido")
while(True):
    print("""Que quieres hacer? 
    1) Jugar Piedra, Papel o Tijera contra la computadora
    2) Adivinar un numero compitiendo contra la computadora
    3) Tirar un dado
    4) Graficar una funcion matematica
    5) Salir""")

    opcion = input()
    if opcion == "1":
        juego.jugarPPT()
    elif opcion == "2":
        juego.jugarNRO()
    elif opcion == "3":
        juego.jugarDADO()
    elif opcion == "4":
        juego.jugarGRAF()
    elif opcion == "5":
        print("Muchas Gracias por jugar! Nos Vemos!")
        break    
    else:
        print("algo ha salido mal")


import random

posicion = 0
llave_encontrada = False
vida = 3

habitaciones = ["Entrada", "Cocina", "Sala de estar", "Sótano", "Ático"]
objetos = ["nada", "calabaza", "esqueleto", "fantasma", "vampiro"]
random.shuffle(objetos) 


def mostrar_descripcion():
    print(f"\n🔎 Estás en la {habitaciones[posicion]}.")
    print(f"Encuentras {objetos[posicion]}... ", end="")
    if objetos[posicion] == "vampiro":  
        global vida
        vida -= 1
        print("🧛‍♂️ ¡El vampiro te ha mordido y pierdes 1 punto de vida! 🩸")
        print(f"❤️ Te quedan {vida} puntos de vida")
        if vida == 0:
            print("💀 Has perdido toda tu vida. ¡Juego terminado! 💀")
            exit()
    elif objetos[posicion] == "calabaza":
        print("🎃 Una calabaza")
    elif objetos[posicion] == "esqueleto":
        print("💀 Un esqueleto que te observa silenciosamente")
    elif objetos[posicion] == "fantasma":
        print("👻 Un fantasma flotando a tu alrededor...")
    elif objetos[posicion] == "nada":
        print("🤔 No encuentras nada interesante aquí")

def interactuar_con_objeto():
    global llave_encontrada
    if objetos[posicion] == "fantasma":
        llave_encontrada = True
        print("🔑👻 Encontraste al fantasma que te va a dar la llave mágica para escapar!")
    elif objetos[posicion] == "calabaza":
        print("🎃 La calabaza parece inofensiva")
    elif objetos[posicion] == "esqueleto":
        print("💀 El esqueleto no hace ningún movimiento")
    elif objetos[posicion] == "nada":
        print("🤷 No hay nada interesante aquí")

def moverse():
    global posicion
    eleccion = input("¿Quieres avanzar (A), retroceder (R) o quedarte (Q)? ").lower()
    if eleccion == 'a' and posicion < len(habitaciones) - 1:
        posicion += 1
        print("🚶 Avanzas hacia la siguiente habitación...")
    elif eleccion == 'r' and posicion > 0:
        posicion -= 1
        print("🔙 Regresas a la habitación anterior...")
    elif eleccion == 'q':
        print("⏳ Decides quedarte en esta habitación.")
    else:
        print("🚫 No puedes moverte en esa dirección")


def juego():
    print("🎃 Bienvenido(a) a 'La Casa Embrujada' 🦇")
    print("🏠 Una de las habitaciones tiene la llave para escapar. Encuéntrala antes de quedarte sin intentos!")
    print("Encuentra la llave mágica para escapar y cuidado con las criaturas 👹\n")
    
    
    while not llave_encontrada and vida > 0:
        mostrar_descripcion()
        interactuar_con_objeto()
        if llave_encontrada:
            break
        moverse()

    
    if llave_encontrada:
        print("🎉 ¡Felicidades! Encontraste la llave y escapaste de la casa 🏆")
    else:
        print("💀 Fin del juego. No lograste escapar ☠️")

# Iniciar el juego
juego()
import random

# juego de adivinanza: número secreto del 1 al 10
secreto = random.randint(1, 10)
intentos = 0

print("Estoy pensando en un número entre 1 y 10. ¡Adivina cuál es!")

while True:
    try:
        guess = int(input("Tu intento: "))
    except ValueError:
        print("Por favor introduce un número válido.")
        continue

    intentos += 1

    if guess == secreto:
        print(f"¡Acertaste! El número era {secreto} y te tomó {intentos} intentos.")
        break
    elif guess < secreto:
        print("Demasiado bajo. Intenta otra vez.")
    else:
        print("Demasiado alto. Intenta otra vez.")

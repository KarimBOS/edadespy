def puede_tomar_alcohol(edad):
    if edad >= 18:
        return "Apoco si muy adulto. Invita un bacacho"
    else:
        return "Naaa vayase mejor a ver pocoyo. Tas chavo"

if __name__ == "__main__":
    try:
        edad = int(input("Introduce tu edad: "))
        print(puede_tomar_alcohol(edad))
    except ValueError:
        print("Por favor, introduce un número válido.")

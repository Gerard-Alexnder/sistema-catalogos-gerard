catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad" : True},
    {"nombre" : "Manicure", "precio" : 200.00, "disponibilidad" : True},
    {"nombre" : "Pedicure", "precio" : 300.00, "disponibilidad" : False}
]


def main():
    while True:
        print("Menu")
        print("0. Salir")
        print("1. Ver catalogo completo")
        opcion = input("Elige una opción: ")

        if opcion == "0":
                    print("¡Hasta luego!")
                    break
        
        elif opcion == "1":
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")

        


if __name__ == "__main__":
    main()
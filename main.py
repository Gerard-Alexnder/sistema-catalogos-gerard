catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False},
]


def buscar_producto(catalogo, nombre_buscado):
    for producto in catalogo:
        if producto["nombre"].lower() == nombre_buscado.lower():
            return producto
    return None


def agregar_producto(catalogo, nombre, precio, disponibilidad):
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "disponibilidad": disponibilidad,
    }
    catalogo.append(nuevo_producto)
    return nuevo_producto


def main():
    while True:
        print("Menu")
        print("0. Salir")
        print("1. Ver catalogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un Producto Nuevo")
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            producto = buscar_producto(catalogo_negocio, nombre)
            if producto is not None:
                print(f"{producto['nombre']}: ${producto['precio']}")
            else:
                print("producto no encontrado")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            disponibilidad = True
            agregar_producto(catalogo_negocio, nombre, precio, disponibilidad)
            print("Producto agregado correctamente")


if __name__ == "__main__":
    main()
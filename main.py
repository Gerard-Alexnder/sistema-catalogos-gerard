catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False},
]


class negocio:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def ver_catalogo(self):
        for producto in self.catalogo:
            print(f"{producto['nombre']} ${producto['precio']}")

    def buscar_producto(self, nombre_buscado):
        for producto in self.catalogo:
            if producto["nombre"].lower() == nombre_buscado.lower():
                return producto
        return None

    def agregar_producto(self, nombre, precio_texto, disponibilidad):
        try:
            precio_numero = float(precio_texto)
        except (TypeError, ValueError):
            print("El precio debe ser un numero. Producto no agregado")
            return None

        nuevo_producto = {
            "nombre": nombre,
            "precio": precio_numero,
            "disponibilidad": disponibilidad,
        }
        self.catalogo.append(nuevo_producto)
        return nuevo_producto


def producto_disponible(catalogo, disponibilidad):
    while True:
        print("Menu")
        print("0. Salir")
        print("1. Ver catalogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un Producto Nuevo")
        print("4. Ver solo los productos diponibles")
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            negocio(catalogo).ver_catalogo()

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            producto = negocio(catalogo).buscar_producto(nombre)
            if producto is not None:
                print(f"{producto['nombre']}: ${producto['precio']}")
            else:
                print("producto no encontrado")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            disponibilidad = True
            resultado = negocio(catalogo).agregar_producto(nombre, precio, disponibilidad)
            if resultado is not None:
                print("Producto agregado correctamente")

        elif opcion == "4":
            for producto in catalogo:
                if producto["disponibilidad"] == disponibilidad:
                    print(f"{producto['nombre']}: ${producto['precio']}")

        else:
            print("Opción inválida")


def main():
    producto_disponible(catalogo_negocio, True)


if __name__ == "__main__":
    main()
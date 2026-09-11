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
        nombre_buscado_normalizado = str(nombre_buscado or "").strip().lower()

        for producto in self.catalogo:
            nombre_producto = str(producto.get("nombre", "")).strip().lower()
            if nombre_producto == nombre_buscado_normalizado:
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

    def producto_disponibles(self):
        return [producto for producto in self.catalogo if producto["disponibilidad"] is True]

    def producto_disponible(self, disponibilidad=None):
        if disponibilidad is None:
            return self.catalogo
        return [producto for producto in self.catalogo if producto["disponibilidad"] == disponibilidad]


def menu():
    negocio_actual = negocio(catalogo_negocio)

    while True:
        print("Menu")
        print("0. Salir")
        print("1. Ver catalogo completo")
        print("2. Buscar un producto")
        print("3. Agregar un Producto Nuevo")
        print("4. Ver solo los productos disponibles")
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            negocio_actual.ver_catalogo()

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            producto = negocio_actual.buscar_producto(nombre)
            if producto is not None:
                print(f"{producto['nombre']}: ${producto['precio']}")
            else:
                print("producto no encontrado")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            resultado = negocio_actual.agregar_producto(nombre, precio, True)
            if resultado is not None:
                print("Producto agregado correctamente")

        elif opcion == "4":
            for producto in negocio_actual.producto_disponible(True):
                print(f"{producto['nombre']}: ${producto['precio']}")

        else:
            print("Opción inválida")


def main():
    menu()


if __name__ == "__main__":
    main()
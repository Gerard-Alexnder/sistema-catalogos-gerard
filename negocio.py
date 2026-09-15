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

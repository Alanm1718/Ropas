
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio

    def get_precio(self):
        return self._precio

    def descripcion(self):
        return f"{self._nombre} - {self._precio:,} PYG"


class Camisa(Producto):
    def __init__(self, precio, talla):
        super().__init__("Camisa", precio)
        self.talla = talla

    def descripcion(self):
        return f"Camisa de talla {self.talla} - {self._precio:,} PYG"

class Pantalon(Producto):
    def __init__(self, precio, talla):
        super().__init__("Pantalón", precio)
        self.talla = talla

    def descripcion(self):
        return f"Pantalón de talla {self.talla} - {self._precio:,} PYG"

class Zapato(Producto):
    def __init__(self, precio, talla):
        super().__init__("Zapato", precio)
        self.talla = talla

    def descripcion(self):
        return f"Zapato de talla {self.talla} - {self._precio:,} PYG"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.descripcion()}")

    def procesar_compra(self, indice):
        producto = self.productos.pop(indice - 1)
        print(f"Has comprado: {producto.descripcion()}\n")

if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_producto(Camisa(150000, 'M'))
    tienda.agregar_producto(Pantalon(250000, 'L'))
    tienda.agregar_producto(Zapato(300000, '42'))

    print("Bienvenido a la tienda de ropa:")
    tienda.mostrar_productos()
    
    
    tienda.procesar_compra(1) 

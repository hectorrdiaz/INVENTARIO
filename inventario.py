class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            raise ValueError(f"El producto '{nombre}' ya existe en el inventario.")
        self.productos[nombre] = {'cantidad': cantidad, 'precio': precio}

    def actualizar_stock(self, nombre, nueva_cantidad):
        if nombre not in self.productos:
            raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
        self.productos[nombre]['cantidad'] = nueva_cantidad

    def eliminar_producto(self, nombre):
        if nombre not in self.productos:
            raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
        del self.productos[nombre]

    def buscar_producto(self, nombre):
        return self.productos.get(nombre, None)
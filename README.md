# Sistema de Inventario

Este proyecto es un sistema simple de gestión de inventario que permite agregar, actualizar, eliminar y buscar productos. Incluye una suite de pruebas unitarias para asegurar que todas las funciones del sistema funcionen correctamente.

## Contenido del Proyecto

- `inventario.py`: Implementación del sistema de gestión de inventario.
- `test_inventario.py`: Pruebas unitarias para verificar el funcionamiento del sistema.

## Requisitos

- Python 3.6 o superior
- pytest (para ejecutar las pruebas unitarias)

## Instalación

1. **Clona el repositorio** (si aplica):
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <DIRECTORIO_DEL_PROYECTO>
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala las dependencias**:
    ```sh
    pip install pytest
    ```

## Uso

### Ejemplo de uso del sistema de inventario

Puedes usar el sistema importando la clase `Inventario` desde `inventario.py`. Aquí tienes un ejemplo de cómo usar el sistema:

```python
from inventario import Inventario

# Crear una instancia del inventario
inventario = Inventario()

# Agregar un nuevo producto
inventario.agregar_producto('manzana', 50, 0.5)

# Actualizar el stock de un producto existente
inventario.actualizar_stock('manzana', 30)

# Buscar un producto
print(inventario.buscar_producto('manzana'))

# Eliminar un producto
inventario.eliminar_producto('manzana')

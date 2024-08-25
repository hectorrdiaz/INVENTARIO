import pytest
from inventario import Inventario

@pytest.fixture
def inventario():
    return Inventario()

def test_agregar_producto(inventario):
    inventario.agregar_producto('manzana', 50, 0.5)
    assert inventario.buscar_producto('manzana') == {'cantidad': 50, 'precio': 0.5}

def test_agregar_producto_existente(inventario):
    inventario.agregar_producto('manzana', 50, 0.5)
    with pytest.raises(ValueError, match="El producto 'manzana' ya existe en el inventario."):
        inventario.agregar_producto('manzana', 30, 0.4)

def test_actualizar_stock(inventario):
    inventario.agregar_producto('manzana', 50, 0.5)
    inventario.actualizar_stock('manzana', 30)
    assert inventario.buscar_producto('manzana') == {'cantidad': 30, 'precio': 0.5}

def test_actualizar_stock_producto_no_existente(inventario):
    with pytest.raises(KeyError, match="El producto 'manzana' no existe en el inventario."):
        inventario.actualizar_stock('manzana', 30)

def test_eliminar_producto(inventario):
    inventario.agregar_producto('manzana', 50, 0.5)
    inventario.eliminar_producto('manzana')
    assert inventario.buscar_producto('manzana') is None

def test_eliminar_producto_no_existente(inventario):
    with pytest.raises(KeyError, match="El producto 'manzana' no existe en el inventario."):
        inventario.eliminar_producto('manzana')

def test_buscar_producto_no_existente(inventario):
    assert inventario.buscar_producto('manzana') is None
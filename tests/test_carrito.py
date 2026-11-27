from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

from utils.reader import read_productos_json

"""
    Prueba el flujo de agregar un producto al carrito de compras.
    Verifica que el contador del carrito se incremente correctamente y que el producto 
    agregado coincida con el que aparece en la vista detallada del carrito.
 """


def test_carrito(driver):

    # Abre la página de login y ejecuta el flujo completo
    LoginPage(driver).abrir().login_completo("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    producto = read_productos_json()[0]

    inventory_page.agregar_producto(producto["nombre"])

    assert inventory_page.obtener_contador_carrito() == "1"

    inventory_page.ir_al_carrito()

    assert cart_page.obtener_nombre_producto() == producto["nombre"]

    assert cart_page.obtener_precio_producto() == producto["precio"]


    driver.quit()
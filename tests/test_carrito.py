from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

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

    try:
        producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        nombre_producto = producto.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        producto.find_element(By.TAG_NAME, "button").click()   

        
        cont_carrito = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        assert cont_carrito == "1"

        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        nombre_carrito = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        assert nombre_carrito == nombre_producto 

    finally:
        driver.quit()
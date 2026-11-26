from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory(driver):
 
    # Abre la página de login y ejecuta el flujo completo
    LoginPage(driver).abrir().login_completo("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
       
    try:

        # Validación del título de la pestaña del navegador
        assert driver.title == "Swag Labs"

        # Búsqueda y verificación de que existan elementos en el catálogo
        productos = inventory_page.obtener_productos()
        assert len(productos) > 0

        # Extracción y comprobación de datos (nombre y precio) del primer producto
        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"

        # Verificación de visibilidad del menú de navegación lateral

        assert inventory_page.menu_visible()

        # Verificación de visibilidad del selector de ordenamiento de productos
        assert inventory_page.filtro_visible()

    finally:
        # Cierra la instancia de Firefox y libera los recursos
        driver.quit()
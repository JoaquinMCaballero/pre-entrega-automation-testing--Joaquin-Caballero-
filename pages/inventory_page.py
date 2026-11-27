# pages/inventory_page.py

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text
    
    def obtener_productos(self):
        """Obtiene la lista de productos disponibles."""
        return self.driver.find_elements(*self._PRODUCTS)

    def obtener_nombre_primer_producto(self):
        return self.obtener_productos()[0].find_element(*self._PRODUCT_NAME).text

    def obtener_precio_primer_producto(self):
        return self.obtener_productos()[0].find_element(*self._PRODUCT_PRICE).text  

    def menu_visible(self):
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self._FILTRO).is_displayed()

    
    def agregar_producto(self,nombre):
        productos = self.obtener_productos()
        for producto in productos:
            nombre_producto = producto.find_element(*self._PRODUCT_NAME).text
            if nombre_producto == nombre:
                producto.find_element(By.TAG_NAME,"button").click()
                return
        raise AssertionError(f"No se encontró el producto: {nombre}")
    
    def obtener_contador_carrito(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text

    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()
        
    def hacer_logout(self):
        """Cierra la sesión del usuario."""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(
        EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        from pages.login_page import LoginPage

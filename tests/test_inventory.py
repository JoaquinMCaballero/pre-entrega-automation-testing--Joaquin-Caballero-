import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login

def test_inventory():
    # Inicializa el driver para el navegador Firefox
    driver = webdriver.Firefox()
       
    try:
        #Inicio el login
        login(driver,"user-name", "password")

        # Validación del título de la pestaña del navegador
        assert driver.title == "Swag Labs"

        # Búsqueda y verificación de que existan elementos en el catálogo
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        # Extracción y comprobación de datos (nombre y precio) del primer producto
        nombre_producto = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"

        # Verificación de visibilidad del menú de navegación lateral
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        # Verificación de visibilidad del selector de ordenamiento de productos
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

    finally:
        # Cierra la instancia de Firefox y libera los recursos
        driver.quit()
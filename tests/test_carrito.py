from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login

"""
    Prueba el flujo de agregar un producto al carrito de compras.
    Verifica que el contador del carrito se incremente correctamente y que el producto 
    agregado coincida con el que aparece en la vista detallada del carrito.
 """


def test_carrito():
    # Inicializa el driver para el navegador Firefox
    driver = webdriver.Firefox()

    try:
        #Inicio el login
        login(driver,"user-name", "password")

     
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
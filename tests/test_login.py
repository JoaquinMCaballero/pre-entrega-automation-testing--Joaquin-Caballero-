from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login

"""
    Prueba el flujo de inicio de sesión exitoso con credenciales válidas.
    Verifica la redirección y la carga correcta de la página principal del inventario. 
"""


def test_login_exitoso():
    # Inicializa el driver para el navegador Firefox
    driver = webdriver.Firefox()
    
    try:
        #Inicio el login
        login(driver,"user-name","password")

        # Verifica que la URL haya cambiado a la ruta del inventario
        assert "/inventory.html" in driver.current_url

        # Valida que el texto del logo principal sea correcto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # Valida que el título de la sección corresponda a los productos
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
         # Asegura el cierre del navegador y la sesión de WebDriver, incluso si una aserción falla
        driver.quit()



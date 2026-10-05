import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    """
    Prueba el flujo de inicio de sesión exitoso con credenciales válidas.
    Verifica la redirección y la carga correcta de la página principal del inventario.
    """

    # Inicializa el driver para el navegador Firefox
    driver = webdriver.Firefox()
    
    try:
        # Navega a la página de inicio de la aplicación
        driver.get("https://www.saucedemo.com/")

        # Localiza los elementos del formulario de autenticación
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        # Ingresa las credenciales para el incio de sesión
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        # Envía el formulario para iniciar sesión
        boton_login.click()

        # VERIFICACIONES (ASSERTS)
        # 1. Verifica que la URL haya cambiado a la ruta del inventario
        assert "/inventory.html" in driver.current_url

        # 2. Valida que el texto del logo principal sea correcto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # 3. Valida que el título de la sección corresponda a los productos
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
         # Asegura el cierre del navegador y la sesión de WebDriver, incluso si una aserción falla
        driver.quit()

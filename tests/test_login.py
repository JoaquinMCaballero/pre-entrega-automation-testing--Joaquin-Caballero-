from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
import pytest 
from utils.reader import read_users_csv

@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver,data):
    wait = WebDriverWait(driver, 5)
    login_page = LoginPage(driver)
    # Abre la página de login y ejecuta el flujo completo
    login_page.abrir().login_completo(data["usuario"],data["password"])

    if data["tipo_usuario"] == "True":
        # Verifica que la URL haya cambiado a la ruta del inventario
        print(data["tipo_usuario"])
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url

        # Valida que el texto del logo principal sea correcto
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
        assert logo.text == "Swag Labs"

        # Valida que el título de la sección corresponda a los productos
        titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']")))
        assert titulo.text == "Products"
    elif data["tipo_usuario"] == "False": 
        print("Falso")
        assert "Epic Sadface" in login_page.obtener_mensaje_error()
  
    

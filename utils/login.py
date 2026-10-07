from selenium.webdriver.common.by import By

def login(driver, usuario, contraseña):
    # Navega a la página de inicio de la aplicación
    driver.get("https://www.saucedemo.com/")

    # Localiza los elementos del formulario de autenticación
    user = driver.find_element(By.ID, usuario)
    password = driver.find_element(By.ID, contraseña)
    boton_login = driver.find_element(By.ID, "login-button")

    # Ingresa las credenciales para el incio de sesión
    user.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # Envía el formulario para iniciar sesión
    boton_login.click()

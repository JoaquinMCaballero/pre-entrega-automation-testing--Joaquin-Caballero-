# conftest.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options



@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado."""
    firefox_options = Options()
    # chrome_options.add_argument("--headless") # Para CI/CD
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.implicitly_wait(5)
    yield driver
    time.sleep(1) # Para ver el resultado final
    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"}

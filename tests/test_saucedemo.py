'''from selenium import webdriver 
import time 
driver = webdriver.Chrome() # O Firefox(), Edge()
driver.get("https://www.google.com") 
print("Título:", driver.title)
time.sleep(5) 
driver.quit()'''

import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver


@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'

def test_catalogo( driver ):
    login_saucedemo( driver )
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

  




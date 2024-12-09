
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # time.sleep(5)

    # driver.find_element(By.CSS_SELECTOR,"button[role='none']").click()
    # driver.find_elements(By.CSS_SELECTOR, ".oxd-main-menu-item.active").click()
    time.sleep(5)
    request.cls.driver = driver
    yield
    # print("hii")
    driver.close()



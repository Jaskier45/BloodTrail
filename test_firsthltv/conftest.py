import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope = 'function')
def browser():
    print("\nStart test ...")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("End test.")
    browser.quit()

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.hltv.org/"
def test_open_page(browser):
    print('Start first test :/')
    browser.get(url)
    accept_cookie = WebDriverWait(browser,15).until(
        EC.element_to_be_clickable((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
    )
    accept_cookie.click()
    page_title = browser.title
    assert page_title == 'CS:GO News & Coverage | HLTV.org'
    print('End first test PogU!!!!1')
        #time.sleep(3)

@pytest.mark.smoke
def test_search(browser):
    print('Try to find some players')
    browser.get(url)
    accept_cookie = WebDriverWait(browser,15).until(
        EC.element_to_be_clickable((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
    )
    accept_cookie.click()
    search_box = browser.find_element(By.XPATH,'//input[@name="query"]')
    search_box.send_keys('s1mple')
    browser.find_element(By.XPATH,'//i[@class="fa fa-search"]').click()
    browser.find_element(By.CSS_SELECTOR,'a[href="/player/7998/s1mple"]').click()
    time.sleep(10)
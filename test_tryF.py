import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#pytest -v -s -m list .\test_tryF.py

@pytest.fixture(scope = 'function')
def browser():
    print('Start browser test ...')
    browser = webdriver.Chrome()
    yield browser
    print('quit browser test :/')
    browser.quit()


class TestOpenPage:
    @pytest.mark.smoke
    def test_open(self, browser):
        print("Start first test ...")
        browser.get("https://www.hltv.org/")
        accept_cookie = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
        )
        accept_cookie.click()
        page_name = browser.title
        assert page_name == 'CS:GO News & Coverage | HLTV.org'
        print("End first test PogU!!!!!")

    @pytest.mark.smoke
    @pytest.mark.list
    def test_match_list(self, browser):
        print("Start second test ...")
        #method without scope = 'class'
        browser.get("https://www.hltv.org/")
        accept_cookie = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
        )
        accept_cookie.click()
        browser.find_element(By.CSS_SELECTOR,".navmatches").click()
        upcoming_match = browser.find_elements(By.CSS_SELECTOR,".match")
        for item in upcoming_match:
            print(item.text, sep = '\n')
        print("End second test PogU!!!!!")

#.upcomingMatch
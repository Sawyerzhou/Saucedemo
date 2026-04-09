from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_open_saucedemo(driver):
    assert "Swag Labs" in driver.title
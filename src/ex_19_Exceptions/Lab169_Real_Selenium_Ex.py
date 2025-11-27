from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.maximize_window()
    driver.find_element("id", "button does not exist")

except NoSuchElementException as nse:
    print("element not found", nse.msg)

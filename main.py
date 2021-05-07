from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(
    "https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(8)
my_element = driver.find_element_by_id('downloadButton')
my_element.click()


# Explicitly wait
WebDriverWait(driver, 30).until(
    # EC.text_to_be_present_in_element(locator, text_) || (Element filtration, The expected text)
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), 'Completed!')
)

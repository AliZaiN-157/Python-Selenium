from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.implicitly_wait(5)

# Remove any kind of unwanted Ads
try:
    removeAd = driver.find_element_by_class_name('at-cm-no-button')
    removeAd.click()
except:
    print('No Add element found')

# Using Keys to edit inputs

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)

# to achieve total sum button use css_selectors
total_sum = driver.find_element_by_css_selector(
    'button[onclick="return total()"]')
total_sum.click()

# Css selectors You can use

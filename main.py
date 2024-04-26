from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options

options = options.Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')

print(driver.title)
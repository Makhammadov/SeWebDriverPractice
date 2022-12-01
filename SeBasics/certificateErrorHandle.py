from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#initializing webdriver
web_options = Options()
web_options.add_experimental_option("detach", True)
web_options.set_capability("acceptInsecureCerts",True)

driver = webdriver.Chrome(options=web_options, service=Service(ChromeDriverManager().install()))

driver.get("https://expired.badssl.com/")
ele = driver.find_element(By.CSS_SELECTOR, "#content h1")
print(ele.text)

driver.quit()
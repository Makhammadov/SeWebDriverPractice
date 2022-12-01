from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#initializing webdriver
web_detach = Options()
web_detach.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=web_detach, service=Service(ChromeDriverManager().install()))

driver.get('https://www.amazon.com')

wait = WebDriverWait(driver, 10)
wait.until(ec.title_is(driver.title))

print(driver.execute_script("return document.title;"))

best_seller = driver.find_element(By.LINK_TEXT, "Best Sellers")
driver.execute_script("arguments[0].click();", best_seller)

print(driver.execute_script("return document.title;"))



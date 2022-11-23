import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

web_detach = Options()
web_detach.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=web_detach, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://tools.usps.com/zip-code-lookup.htm?byaddress")

def select_value(element, value):
    Select(element).select_by_value(value)

select_value(driver.find_element(By.ID, "tState"), 'TN')
time.sleep(5)

state_d_d = Select(driver.find_element(By.ID, "tState"))

states_list = state_d_d.options
for state in states_list:
    print(state.text)
    if state.text == "ME - Maine":
        state.click()
        break

# time.sleep(10)
driver.close()
#importing required lib
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#initializing webdriver
web_detach = Options()
web_detach.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=web_detach, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.delta.com/")
time.sleep(3)

sky_miles_tab = driver.find_element(By.ID, "headSectab2")
act_chain = ActionChains(driver)
act_chain.move_to_element(sky_miles_tab).perform()
how_to_earn_miles = driver.find_element(By.ID, "secondary-static-link-0")
how_to_earn_miles.click()


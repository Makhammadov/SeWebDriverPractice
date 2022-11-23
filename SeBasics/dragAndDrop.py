#https://jqueryui.com/resources/demos/droppable/default.html
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

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

act_chains = ActionChains(driver)

#act_chains.drag_and_drop(source, target).perform()

time.sleep(5)
driver.quit()

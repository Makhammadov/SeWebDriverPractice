#https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/

#importing required lib
from selenium import webdriver
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
#functions Will be declared here:

def select_values(options_list, value):
    for option in options_list:
        if option.text in value:
            option.click()

#navigating to the web_page
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.implicitly_wait(2)

options_list = ["choice 1", "choice 2", "choice 3", "choice 4", "choice 5", "choice 6"]
driver.find_element(By.ID, "justAnInputBox").click()
driver.implicitly_wait(2)
dd_list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
driver.implicitly_wait(2)

#calling th function
select_values(dd_list, "choice 6" )

#closting the window
#driver.close()

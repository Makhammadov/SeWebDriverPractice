import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#Step 1:
#initializing webdriver go to the "https://www.usps.com"
web_detach = Options()
web_detach.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=web_detach, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

#get to the web page
driver.get("https://www.usps.com")
driver.maximize_window()

time.sleep(3)

#creating an instance of ActionChains class
act_chain = ActionChains(driver)

#create refeance variable to a Quick Tools tab
qk_tools_ele = driver.find_element(By.CSS_SELECTOR, ".nav-first-element.menuitem")

#Step 2:
#moving the mouse over quick tools to expose dropdown menu
act_chain.move_to_element(qk_tools_ele).perform()

time.sleep(3)

#Step 3:
#locating Zip code Look Up button and click
#Option 1
#zip_lookup_ele = driver.find_element(By.PARTIAL_LINK_TEXT, ".qt-nav.menuheader li:nth-child(7) ")
#Option 2
zip_lookup_ele = driver.find_element(By.CSS_SELECTOR, ".qt-nav.menuheader li:nth-child(7) ")
zip_lookup_ele.click()

time.sleep(3)

#Step 4:
#locate and clic on the find by address button
find_by_add_btn = driver.find_element(By.LINK_TEXT, "Find by Address")
find_by_add_btn.click()

time.sleep(3)

#Step 5:
#locate street adress textbox and type "1000 broadway"
street_textbox = driver.find_element(By.ID, "tAddress")
street_textbox.send_keys("1000 Broadway")

#locate city textbox and type "Nashville"
street_textbox = driver.find_element(By.ID, "tCity")
street_textbox.send_keys("Nashville")

#locate state drop down elemnet choose "TN" as option
street_textbox = driver.find_element(By.ID, "tState")
Select(street_textbox).select_by_value("TN")

time.sleep(3)

#Step 6:
#locate find button clic on it
find_btn = driver.find_element(By.ID, "zip-by-address")
find_btn.click()


time.sleep(5)
driver.quit()

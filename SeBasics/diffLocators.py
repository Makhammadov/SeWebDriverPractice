import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

web_option = Options()
web_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web_option, service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://www.usps.com")

quickTools = driver.find_element(By.XPATH, "//a[@class='nav-first-element menuitem']")
#quickTools = driver.find_element(By.CLASS_NAME, "nav-first-element menuitem") #not working
quickTools.click()


zipLookUp = driver.find_element(By.XPATH, "//*[@id='g-navigation']/div/nav/ul/li[1]/div/ul/li[7]/a")
#zipLookUp = driver.find_element(By.XPATH, "//a[@tabindex='-1']")
zipLookUp.click()

#byAddress = driver.find_element(By.XPATH, "//a[@class='btn-primary zip-code-home']")
#byAddress = driver.find_element(By.XPATH, "//*[contains(@title,'byaddress')]") #not working
driver.find_element(By.LINK_TEXT, 'Find by Address').click()


driver.find_element(By.ID, "tAddress").send_keys("1000 Broadway")
driver.find_element(By.ID, "tCity").send_keys("Nashville")
driver.find_element(By.ID, "tState").send_keys("TN")
#driver.find_element(By.CLASS_NAME, "btn-primary").click() #not working
driver.find_element(By.ID, "zip-by-address").click()


driver.get_screenshot_as_file("screenshot2.png")
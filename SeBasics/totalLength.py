from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#creating instance of Options() class
#setting detach to True
web_detach = Options()
web_detach.add_experimental_option("detach", True)

#initailizing the browser
driver = webdriver.Chrome(options=web_detach, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

#get to the web address
driver.get("https://www.amazon.com")

#get all the linsks and return the length
links_list = driver.find_elements(By.TAG_NAME, "a")
print("Number of links: ", len(links_list))

for link in links_list:
    print(link.text)
    print((link.get_attribute("href")))

#iamges list
images_list = driver.find_elements(By.TAG_NAME, "img")
print("Number of images: ", len(images_list))

for image in images_list:

    print(image.get_attribute("src"))

#close the window
driver.close()



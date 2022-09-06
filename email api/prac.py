from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains (driver)
#driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://postdev.akru.co/sign-up/czFYcldlTUVjMmFKbjF0dTVITXBfNjMxNmVlMGM1MWEzNDI4NmE5NDg2YzE5")
#to refresh the browser
#driver.refresh()
# identifying the edit box and entering text in edit box

#driver.find_element_by_xpath("//form[input/@name ='search']")
 

# driver.find_element(By.XPATH("//input[@name='key']")).send_keys("Selenium")
# # clears the content
# driver.find_element(By.XPATH("//input[@name='key']")).clear()

username_input = driver.find_element(By.XPATH, '//input[@name="zipCode"]')
username_input.send_keys("00")
time.sleep(3)
action.key_down(Keys.COMMAND).perform()
action.send_keys('a').perform()
action.key_up(Keys.COMMAND).perform()
action.send_keys(Keys.BACK_SPACE).perform()
username_input.clear()
#driver.find_element(By.XPATH, '//input[@name="zipCode"]').clear()
time.sleep(3)
driver.save_screenshot("prac.png")
        #screenshot = Image.open("idsig.png")
allure.attach.file(r"prac.png", "screenshot",attachment_type=allure.attachment_type.PNG)
time.sleep(3)
driver.quit()
#to close the browser
driver.close
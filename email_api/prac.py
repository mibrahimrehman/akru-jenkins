from pickle import FALSE
import unittest

from selenium import webdriver
import time
import names
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import allure

class test_invite(unittest.TestCase):

    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--disable-dev-shm-using')
        # s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        #s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service , options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        driver =  self.driver
        action = ActionChains (self.driver)
#get method to launch the URL
        self.driver.get("https://postdev.akru.co/sign-up/czFYcldlTUVjMmFKbjF0dTVITXBfNjMxNmVlMGM1MWEzNDI4NmE5NDg2YzE5")
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
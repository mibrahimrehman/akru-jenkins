from binhex import FInfo
from collections import abc
from lib2to3.pgen2 import driver
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
#from PIL import Image
#import allure
#import yopmail_login
from yopmail_login import yopmail
import variables
from chrome_setup import chrome


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        # WINDOW_SIZE = "1920,1080"
        # chrome_options = Options()
        # #chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--disable-setuid-sandbox')
        # #s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        # # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        
        
        # service = ChromeService(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=service , options=chrome_options)
       # PATH = "chromedriver"
        #self.driver = webdriver.Chrome(PATH, options=chrome_options)

        csk = chrome()
        self.driver = csk.get_driver()
        driverl = self.driver

        self.test_search_in_python_org(self.driver)

        

    def test_search_in_python_org(self , driver):
        driver = self.driver
        driver.maximize_window()
        url = variables.url

        action = ActionChains (driver)
        def clearTextField():
            action.key_down(Keys.COMMAND).perform()
            action.send_keys('a').perform()
            action.key_up(Keys.COMMAND).perform()
            action.send_keys(Keys.BACK_SPACE).perform()


        driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')
        wait = WebDriverWait(driver, 120)

        time.sleep(3)
        try:
            loginButton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#navbar-header-sticky-login")))
            loginButton.click()
            print('SUCCESS: Get Started button clicked')
        except:
            print("FAILED: Get Started button could not be clicked")
            raise Exception

        try:
            tenant_portal = wait.until(EC.element_to_be_clickable((By.XPATH,     "//button[. = 'Tenant portal']")))
            tenant_portal.click()
            print('SUCCESS: Tenant portal option clicked')
        except:
            print("FAILED: Tenant portal option could not be clicked")
            raise Exception

        def cookiesHandle():
            try:
                time.sleep(3)
                cookiesClickerFound=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='d-flex justify-content-end']/button[3]")))
                cookiesClickerFound.click()
                print('SUCCESS: "Allow all cookies" button clicked')
            except:
                print('FAILED: "Allow all cookies" button could not be clicked')
                raise Exception
        cookiesHandle()

        try:
            mo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-select-magic")))
            mo.click()
            print('SUCCESS: Email option from modale clicked')
        except:
            print("FAILED: Email option from modale could not be clicked")
            raise Exception

        
        try:
            emailbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-magic-email")))
            emailbox.click()
            print('SUCCESS: email box clicked')
        except:
            print("FAILED: email box could not be clicked")
            raise Exception

        try:
            email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar-magic-email")))
            email.click()
            clearTextField()
            email.send_keys(variables.login_email)
            print('SUCCESS: email entered successfully')
        except:
            print("FAILED: email could not be entered")
            raise Exception

        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-magic-next")))
            next_button.click()
            print('SUCCESS:Next button clicked')
        except:
            print("FAILED:Next button could not be clicked")
            raise Exception

        try:
            if(wait.until(EC.visibility_of_element_located(By.CLASS_NAME , 'loader-overlay'))):
                print("SUCCESS: Loader found")
                loaderremove = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
                print("SUCCESS: Loader disappeared successfully")
            else:
                print("FAILED: loader did not disappeared or still loading")

        except:
            print("FAILED: Loader did not open")


        # Login from yopmail
        ym = yopmail(driver)
        ym.run()


        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Log in successfully toaster appeared')
        except:
            print("FAILED: Toaster could not appeared")
            raise Exception

        #ym = yopmail(driver)
        #ym.run()
        time.sleep(5)

        #Click Maintenance ticket
        try:
            maintenance_ticket = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,  "#tomaintenanceticket")))
            maintenance_ticket.click()
            print('SUCCESS: Maintenance_ticket clicked successfully')
        except:
            print("FAILED: Maintenance_ticket could not be clicked successfully")
            raise Exception
        # maintenance_ticket = driver.find_element(By.CSS_SELECTOR,
        #                                      "#tomaintenanceticket")
        # maintenance_ticket.click()

        # 46. Scroll window by ('0','148')
        driver.execute_script("window.scrollBy(0,148)")

        # 47. Click '​'
        _ = driver.find_element(By.CSS_SELECTOR,
                                "#mui-component-select-propertyId")
        _.click()

        # 48. Click 'bahria lodges'
        bahria_lodges = driver.find_element(By.XPATH,
                                            "//li[. = 'bahria lodges']")
        bahria_lodges.click()

        # 49. Click '​1'
        _1 = driver.find_element(By.CSS_SELECTOR,
                                "#mui-component-select-unitId")
        _1.click()

        # 50. Click '3'
        _3 = driver.find_element(By.XPATH,
                                "//li[. = '3']")
        _3.click()

        # 51. Click 'message'
        message = driver.find_element(By.CSS_SELECTOR,
                                    "[name='message']")
        message.click()

        # 52. Type 'maintenance ticket from tenantav3 ' in 'message'
        try:
            message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='message']")))
            message.send_keys("maintenance ticket from tenantav3 ")
            print('SUCCESS: Message entered successfully')
        except:
            print("FAILED: Message could not be entered")


        # 53. Click 'Generate Ticket'
        try:
            generate_ticket = wait.until(EC.presence_of_element_located((By.XPATH,"//button[. = ' Generate Ticket']")))
            generate_ticket.click()
            print('SUCCESS: Generate Ticket button clicked successfully')
        except:
            print("FAILED: Generate Ticket button could not be clicked")

        # generate_ticket = driver.find_element(By.XPATH,
        #                                     "//button[. = ' Generate Ticket']")
        # generate_ticket.click()

        # 54. Is 'DIV3' present?
        div3 = driver.find_element(By.XPATH,
                                "//body/div/div/div[1]/div/div")

        # 55. Scroll window by ('0','-237')
        driver.execute_script("window.scrollBy(0,-237)")

        # 56. Scroll window by ('0','-8')
        driver.execute_script("window.scrollBy(0,-8)")

        # 57. Scroll window by ('0','-1')
        driver.execute_script("window.scrollBy(0,-1)")



        
        time.sleep(5)
        
        
        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        #allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

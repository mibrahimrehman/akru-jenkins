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
        url = "https://postdev.akru.co/sign-up/czFYcldlTUVjMmFKbjF0dTVITXBfNjMxMDVhNGFiN2ZhMzEwYTZmMjU3YTI2"
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname + lname + '123@yopmail.com'
        print("EMAIL generated for signup is: " , email)
        phone_no = '5678956789'

        action = ActionChains (self.driver)
        def clearTextField():
            action.key_down(Keys.COMMAND).perform()
            action.send_keys('a').perform()
            action.key_up(Keys.COMMAND).perform()
            action.send_keys(Keys.BACK_SPACE).perform()

        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')
        wait = WebDriverWait(self.driver, 120)

        time.sleep(2)
        
        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="isTradingLowSecurities"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//li[@data-value="true"]'):
                #if option.text == 'Ohio'
                if True:
                    option.click()
                    break
            print("SUCCESS: Low trade volume , yes is selected")
        except:
            print("FAILED: Low trade volume , yes is not selected")
            raise Exception


        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="employmentStatus"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, "//li[@data-value='unemployed']"):
                #if option.text == 'Ohio'
                if True:
                    option.click()
                    break
            print("SUCCESS: Employement status , unemployed is selected")
        except:
            print("FAILED: Employement status , unemployed is not selected")
            raise Exception

        time.sleep(3)
        try:
            addbanklater=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='veryLow']/parent::span")))
            time.sleep(2)
            addbanklater=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='veryLow']/parent::span")))
            addbanklater.click()
            print('SUCCESS:  Will add bank later is clicked')
        except:
            print("FAILED:  Will add bank later could not be clicked")
            raise Exception


        try:
            skipAddingBankButton=wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Next"]')))
            skipAddingBankButton.click()
            print('SUCCESS: Next button of account detail is clicked')
        except:
            print("FAILED:  Next button of account detail could not be clicked")
            raise Exception

        

        try:
            checkingAgreement1=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point1"]')))
            checkingAgreement1.click()
            print('SUCCESS: Agreement 1 checked')
        except:
            print("FAILED: Agreement 1 could not be checked")
            raise Exception

        try:
            checkingAgreement2=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point2"]')))
            checkingAgreement2.click()
            print('SUCCESS: Agreement 2 checked')
        except:
            print("FAILED: Agreement 2 could not be checked")
            raise Exception

        try:
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point3"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 3 checked')
        except:
            print("FAILED: Agreement 3 could not be checked")
            raise Exception
        try:
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point4"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 4 checked')
        except:
            print("FAILED: Agreement 4 could not be checked")
            raise Exception
        try:
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point5"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 5 checked')
        except:
            print("FAILED: Agreement 5 could not be checked")
            raise Exception


        
        try:
            ContinueButtonAfterCheckingAgreements=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
            ContinueButtonAfterCheckingAgreements.click()
            print('SUCCESS: Continue button clicked after checking all 5 agreements')
        except:
            print("FAILED: Continue button could not be clicked after checking all 5 agreements")
            raise Exception

        time.sleep(5)
        
        try:
            esignature=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="eSignature"]')))
            esignature.click()
            esignature.send_keys(fname + lname)
            print('SUCCESS: Esignature is signed')
        except:
            print("FAILED: Esignature could not be signed")
            raise Exception



        try:
            VerifyInfoButtonAtStep5=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
            VerifyInfoButtonAtStep5.click()
            print('SUCCESS: Verify button at step 5 is clicked')
        except:
            print("FAILED: Verify button at step 5 could not be clicked")
            raise Exception

        time.sleep(10)
        try:
            createConnectWalletButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
            createConnectWalletButton.click()
            print('SUCCESS: CREATE/CONNECT wallet button is clicked')
        except:
            print("FAILED: CREATE/CONNECT wallet button could not be clicked")
            raise Exception

        try:
            magicButtonFromSignupModal=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="donwload-btn"]')))
            magicButtonFromSignupModal.click()
            print('SUCCESS: Magic button is clicked from signup modal')
        except:
            print("FAILED: Magic button could not be clicked from signup modal")
            raise Exception

        try:
            time.sleep(3)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')
        
        def emailLogin():
            self.driver.execute_script("window.open('http://www.yopmail.com', 'new window')")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('SUCCESS: Switched to YOPMAIL tab')

            try:
                time.sleep(3)
                search = wait.until(EC.element_to_be_clickable((By.ID,"login")))
                search.clear()
                search.send_keys(email)
                search.send_keys(Keys.RETURN)
                print('SUCCESS: Email entered in YOPMAIL input field')
            except:
                print('FAILED: Email could not be entered in YOPMAIL input field')
                raise Exception

            time.sleep(3)
            self.driver.refresh()
            time.sleep(5)

            try:
                self.driver.switch_to.frame('ifmail')
            except:
                print("FAILED: Could not switch to iframe in YOPMAIL.")
                raise Exception

            try:
                time.sleep(3)
                LoginEmailButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//strong[text()="Log in to Akru TestNet"]')))
                LoginEmailButton.click()
                print('SUCCESS: "Log in to Akru TestNet" button clicked from YOPMAIL')
            except:
                print('FAILED: Could not find "Log in to Akru TestNet" button. Maybe due to captcha.')
                raise Exception

        emailLogin()

        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(10)

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            OKButtonAfterSignUpCompletion=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Ok"]')))
            OKButtonAfterSignUpCompletion.click()
            print('SUCCESS: OK button after signup completion is clicked')
        except:
            print('FAILED: OK button after signup completion could not be clicked')
            raise Exception

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if LoginToasterMessage.text == 'Registered successfully!':
            print('\nSUCCESS: SUCCESSFULLY LOGGED IN. Toaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        else:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        print('\nSUCCESSFULLY SINGED UP INDIVIDUAL ACCOUNT\n' + "Email: " + email)

    def tearDown(self):
        time.sleep(5)
        self.driver.save_screenshot("idsig.png")
        #screenshot = Image.open("idsig.png")
        allure.attach.file(r"idsig.png", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager import driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PSTUTeachersPage:
    div_page_xpath="//div[@class='col-md-9']/div[@class='row']/div[@class='col-md-4 wow slideInRight']"
    
    
    def __init__(self, driver):
        self.driver=driver
        self.driver.set_window_size(1080,800)
        
        
    def findpersonscount(self):
        # For Text Length   
        sleep(2)
        self.personcount=len(self.driver.find_elements(By.XPATH,self.div_page_xpath))
        return self.personcount
         
         
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager import driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BDNewsPage:
    div_body_xpath="//img[@src]"
    
    
    def __init__(self, driver):
        self.driver=driver
        self.driver.set_window_size(1080,800)
        
        
    def collectImages(self):
         all_images=self.driver.find_elements(By.XPATH,self.div_body_xpath)
         return all_images
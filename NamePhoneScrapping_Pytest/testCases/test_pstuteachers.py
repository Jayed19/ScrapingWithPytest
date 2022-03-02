from fileinput import filename
from time import sleep
from urllib import request
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pageObjects.pstuteacherspageobject import PSTUTeachersPage
from utilities.readProperties import readConfig
from utilities.customlogger import LogGen
from utilities import XLUtils
import pytest
from datetime import datetime
import os
import requests





#TestCase run command is pytest -v -s testCases/test_bdnewsobj.py
#If wanto run in browser mode, pytest -v -s testCases/test_bdnewsobj.py --browser firefox
# Finally report and screenshot generated auto timestamp mode. Now can run simply "pytest -v .\testcases\test_bdnewsobj.py"
#-v is for sending extra argument and -s for disable all capturing
# for _metadata not found in config object error have to setup pytest-metadata

class Test_001_pstuteachers:
    #For making a Folder Path with Timestamp in Screenshot direcotry
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")
    #os.makedirs(".//screenshots/test_bdnewsobj/"+timestampStr)
    #Create log object for logwrite method
    log=LogGen.logwrite()

    #Page URL
    url=readConfig.geturl()
    
    # Path for Datadriven Excel File 
    path=".//TestData/eVisa_Test.xlsx"
    #path=".//TestData/Login_Data.xlsx"
    #user=readConfig.getuser()
    #pwd=readConfig.getpwd()
        
    def test_pstuperson(self,setup):
        self.log.info("****Started Test_001_bdnews********")
        self.driver=setup
        sleep(1)
        self.driver.get(self.url)
        sleep(10)
        self.psp=PSTUTeachersPage(self.driver)
        self.perscount=self.psp.findpersonscount()
        self.perscount=str(self.perscount)

        if os.path.exists("Namephone"):
            pass
        else:
            os.makedirs("Namephone")
        
        self.filepath=".//Namephone/test.txt"
        with open(self.filepath,"w") as fh:
                fh.write(self.perscount)

        '''
        for self.p in self.all_images:
            self.url=self.img.get_attribute('src') #https://www.banglanews24.com/public/desktop/img/google.png
            self.filename=self.url.split("/")[-1] #google.png
            self.filepath=os.path.join('images',self.filename) 
            self.imagedata=requests.get(self.url)

            with open(self.filepath,"wb") as fh:
                fh.write(self.imagedata.content)

        '''
        
        self.driver.close()
   
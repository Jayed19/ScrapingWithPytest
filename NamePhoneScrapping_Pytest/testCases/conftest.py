from sys import executable
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager
import pytest
from datetime import datetime
opts=webdriver.ChromeOptions()
opts.headless=False



@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=opts)
    elif browser=="firefox":
        #For working firefox have to download geckodriver.exe and point this path
        #Have to add firefox executable path in the path of environment variable
        #Firefox exe found in programm file
        
        driver=webdriver.Firefox(executable_path=r'.//drivers/geckodriver.exe')

    elif browser=="edge":

        #For working Edge have to download msedgedriver.exe and keep in C Drive
        #Download Link https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        #options.add_extension(r"Path_to_your_extension_here...\extension_name.crx") # Modify the path here...
        capabilities = DesiredCapabilities.EDGE
        driver = Edge(executable_path = r'.//drivers/msedgedriver.exe', options = options,desired_capabilities=capabilities) # Modify the path here...

    elif browser=="opera":
        driver=webdriver.Opera(executable_path=r'.//drivers/operadriver.exe')
        '''
    #Safari webdriver is supported after version 10, and windows cannot install safari after version 5.7
    elif browser=="safari":
        driver=webdriver.Safari()
        '''   
    else:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=opts)
         
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


''' #Report off
##########PyTest HTML Report #########
# @pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata['Project Name']='Test Project'
    config._metadata['Module Name']='Test Module'
    config._metadata['Tester']='Jayed'
    config.option.htmlpath = 'reports/' + datetime.now().strftime("%Y%m%d_%H%M%S") + "_Report.html"
    config.option.self_contained_html = True
    

# It is hook for delete/Modify Enviroment to HTML Report
@pytest.mark.optionalhook
def pytest_metdata(metadata):
    metadata.pop('JAVA HOME',None)
    metadata.pop('Plugins',None)

'''
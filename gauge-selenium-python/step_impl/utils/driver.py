from getgauge.python import before_suite, after_suite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver(object):
    driver = None
    options = Options()
    options.headless = True
    
    CHROMEDRIVER_PATH='/usr/local/bin/'
    @before_suite
    def __init__():
        Driver.driver = webdriver.Chrome(driver_path=CHROMEDRIVER_PATH, chrome_options=options)
    @after_suite
    def close():
        Driver.driver.close()

from getgauge.python import before_suite, after_suite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("--headless") 

class Driver(object):
    driver = None
  
    @before_suite
    def init():
        Driver.driver = webdriver.Chrome(chrome_options=chromeOptions)
    @after_suite
    def close():
        Driver.driver.close()

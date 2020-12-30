from getgauge.python import before_suite, after_suite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 

chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars") 
chromeOptions.add_argument("--headless") 
chromeOptions.add_argument(r"user-data-dir=.\cookies\\" + login) 
b = webdriver.Chrome(chrome_options=chromeOptions) 

class Driver(object):
    driver = None
  
    @before_suite
    def init():
        Driver.driver = webdriver.Chrome(chrome_options=chromeOptions)
    @after_suite
    def close():
        Driver.driver.close()

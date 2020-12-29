from getgauge.python import before_suite, after_suite
from selenium import webdriver

class Driver(object):
    driver = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    @before_suite
    def __init__():
        Driver.driver = webdriver.Chrome(chrome_options=chrome_options)
    @after_suite
    def close():
        Driver.driver.close()

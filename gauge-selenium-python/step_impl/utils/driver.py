from getgauge.python import before_suite, after_suite
from selenium import webdriver

class Driver(object):
    driver = None

    @before_suite
    def __init__():
        Driver.driver = webdriver.Chrome()
    @after_suite
    def close():
        Driver.driver.close()
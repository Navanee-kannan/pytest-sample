import time1

from selenium import webdriver
from selenium.common import WebDriverException


class Base:
    driver = None

    def launch_browser(self):
        print('in launch browser function')
        options = webdriver.ChromeOptions()
        try:
            # self.driver = webdriver.Remote('http://localhost:4444',options=options)
            self.driver = webdriver.Chrome(options=options)
        except WebDriverException as e:
            print(e)
        self.driver.get('http://amazon.in')
        self.driver.maximize_window()
        time.sleep(1)


    def quit(self):
        self.driver.quit()


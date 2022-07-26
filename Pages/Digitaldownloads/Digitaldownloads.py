import time
from selenium.webdriver.common.by import By
from Locators.path import path
from selenium.webdriver.common.keys import Keys


class download_digital_page:
    def __init__(self, driver):
        self.driver = driver
        self.digital_page = path.digital_page_xpath
        self.digital_detail_page = path.digital_detail_page_xpath

    def digital_download_page(self):
        self.driver.find_element(By.XPATH, path.digital_page_xpath).send_keys(Keys.CONTROL + Keys.RETURN)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        # self.driver.find_element(By.XPATH, path.digital_detail_page_xpath).click()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # self.driver.close()
        # time.sleep(10)

    def detail_page(self):
        self.driver.find_element(By.XPATH, path.digital_detail_page_xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.driver.close()
        time.sleep(10)

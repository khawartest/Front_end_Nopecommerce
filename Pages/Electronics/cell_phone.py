from selenium.webdriver.common.by import By
from Locators.path import path


class cell_phone:
    def __init__(self, driver):
        self.driver = driver
        self.cell_home_page = path.cell_ph_main_page_xpath
        self.cell_detail_page = path.detail_page_xpath

    def cell_phone_home_post(self):
        self.driver.find_element(By.XPATH, path.cell_ph_main_page_xpath).click()

    def detail_page1(self):
        self.driver.find_element(By.XPATH, path.detail_page_xpath).click()



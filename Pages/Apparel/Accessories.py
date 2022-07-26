import time
from selenium.webdriver.common.by import By
from Locators.path import path
from selenium.webdriver.common.action_chains import ActionChains


class accessories_page:
    def __init__(self, driver):
        self.driver = driver
        self.hover = path.hover_on_apparel_xpath
        self.goto_cloths_page = path.click_0n_accessories_xpath
        self.sunglass_detail_page = path.access_detail_page_xpath

    def hover_apparel_accessories_page(self, driver):
        # object of ActionChains3
        action_on_accessories = ActionChains(driver)
        # identify element
        hover_on_apparel = self.driver.find_element(By.XPATH, path.hover_on_apparel_xpath)
        # hover over element
        action_on_accessories.move_to_element(hover_on_apparel).perform()
        # identify sub menu element
        accessories = self.driver.find_element(By.XPATH, path.click_0n_accessories_xpath)
        # hover over element and click
        action_on_accessories.move_to_element(accessories).click().perform()
        time.sleep(10)

    def accessories_detail_page(self):
        self.driver.find_element(By.XPATH, path.access_detail_page_xpath).click()
        time.sleep(10)


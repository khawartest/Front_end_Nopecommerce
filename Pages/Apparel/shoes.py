import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locators.path import path
from selenium.webdriver.common.action_chains import ActionChains


class shoes_page:
    def __init__(self, driver):
        self.driver = driver
        self.hover = path.apparel_page_hover_xpath
        self.shoes_page_link = path.click_on_shoes_page_xpath
        self.shoes_filter = path.filter_id
        self.post_detail = path.shoes_detail_post_xpath
        self.add_to_cart_btn = path.add_cart_btn_xpath
        self.select_size = path.short_by_size_id

    def hover_apparel_shoes_page(self, driver):

        # object of ActionChains2
        a = ActionChains(driver)
        # identify element
        m = self.driver.find_element(By.XPATH, path.apparel_page_hover_xpath)
        # hover over element
        a.move_to_element(m).perform()
        # identify sub menu element
        n = self.driver.find_element(By.XPATH, path.click_on_shoes_page_xpath)
        # hover over element and click
        a.move_to_element(n).click().perform()

    def filter(self):
        self.driver.find_element(By.ID, path.filter_id).click()
        time.sleep(5)

    def add_cart_btn(self):
        self.driver.find_element(By.XPATH,path.shoes_detail_post_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, path.add_cart_btn_xpath).click()
        # select size of a shoes
        time.sleep(5)
        select_by_size = Select(self.driver.find_element(By.ID, path.short_by_size_id))
        select_by_size.select_by_value("23")
        # select size of a shoes end
        # again click on add cart button
        time.sleep(5)
        self.driver.find_element(By.ID, path.add_cart_btn2_id).click()
        time.sleep(5)

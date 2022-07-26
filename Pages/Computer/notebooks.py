import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Locators.path import path


class Notebooks:
    def __init__(self, driver):
        self.driver = driver
        self.notebooks = path.notebooks_img_link_xpath
        self.notebooks_short_by = path.short_by_id
        self.notebooks_display_page = path.display_per_page_id
        self.notebooks_viewlist = path.view_by_list_xpath
        self.notebooks_tab = path.new_tab_post_xpath
        self.notebooks_add_cart = path.notebook_add_cart_button_id
        self.notebooks_wish_list = path.notebook_add_wishlist_button_id
        self.notebooks_compare_list = path.notebook_add_compare_btn_xpath
        self.shipping_section = path.shipping_add_xpath
        self.select_by_country = path.country_id
        self.select_by_state = path.state_id
        self.select_by_zipcode = path.zip_code_id
        self.submit_button = path.submit_btn_xpath
        self.main_window = path.main_second_post_xpath

    def notebook_home(self):
        self.driver.find_element(By.XPATH, path.notebooks_img_link_xpath).click()

    def sort_by(self):
        select_sort_by = Select(self.driver.find_element(By.ID, path.short_by_id))
        select_sort_by.select_by_value("10")

    def show_page(self):
        select_display_per_page = Select(self.driver.find_element(By.ID, path.display_per_page_id))
        select_display_per_page.select_by_value("9")

    def view_list(self):
        self.driver.find_element(By.XPATH, path.view_by_list_xpath).click()
        time.sleep(5)

    def new_tab(self):
        self.driver.find_element(By.XPATH, path.new_tab_post_xpath).send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

    def add_cart_btn(self):
        self.driver.find_element(By.ID, path.notebook_add_cart_button_id).click()
        time.sleep(5)

    def wishlist_btn(self):
        self.driver.find_element(By.ID, path.notebook_add_wishlist_button_id).click()
        time.sleep(5)

    def compare_list_btn(self):
        self.driver.find_element(By.XPATH, path.notebook_add_compare_btn_xpath).click()

    def shipping(self):
        self.driver.find_element(By.XPATH, path.shipping_add_xpath).click()
        time.sleep(5)

    def country(self):
        select_country = Select(self.driver.find_element(By.ID, path.country_id))
        select_country.select_by_value("1")
        time.sleep(5)

    def state(self):
        select_state = Select(self.driver.find_element(By.ID, path.state_id))
        select_state.select_by_value("47")
        time.sleep(5)

    def zip_code(self, zipcode):
        self.driver.find_element(By.ID, path.zip_code_id).send_keys(zipcode)
        time.sleep(5)

    def submit_btn(self):
        self.driver.find_element(By.XPATH, path.submit_btn_xpath).click()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(10)

    def main_tab(self):
        self.driver.find_element(By.XPATH, path.main_second_post_xpath).click()
        time.sleep(10)

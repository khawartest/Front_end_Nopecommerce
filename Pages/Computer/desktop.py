import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Locators.path import path


class Computer:
    def __init__(self, driver):
        self.driver = driver
        self.computer_parent_page = path.computer_detail_page_xpath
        self.desktop = path.desktop_img_link_xpath
        self.short_by = path.short_by_id
        self.display_page = path.display_per_page_id
        self.viewlist = path.view_by_list_xpath
        self.detail_post = path.detail_post_xpath
        self.add_cart_btn = path.add_cart_button_id
        self.wishlist_button = path.add_wishlist_button_id
        self.add_compare_list_btn = path.add_compare_btn_xpath

    def desktop_home(self):
        self.driver.find_element(By.XPATH, path.desktop_img_link_xpath).click()

    def sort_by(self):
        select_sort_by = Select(self.driver.find_element(By.ID, path.short_by_id))
        select_sort_by.select_by_value("10")

    def show_page(self):
        select_display_per_page = Select(self.driver.find_element(By.ID, path.display_per_page_id))
        select_display_per_page.select_by_value("9")

    def view_list(self):
        self.driver.find_element(By.XPATH, path.view_by_list_xpath).click()
        time.sleep(5)

    def inner_post(self):
        self.driver.find_element(By.XPATH, path.detail_post_xpath).click()
        time.sleep(5)

    def addcart_btn(self):
        self.driver.find_element(By.ID, path.add_cart_button_id).click()
        time.sleep(5)

    def wishlist_btn(self):
        self.driver.find_element(By.ID, path.add_wishlist_button_id).click()
        time.sleep(5)

    def comparelist_btn(self):
        self.driver.find_element(By.XPATH, path.add_compare_btn_xpath).click()

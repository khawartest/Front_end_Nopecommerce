import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Locators.path import path


class Software:
    def __init__(self, driver):
        self.driver = driver
        self.software = path.software_post_xpath
        self.software_short_by = path.short_by_id
        self.software_display_page = path.display_per_page_id
        self.software_viewlist = path.view_by_list_xpath
        self.software_tab = path.soft_new_tab_post_xpath
        self.software_add_cart = path.software_add_cart_button_id
        self.software_wish_list = path.software_add_wishlist_button_id
        self.software_compare_list = path.software_add_compare_btn_xpath
        self.shipping_section = path.soft_shipping_add_xpath
        self.select_by_country = path.country_id
        self.select_by_state = path.state_id
        self.select_by_zipcode = path.zip_code_id
        self.submit_button = path.soft_submit_btn_xpath
        self.main_window = path.soft_main_tab_xpath
        self.email_btn = path.soft_email_btn_xpath
        self.friend_email = path.friend_email_id
        # self.my_email = path.y_email_id
        self.message = path.p_message_id
        self.s_btn = path.send_email_btn_xpath

    def software_home(self):
        self.driver.find_element(By.XPATH, path.software_post_xpath).click()

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
        self.driver.find_element(By.XPATH, path.soft_new_tab_post_xpath).send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

    def add_cart_btn(self):
        self.driver.find_element(By.ID, path.software_add_cart_button_id).click()
        time.sleep(5)

    def wishlist_btn(self):
        self.driver.find_element(By.ID, path.software_add_wishlist_button_id).click()
        time.sleep(5)

    def compare_list_btn(self):
        self.driver.find_element(By.XPATH, path.software_add_compare_btn_xpath).click()

    def shipping(self):
        self.driver.find_element(By.XPATH, path.soft_shipping_add_xpath).click()
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
        self.driver.find_element(By.XPATH, path.soft_submit_btn_xpath).click()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

    def main_tab(self):
        self.driver.find_element(By.XPATH, path.soft_main_tab_xpath).click()

    def email_to_friend_btn(self):
        self.driver.find_element(By.XPATH, path.soft_email_btn_xpath).click()

    def frind_email(self, f_email):
        self.driver.find_element(By.ID, path.friend_email_id).send_keys(f_email)

    def personal_message(self, m_box):
        self.driver.find_element(By.ID, path.p_message_id).send_keys(m_box)

    def send_email_to_friend_btn(self):
        self.driver.find_element(By.XPATH, path.send_email_btn_xpath).click()
        time.sleep(5)

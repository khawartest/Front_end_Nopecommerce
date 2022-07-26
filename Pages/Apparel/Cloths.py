import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.path import path
from selenium.webdriver.common.action_chains import ActionChains


class cloths_page:
    def __init__(self, driver):
        self.driver = driver
        self.hover = path.hover_on_apparel_xpath
        self.goto_cloths_page = path.click_0n_cloth_xpath
        self.new_tab_detail_post = path.cloth_detail_post_xpath
        self.cloth_add_btn = path.cloth_add_cart_btn_id
        self.close_notification = path.cloth_cross_icon_xpath
        self.enter_text = path.cloth_input_txt_xpath

    def hover_apparel_cloth_page(self, driver):
        # object of ActionChains3
        a = ActionChains(driver)
        # identify element
        m = self.driver.find_element(By.XPATH, path.hover_on_apparel_xpath)
        # hover over element
        a.move_to_element(m).perform()
        # identify sub menu element
        n = self.driver.find_element(By.XPATH, path.click_0n_cloth_xpath)
        # hover over element and click
        a.move_to_element(n).click().perform()

    def cloths_detail_post(self, cloth_text):
        self.driver.find_element(By.XPATH, path.cloth_detail_post_xpath).send_keys(Keys.CONTROL + Keys.RETURN)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.find_element(By.ID, path.cloth_add_cart_btn_id).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, path.cloth_cross_icon_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, path.cloth_input_txt_xpath).send_keys(cloth_text)
        time.sleep(5)
        self.driver.find_element(By.ID, path.cloth_add_cart_btn_id).click()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

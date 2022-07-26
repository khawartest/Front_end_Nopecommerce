import time
from selenium.webdriver.common.by import By
from Locators.path import path
from selenium.webdriver.common.action_chains import ActionChains


class others_page:
    def __init__(self, driver):
        self.driver = driver
        self.hover = path.other_page_hover_xpath
        self.click_on_others_page_link = path.click_0n_other_xpath
        self.new_tab = path.new_tab_url
        self.new_tab1 = path.new_tab_url1
        self.new_tab2 = path.new_tab_url2

    def hover_electronic_page(self, driver):
        # object of ActionChains
        a = ActionChains(driver)
        # identify element
        m = self.driver.find_element(By.XPATH, path.other_page_hover_xpath)
        # hover over element
        a.move_to_element(m).perform()
        # identify sub menu element
        n = self.driver.find_element(By.XPATH, path.click_0n_other_xpath)
        # hover over element and click
        a.move_to_element(n).click().perform()
        time.sleep(5)

    def new_tab_other(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(path.new_tab_url)
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

    def new_tab_1(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(path.new_tab_url1)
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

    def new_tab_2(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(path.new_tab_url2)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(10)

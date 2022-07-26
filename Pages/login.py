from selenium.webdriver.common.by import By
from Locators.path import path


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login_txt_xpath = path.login_txt_link_path
        self.l_email_id = path.login_email_id
        self.l_password_id = path.login_password_id
        self.l_btn_xpath = path.login_btn_path

    def login_txt_link(self):
        self.driver.find_element(By.XPATH, path.login_txt_link_path).click()

    def l_email(self, email):
        self.driver.find_element(By.ID, path.login_email_id).send_keys(email)

    def l_password(self, password):
        self.driver.find_element(By.ID, path.login_password_id).send_keys(password)

    def l_btn(self):
        self.driver.find_element(By.XPATH, path.login_btn_path).click()

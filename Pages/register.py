from selenium.webdriver.common.by import By
from Locators.path import path


class SignUp:
    def __init__(self, driver):
        self.driver = driver

        self.register_txt_path = path.register_txt_path
        self.reg_gender_id = path.reg_gender_id
        self.reg_firstname_id = path.reg_firstname_id
        self.reg_last_name_id = path.reg_last_name_id
        self.reg_email_id = path.reg_email_id
        self.reg_password_id = path.reg_password_id
        self.reg_confirm_pass_id = path.reg_confirm_pass_id
        self.reg_button_id = path.reg_button_id
        self.reg_logout_txt_path = path.logout_txt_path

    def register_text_link(self):
        self.driver.find_element(By.XPATH, path.register_txt_path).click()

    def reg_select_gender(self):
        self.driver.find_element(By.ID, path.reg_gender_id).click()

    def reg_first_name(self, first_name):
        self.driver.find_element(By.ID, path.reg_firstname_id).send_keys(first_name)

    def reg_last_name(self, last_name):
        self.driver.find_element(By.ID, path.reg_last_name_id).send_keys(last_name)

    def reg_email(self, email):
        self.driver.find_element(By.ID, path.reg_email_id).send_keys(email)

    def reg_password(self, password):
        self.driver.find_element(By.ID, path.reg_password_id).send_keys(password)

    def reg_confirm_password(self, c_password):
        self.driver.find_element(By.ID, path.reg_confirm_pass_id).send_keys(c_password)

    def reg_button(self):
        self.driver.find_element(By.ID, path.reg_button_id).click()

    def reg_logout_txt(self):
        self.driver.find_element(By.XPATH, path.logout_txt_path).click()

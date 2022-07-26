import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.hard_copy_txt import txt
from Locators.path import path


class camera_pic:
    def __init__(self, driver):
        self.driver = driver
        self.cam_photo = path.cam_photo_post_xpath
        self.detail_post = path.cam_detail_post_xpath
        self.post_review = path.detail_post_review
        self.review_title = path.review_title_xpath
        self.review_area = path.review_text_area_xpath
        self.rating = path.radio_rating_id
        self.submit_btn = path.review_submit_button_xpath

    def cam_photo_home_post(self):
        self.driver.find_element(By.XPATH, path.cam_photo_post_xpath).click()

    def cam_detail_post(self):
        self.driver.find_element(By.XPATH, path.cam_detail_post_xpath).click()

    def cam_detail_post_review(self):
        self.driver.find_element(By.XPATH, path.detail_post_review).send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.find_element(By.XPATH, path.review_title_xpath).send_keys(txt.review_title)
        self.driver.find_element(By.XPATH, path.review_text_area_xpath).send_keys(txt.ReviewText_area)
        self.driver.find_element(By.ID, path.radio_rating_id).click()
        self.driver.find_element(By.XPATH, path.review_submit_button_xpath).click()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

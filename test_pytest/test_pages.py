import time
import pytest
# import allure
from selenium import webdriver
from Pages.login import Login
from Pages.register import SignUp
from Locators.hard_copy_txt import txt
from Pages.Computer.desktop import Computer
from Pages.Computer.software import Software
from Page_links.web_links import pages_links
from Pages.Computer.notebooks import Notebooks
from Pages.Electronics.cam_photo import camera_pic
from Pages.Electronics.cell_phone import cell_phone
from Pages.Electronics.others import others_page
from Pages.Apparel.shoes import shoes_page
from Pages.Apparel.Cloths import cloths_page
from Pages.Apparel.Accessories import accessories_page
from Pages.Digitaldownloads.Digitaldownloads import download_digital_page
from webdriver_manager.chrome import ChromeDriverManager


# @allure.severity(allure.severity_level.NORMAL)
class TestLogin:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()

    # register section coding start here
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_signup(self):
        driver = self.driver
        self.driver.get(pages_links.base_link)
        time.sleep(10)
        signup = SignUp(driver)
        signup.register_text_link()
        signup.reg_select_gender()
        signup.reg_first_name(txt.first_name)
        signup.reg_last_name(txt.last_name)
        signup.reg_email(txt.email)
        signup.reg_password(txt.password)
        signup.reg_confirm_password(txt.confirm_pass)
        signup.reg_button()
        signup.reg_logout_txt()
        time.sleep(5)
    # register section coding end here

    # Login section coding start here
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_singin(self):
        driver = self.driver
        # self.driver.get(pages_links.base_link)
        login = Login(driver)
        login.login_txt_link()
        login.l_email(txt.email)
        login.l_password(txt.password)
        login.l_btn()
        time.sleep(10)
    # Login section coding end here

    # computer page-->Desktop section start
    # @allure.severity(allure.severity_level.NORMAL)
    def test_compdesktop(self):
        driver = self.driver
        desktop = Computer(driver)
        self.driver.get(pages_links.computer_page_link)
        desktop.desktop_home()
        desktop.sort_by()
        desktop.show_page()
        desktop.view_list()
        desktop.inner_post()
        desktop.addcart_btn()
        desktop.wishlist_btn()
        desktop.comparelist_btn()
    # computer page-->Desktop section end

    # computer page-->Notebooks section start
    # @allure.severity(allure.severity_level.NORMAL)
    def test_compnotebook(self):
        driver = self.driver
        notebook = Notebooks(driver)
        self.driver.get(pages_links.computer_page_link)
        notebook.notebook_home()
        notebook.sort_by()
        notebook.show_page()
        notebook.view_list()
        notebook.new_tab()
        notebook.add_cart_btn()
        notebook.wishlist_btn()
        notebook.compare_list_btn()
        notebook.shipping()
        notebook.country()
        notebook.state()
        notebook.zip_code(txt.zipcode)
        notebook.submit_btn()
        notebook.main_tab()
    # computer page-->Notebooks section end

    # computer page-->software section start
    def test_comsoftware(self):
        driver = self.driver
        software = Software(driver)
        self.driver.get(pages_links.computer_page_link)
        software.software_home()
        software.sort_by()
        software.show_page()
        software.view_list()
        software.new_tab()
        software.add_cart_btn()
        software.wishlist_btn()
        software.compare_list_btn()
        software.shipping()
        software.country()
        software.state()
        software.zip_code(txt.zipcode)
        software.submit_btn()
        software.main_tab()
        software.email_to_friend_btn()
        software.frind_email(txt.f_email)
        software.personal_message(txt.m_box)
        software.send_email_to_friend_btn()
    # computer page-->software section end

    # electronics page-->camera_photo section start
    def test_electronic_camera_photo(self):
        driver = self.driver
        cam_pic = camera_pic(driver)
        self.driver.get(pages_links.electronics_parent_page)
        cam_pic.cam_photo_home_post()
        cam_pic.cam_detail_post()
        cam_pic.cam_detail_post_review()
    # electronics page-->camera_photo section end

    # electronics page-->cell phone section start
    def test_electronic_cell_phone(self):
        driver = self.driver
        c_phone = cell_phone(driver)
        self.driver.get(pages_links.electronics_parent_page)
        c_phone.cell_phone_home_post()
        c_phone.detail_page1()
    # electronics page-->cell phone section end

    # electronics page-->others section start
    def test_electronic_others_page(self):
        driver = self.driver
        others = others_page(driver)
        others.hover_electronic_page(driver)
        others.new_tab_other()
        others.new_tab_1()
        others.new_tab_2()
    # electronics page-->others section end

    # apparel page-->shoes phone section start
    def test_apparel_shoes_page(self):
        driver = self.driver
        shoes = shoes_page(driver)
        self.driver.get(pages_links.apparel_parent_page)
        shoes.hover_apparel_shoes_page(driver)
        shoes.filter()
        shoes.add_cart_btn()
    # apparel page-->shoes phone section end

    # apparel page-->cloth phone section start
    def test_apparel_cloths_page(self):
        driver = self.driver
        cloth = cloths_page(driver)
        self.driver.get(pages_links.apparel_parent_page)
        cloth.hover_apparel_cloth_page(driver)
        cloth.cloths_detail_post(txt.cloth_text)
    # apparel page-->cloth phone section end

    # apparel page-->Accessories section start
    def test_accessories_page(self):
        driver = self.driver
        access = accessories_page(driver)
        access.hover_apparel_accessories_page(driver)
        access.accessories_detail_page()
    # apparel page-->Accessories section end

    # apparel page-->Digital-downloads section start
    def test_digital_page(self):
        driver = self.driver
        digital = download_digital_page(driver)
        digital.digital_download_page()
        digital.detail_page()
    # apparel page-->Digital-downloads section end

    # @allure.severity(allure.severity_level.NORMAL)
    def test_listemploye(self):
        pytest.skip("add later")

    # @allure.severity(allure.severity_level.NORMAL)
    def test_tearDownClass(self):
        # self.driver.close()
        self.driver.quit()
        print("Test Completed")

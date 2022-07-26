# import time
# import unittest
# from selenium import webdriver
# from Pages.register import SignUp
# from Pages.login import Login
# from Pages.Computer.desktop import Computer
# from Pages.Computer.notebooks import Notebooks
# from Page_links.web_links import pages_links
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class LoginTest(unittest.TestCase):
#
#     @classmethod
#     def test_driver(cls):
#         cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         cls.driver.maximize_window()
#
#     # register section coding start here
#     # @unittest.skip
#     def test_signup(self):
#         driver = self.driver
#         self.driver.get(pages_links.base_link)
#         time.sleep(10)
#         signup = SignUp(driver)
#         signup.register_text_link()
#         signup.reg_select_gender()
#         signup.reg_first_name("Khawar")
#         signup.reg_last_name("Jehangiri")
#         signup.reg_email("testing1@gmail.com")
#         signup.reg_password("2brzG@34HjLRHF")
#         signup.reg_confirm_password("2brzG@34HjLRHF")
#         signup.reg_button()
#         signup.reg_logout_txt()
#         time.sleep(5)
#     # register section coding end here
#
#     # Login section coding start here
#     # @unittest.skip
#     def testsingin(self):
#         driver = self.driver
#         login = Login(driver)
#         login.login_txt_link()
#         login.l_email("testing1@gmail.com")
#         login.l_password("2brzG@34HjLRHF")
#         login.l_btn()
#         time.sleep(10)
#     # Login section coding end here
#
#     # computer page-->Desktop section start
#     # @unittest.skip
#     def testcompdesktop(self):
#         driver = self.driver
#         desktop = Computer(driver)
#         self.driver.get(pages_links.computer_page_link)
#         desktop.desktop_home()
#         desktop.sort_by()
#         desktop.show_page()
#         desktop.view_list()
#         desktop.inner_post()
#         desktop.addcart_btn()
#         desktop.wishlist_btn()
#         desktop.comparelist_btn()
#     # computer page-->Desktop section end
#
#     # computer page-->Notebooks section start
#     # @unittest.skip
#     def testcompnotebook(self):
#         driver = self.driver
#         notebook = Notebooks(driver)
#         self.driver.get(pages_links.computer_page_link)
#         notebook.notebook_home()
#         notebook.sort_by()
#         notebook.show_page()
#         notebook.view_list()
#         notebook.new_tab()
#         notebook.add_cart_btn()
#         notebook.wishlist_btn()
#         notebook.compare_list_btn()
#         # computer page-->Notebooks section end
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#         print("Test Completed")
#
#
# if __name__ == '__main__':
#     unittest.main()

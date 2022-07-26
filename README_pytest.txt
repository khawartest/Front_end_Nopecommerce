on pycharm IDE terminal

First
             folder\file path
pytest -v -s test_pytest\test_pages.py

Second
                           make allure report where it saved
pytest -v -s --alluredir="C:\Users\MYE\PycharmProjects\pythonProject\test_py\reports" test_py\test_pages.py

on cmd
             location where allure reports is saved
allure serve C:\Users\MYE\PycharmProjects\pythonProject\test_py\reports
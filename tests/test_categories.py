from time import sleep

from pages.authorization import AuthorizationPage
from pages.main_page import MainPage


def test_categories(driver):
    authorization = AuthorizationPage(driver)
    authorization.select_authorization()
    sleep(2)
    cb = MainPage(driver)
    cb.category()
    sleep(2)
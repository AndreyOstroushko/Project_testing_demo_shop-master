from time import sleep

from pages.authorization import AuthorizationPage
from pages.main_page import MainPage


def test_search_field(driver):
    authorization = AuthorizationPage(driver)
    authorization.select_authorization()
    sleep(3)
    search = MainPage(driver)
    search.search_computers()
    sleep(3)

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.authorization import AuthorizationPage


class MainPage(AuthorizationPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    search_field = '//input[@id="small-searchterms"]'
    check_result_search = '//div[@class="page-title"]'

    '''Getters'''
    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_result_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_result_search)))

    '''Actions'''
    def input_search_word(self):
        self.get_search_field().send_keys('computer')
        self.get_search_field().send_keys(Keys.RETURN)

    '''Method'''
    def search_computers(self):
        self.input_search_word()
        self.assert_word(self.get_result_search(), 'Search')




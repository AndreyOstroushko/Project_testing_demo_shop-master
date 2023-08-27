from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base


class AuthorizationPage(Base):

    base_url = 'https://demowebshop.tricentis.com/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    button_authorization = '//a[@class="ico-login"]'
    email = '//input[@name="Email"]'
    password = '//input[@id="Password"]'
    login_button = '//input[@class="button-1 login-button"]'


    '''Get wait authorization button'''
    def get_authorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_authorization)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))



    '''Actions'''
    def click_authorization_button(self):
        self.get_authorization_button().click()

    def input_email(self):
        self.get_email().send_keys('ostroushko98@inbox.ru')

    def input_password(self):
        self.get_password().send_keys('Qwerty123')

    def click_login_button(self):
        self.get_login_button().click()

    '''Method'''
    def select_authorization(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_authorization_button()
        self.input_email()
        self.input_password()
        self.click_login_button()

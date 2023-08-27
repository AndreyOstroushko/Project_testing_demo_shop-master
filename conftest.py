import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='C:\\Users\\Андрей\\PycharmProjects\\pythonProject123\\chromedriver.exe')
    yield driver
    driver.quit()
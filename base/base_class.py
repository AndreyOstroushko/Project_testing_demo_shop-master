class Base:

    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good')

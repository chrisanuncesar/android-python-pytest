from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).click()
        except NoSuchElementException as ex:
            raise ex

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except NoSuchElementException as ex:
            raise ex

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except NoSuchElementException as ex:
            raise ex

    def is_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        except NoSuchElementException as ex:
            raise ex

    def get_title(self, title):
        WebDriverWait(self.driver, 60).until(EC.title_is(title))
        return self.driver.title

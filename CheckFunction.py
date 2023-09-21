from abc import ABC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class CheckFuntion(ABC):
    def wait_until_element_available(self, by: By, expression: str, time_out_s: int, poll_interval: int = 1):
        counter = 0
        is_element_visible = self.is_element_available(by, expression)
        while counter < time_out_s and not is_element_visible:
            sleep(poll_interval)
            counter = counter + poll_interval
            is_element_visible = self.is_element_available(by, expression)

    def is_element_available(self, by: By, expression: str):
        try:
            item = self.web_driver.find_element(by, expression)
        except NoSuchElementException:
            print(item, " not found")
            return False
        except StaleElementReferenceException:
            print(item, " StaleElementReferenceException")
            return False
        return True

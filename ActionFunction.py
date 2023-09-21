from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class ActionFuntion(ABC):

    def drag_and_drop(self, element1: WebElement, element2: WebElement):
        self.actions.drag_and_drop(element1, element2).perform()

    def drag_and_drop(self, source: WebElement,  x: int, y: int):
        self.action.drag_and_drop_by_offset(source, 100, 100).perform()

    def open_drop_down_menu_and_select_text(self, drop_down: WebElement, text: str):
        select = Select(drop_down)
        select.select_by_visible_text(text=text)
        # select.select_by_value('1')

    def open_drop_down_menu_and_select_by_value(self, drop_down: WebElement, value: str):
        select = Select(drop_down)
        select.select_by_value(value=value)

    def open_drop_down_menu_and_select_by_index(drop_down: WebElement, index: int):
        select = Select(drop_down)
        select.select_by_index(index=index)

    def scroll_to_element(self, element: WebElement):
        self.web_driver.execute_script(
            "arguments[0].scrollIntoView();", element)

    def scroll_by(self, pixel: int):
        self.web_driver.execute_script("window.scrollTo(0, " + pixel + ")")

    def click(self, element: WebElement):
        self.action.click(element).perform()

    def double_click(self, element: WebElement):
        self.action.double_click(element).perform()

    def right_click(self, element: WebElement):
        self.action.context_click(element).perform()

    def enter_text_to_search_box(self, element: WebElement, key_word: str):
        element.send_keys(key_word)
        element.submit()

from abc import ABC
from selenium.webdriver.common.by import By


class GetFuntion(ABC):

    def get_element_with_text(self, text: str):
        return self.web_driver.find_element (By.XPATH, "//*[text()='" + text + "']")
    
    def get_element_from_class(self, class_name: str):
        return self.web_driver.find_element (By.CSS_SELECTOR, "."  + class_name)
    
    def get_element_with_attribute (self, attribute_name: str , attribute_value: str ):
        return self.web_driver.find_eleHello
    def get_element_has_parent(self, parent_option = str):
        return self.web_driver.find_element(By.XPATH, "/parent::" +  parent_option )
    
    def get_element_has_preceding(self, sibling_option = str):
        return self.web_driver.find_element(By.XPATH, "/preceding-sibling::" +  sibling_option )
    
    def get_element_has_following(self, sibling_option = str):
        return self.web_driver.find_element(By.XPATH, "/following-sibling::" +  sibling_option )
    
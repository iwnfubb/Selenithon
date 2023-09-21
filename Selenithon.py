import logging
import time

from enum import Enum, auto
from selenium.webdriver import Safari, Firefox, Chrome
from selenium.webdriver.common.action_chains import ActionChains
from GetFunction import GetFuntion
from ActionFunction import ActionFuntion
from CheckFunction import CheckFuntion

logger = logging.getLogger(__name__)

# Time out base on internet connection
TIME_OUT = 3


class WebDriverOption(Enum):
    SAFARI = auto()
    FIREFOX = auto()
    CHROME = auto()


class Selenithon (GetFuntion, ActionFuntion, CheckFuntion):
    def __init__(self, webdriver_option: WebDriverOption) -> None:
        self.web_driver_option = webdriver_option
        self.web_driver = None
        self.action = None

    def open_website(self, domain: str, timeout_s: int = TIME_OUT):
        match self.web_driver_option:
            case WebDriverOption.SAFARI:
                from selenium.webdriver.safari.options import Options
                opts = Options()
                opts.add_argument("--headless")
                self.web_driver = Safari(options=opts)
                pass
            case WebDriverOption.FIREFOX:
                from selenium.webdriver.firefox.options import Options
                opts = Options()
                opts.add_argument("--headless")
                self.web_driver = Firefox(options=opts)
            case WebDriverOption.CHROME:
                from selenium.webdriver.chrome.options import Options
                opts = Options()
                opts.add_argument("--headless")
                self.web_driver = Chrome(options=opts)
            case _:
                logger.error(
                    "Can not recognize web driver option. Please choose the following option: Safari, Firefor, Chrome")

        self.web_driver.get(domain)
        self.web_driver.maximize_window()
        self.action = ActionChains(self.web_driver)
        time.sleep(timeout_s)

    def close(self):
        self.web_driver.close()
        quit()

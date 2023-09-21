from Selenithon import Selenithon
from Selenithon import WebDriverOption


def main():
    sele = Selenithon(WebDriverOption.SAFARI)
    sele.open_website("https://www.google.de")
    element = sele.get_element_with_text("Google")
    print(element)


if __name__ == "__main__":
    main()

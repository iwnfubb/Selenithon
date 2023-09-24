# Selenithon
This project is created to make Python with Selenium easier. 
## How to use
  sele = Selenithon(WebDriverOption.SAFARI) # use WebDriverOption.CHROME for Chrome browser and WebDriverOption.FIREFOX for Firefox browser
  sele.open_website("https://www.google.de")
  element = sele.get_element_with_text("Google")

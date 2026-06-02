from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Parent class for all page objects

    It provides shared browser interaction helpers so
    individual page objects can focus purely on page specific behavior
    """

    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        return self

    def get.title(self)
        return self.driver.title

    def get_url(self)
        return self.driver.current_url

    def find(self, locator):
        """Wait for and return single element"""
        return self.wait.until(
            EC.presence_of_element_located((locator))
        )

    def find_all(self, locator):
        """Wait for and return all elements"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator, timeout=5):
        """Return True if element is visible within the timeout"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((locator))
            )
            return True
        except TimeoutException:
            return False

    def click(Self, locator):
        """Wait for element to be click and then clicks it"""
        element= self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text):
        """Clear the field and type text"""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return visible text of an element"""
        return self.find(locator).text.strip()

    def get_attribute(self, locator, attribute):
        return self.find(locator).get_attrib(attribute)

    def wait_for_url(self, partial_url, timeour=5)
        WebDiverWait(self.driver. timeout).until(
            EC.url_contains(aprtial_url)
        )



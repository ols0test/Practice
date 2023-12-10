"""This section contains the basic functions for running tests"""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        This method opens a browser by navigating to the provided URL.
        """
        self.driver.get(self.url)

    def element_is_visible(self, locator: tuple, timeout: int = 10) -> object:
        """
        This method  verifies that an element is present in the DOM tree, visible, and displayed on the page.
        Args:
            locator: (tuple) element's locator that we need to check (example:'id', 'name', 'css selector', 'xpath').
            timeout (int): max waiting time in seconds (10).
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_invisible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        This method verifies that the element becomes invisible (not displayed) on the page within a specified timeout.
        Args:
            locator: (tuple) element's locator that we need to check (example:'id', 'name', 'css selector', 'xpath').
            timeout (int): max waiting time in seconds (10).
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        Args:
            locator: (tuple) element's locator that we need to check (example:'id', 'name', 'css selector', 'xpath').
            timeout (int): max waiting time in seconds (10).
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        """
        This method verifies that an element is present in the DOM tree (not necessarily visible or displayed)
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_actual_url_of_current_page(self):
        """
        This method gets URL of the current page.
        """
        actual_url = self.driver.current_url
        return actual_url

    def action_move_to_element(self, element):
        """
        This method moves the mouse cursor to the center of the selected element, simulating a hover action.
        It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def go_to_element(self, element):
        """
        This method scrolls the page to make the selected element visible.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click(self, locator):
        """
        Clicks on an element identified by a locator.
        """
        element = self.element_is_clickable(locator)
        element.click()

    def get_text(self, locator):
        """
        This method gets  the text content of a visible element.
        :return: element text
        """
        element = self.element_is_visible(locator)
        return element.text

    def wait_for_element_to_load(self, locator):
        """
        Waits for an element to be visible on the page.
        :param locator:
        :return: element
        """
        wait_to_load = wait(self.driver, 15)
        element = wait_to_load.until(EC.visibility_of_element_located(locator))
        return element

    def select_option_from_dropdown(self, dropdown_locator, option_text):
        """
        This function selects an option from a dropdown menu.

        :param dropdown_locator: The locator of the dropdown element.
        :param option_text: The text of the option to select.
        """
        dropdown = self.element_is_clickable(dropdown_locator)
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    def switch_to_active_window(self):
        """
        This function switches to new opened window/tab
        """
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

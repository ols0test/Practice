"""This section contains locators"""

from selenium.webdriver.common.by import By


class AlertsPageLocators:
    """Choosing by ID since locators are static"""
    FIRST_ALERT_BUTTON = (By.ID, "alertButton")
    SECOND_ALERT_WITH_5SEC_DELAY = (By.ID, "timerAlertButton")
    THIRD_ALERT_CONFIRM_BOX = (By.ID, "confirmButton")
    TEXT_FOR_THIRD_ALERT = (By.ID, "confirmResult")
    FOURTH_ALERT_WITH_PROMPT = (By.ID, "promtButton")
    TEXT_FOR_FOURTH_ELEMENT_WITH_PROMPT = (By.ID, "promptResult")


class BrowserWindowsLocators:
    """Choosing by Xpath just for practice"""
    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEW_TAB_WINDOW_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")

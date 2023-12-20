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
    NEW_WINDOW_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")


class FramesLocators:
    """Choosing by Xpath just for practice"""
    BIG_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    TEXT_ON_FRAME = (By.XPATH, "//h1[@id='sampleHeading']")
    SMALL_FRAME = (By.XPATH, "//iframe[@id='frame2']")


class NestedFramesLocators:
    """Choosing by Xpath or ID"""
    PARENT_FRAME = (By.XPATH, "//*[@id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    CHILD_FRAME_TEXT = (By.XPATH, "/html/body/p")



"""This section contains locators"""

from selenium.webdriver.common.by import By


class AlertsPageLocators:
    """Choosing by ID since locators are static"""
    FIRST_ALERT_BUTTON = (By.ID, "alertButton")
    SECOND_ALERT_WITH_5SEC_DELAY = (By.ID, "timerAlertButton")
    THIRD_ALERT_CONFIRM_BOX = (By.ID, "confirmButton")
    TEXT_FOR_THIRD_ALERT = (By.ID, "confirmResult")


import time

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import AlertsPageLocators


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    def first_alert(self):

        self.element_is_clickable(self.locators.FIRST_ALERT_BUTTON)
        self.click(self.locators.FIRST_ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def second_alert_5_sec_delay(self):

        self.element_is_clickable(self.locators.SECOND_ALERT_WITH_5SEC_DELAY)
        self.click(self.locators.SECOND_ALERT_WITH_5SEC_DELAY)
        """Using Time sleep because alert window has no locators"""
        time.sleep(5)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def third_alert_with_accept_or_dismiss(self, choice):

        self.element_is_clickable(self.locators.THIRD_ALERT_CONFIRM_BOX)
        self.click(self.locators.THIRD_ALERT_CONFIRM_BOX)
        alert = self.driver.switch_to.alert
        if choice == "accept":
            alert.accept()
            text = "Ok"
        else:
            alert.dismiss()
            text = "Cancel"

        response = self.element_is_present(self.locators.TEXT_FOR_THIRD_ALERT).text
        return text, response




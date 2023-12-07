import time

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import AlertsPageLocators, BrowserWindowsLocators
from data.data_for_forms import DataForForms

class AlertsPage(BasePage):
    locators = AlertsPageLocators
    data_for_forms = DataForForms

    def first_alert(self):

        self.element_is_clickable(self.locators.FIRST_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def second_alert_5_sec_delay(self):

        self.element_is_clickable(self.locators.SECOND_ALERT_WITH_5SEC_DELAY).click()
        """Using Time sleep because alert window has no locators"""
        time.sleep(5)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def third_alert_with_accept_or_dismiss(self, choice):

        self.element_is_clickable(self.locators.THIRD_ALERT_CONFIRM_BOX).click()
        # self.click(self.locators.THIRD_ALERT_CONFIRM_BOX)
        alert = self.driver.switch_to.alert
        if choice == "accept":
            alert.accept()
            text = "Ok"
        else:
            alert.dismiss()
            text = "Cancel"

        response = self.element_is_present(self.locators.TEXT_FOR_THIRD_ALERT).text
        return text, response

    def fourth_alert_with_prompt_name(self, choice):

        self.element_is_clickable(self.locators.FOURTH_ALERT_WITH_PROMPT).click()
        alert = self.driver.switch_to.alert
        first_name = self.data_for_forms.first_name
        alert.send_keys(first_name)
        if choice == "accept":
            alert.accept()
            text = first_name
            response = self.element_is_present(self.locators.TEXT_FOR_FOURTH_ELEMENT_WITH_PROMPT).text
        else:
            alert.dismiss()
            text = None
            response = self.element_is_invisible(self.locators.TEXT_FOR_FOURTH_ELEMENT_WITH_PROMPT)

        return text, response


class WindowsPage(BasePage):
    locators = BrowserWindowsLocators

    def new_tab_button(self):

        self.element_is_clickable(self.locators.NEW_TAB_BUTTON).click()
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        text_on_new_tab = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return new_tab, text_on_new_tab









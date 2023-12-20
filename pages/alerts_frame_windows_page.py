import time

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import AlertsPageLocators, BrowserWindowsLocators, FramesLocators, \
    NestedFramesLocators
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

    def new_window_new_tab_buttons(self, choice):
        new_tab_button = self.element_is_clickable(self.locators.NEW_TAB_BUTTON)
        new_window_button = self.element_is_clickable(self.locators.NEW_WINDOW_BUTTON)
        if choice == new_tab_button:
            new_tab_button.click()
        else:
            new_window_button.click()
        opened_tab_window = self.switch_to_active_window()
        text_on_new_tab_window = self.element_is_present(self.locators.NEW_TAB_WINDOW_TEXT).text

        return opened_tab_window, text_on_new_tab_window


class FramesPage(BasePage):
    locators = FramesLocators

    def frames_get_info(self, choice):
        if choice == "big":
            frame = self.element_is_present(self.locators.BIG_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text_on_frame = self.element_is_present(self.locators.TEXT_ON_FRAME).text
        else:
            frame = self.element_is_present(self.locators.SMALL_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text_on_frame = self.element_is_present(self.locators.TEXT_ON_FRAME).text

        return width, height, text_on_frame


class NestedFramePage(BasePage):
    locators = NestedFramesLocators

    def nested_frames_text(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        text_on_parent_frame = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        text_on_child_frame = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return text_on_parent_frame, text_on_child_frame




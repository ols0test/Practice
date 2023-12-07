import pytest
from data.data_urls import ALERTS_PAGE_URL, WINDOWS_HANDLING_URL
from pages.alerts_frame_windows_page import AlertsPage, WindowsPage


class TestAlerts:
    user_choice = ["accept", "dismiss"]

    def test_first_alert(self, driver):
        """Checks if alert page can be opened and text is correct"""
        alert_page = AlertsPage(driver, ALERTS_PAGE_URL)
        alert_page.open()
        text_alert_page = alert_page.first_alert()
        assert text_alert_page == "You clicked a button", "You didn't click the button"

    def test_second_alert_with_5sec_delay(self, driver):
        """Checks if alert page can be opened and text is correct with 5 sec delay"""
        alert_page = AlertsPage(driver, ALERTS_PAGE_URL)
        alert_page.open()
        text_alert_page = alert_page.second_alert_5_sec_delay()
        assert text_alert_page == "This alert appeared after 5 seconds", "Alert didn't appear with delay"

    @pytest.mark.parametrize("choice", user_choice)
    def test_third_alert_with_accept_or_dismiss(self, driver, choice):
        """Checks if alert page can be opened and text is correct depends on user choice"""
        alert_page = AlertsPage(driver, ALERTS_PAGE_URL)
        alert_page.open()
        text, response = alert_page.third_alert_with_accept_or_dismiss(choice)
        assert text in response, "User choice doesn't match with text"

    @pytest.mark.parametrize("choice", user_choice)
    def test_fourth_alert_with_prompt_name(self, driver, choice):
        """Checks if alert page can be opened and text can be sent and text appears depends on choice"""
        alert_page = AlertsPage(driver, ALERTS_PAGE_URL)
        alert_page.open()
        text, response = alert_page.fourth_alert_with_prompt_name(choice)
        if choice == "accept":
            assert text in response, "Entered name doesn't appear in the text field"
        else:
            assert response is True, "User didn't enter name, but text is present on the page"


class TestWindows:

    def test_new_tab_button(self, driver):
        """Checks if new tab opens when button clicked and text on new tab is correct"""
        browser_page = WindowsPage(driver, WINDOWS_HANDLING_URL)
        browser_page.open()
        new_tab, new_tab_text = browser_page.new_tab_button()
        assert driver.current_url == "https://demoqa.com/sample", "Wrong page opened, URL doesn't match"
        assert new_tab_text == "This is a sample page", "Text on New tab page doesn't match"


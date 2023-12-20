import pytest
from data.data_urls import ALERTS_PAGE_URL, WINDOWS_HANDLING_URL, FRAME_PAGE_URL, NESTED_FRAME_PAGE_URL
from pages.alerts_frame_windows_page import AlertsPage, WindowsPage, FramesPage, NestedFramePage


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
    buttons_new_tab_new_window = ["New Tab", "New Window"]

    @pytest.mark.parametrize("choice", buttons_new_tab_new_window)
    def test_new_tab_new_window(self, driver, choice):
        """Checks if new tab/new window opens when button clicked and text on new tab/window is correct"""
        browser_page = WindowsPage(driver, WINDOWS_HANDLING_URL)
        browser_page.open()
        opened_tab_window, text_on_new_tab_window = browser_page.new_window_new_tab_buttons(choice)
        assert driver.current_url == "https://demoqa.com/sample", "Wrong page opened, URL doesn't match"
        assert text_on_new_tab_window == "This is a sample page", "Text on New tab page doesn't match"


class TestFrames:
    available_frames = ["big", "small"]

    @pytest.mark.parametrize("choice", available_frames)
    def test_frames(self, driver, choice):
        """Checks if big frame has correct size and text is correct"""
        frame_page = FramesPage(driver, FRAME_PAGE_URL)
        frame_page.open()
        width, height, text_on_frame = frame_page.frames_get_info(choice)
        if choice == "big":
            print(width, height)
            assert width == "500px" and height == "350px", "Big frame size doesn't match"
            assert text_on_frame == "This is a sample page", "Big frame text doesn't match"
        else:
            assert width == "100px" and height == "100px", "Small frame size doesn't match"
            assert text_on_frame == "This is a sample page", "Small frame text doesn't match"


class TestNestedFrames:
    def test_nested_frames(self, driver):
        """Checks if text on nested frames is correct"""
        nested_frame_page = NestedFramePage(driver, NESTED_FRAME_PAGE_URL)
        nested_frame_page.open()
        text_on_parent_frame, text_on_child_frame = nested_frame_page.nested_frames_text()
        assert text_on_parent_frame == "Parent frame", "Parent frame text doesn't match"
        assert text_on_child_frame == "Child Iframe", "Child frame text doesn't match"



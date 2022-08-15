import pytest

from pages.Tollway_Homepage import TollwayHomepage
from tests.test_base import BaseTest


@pytest.mark.Regression
class TestTollwayHomepage(BaseTest):

    def test_i_pass_box_visible(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.is_ipass_box_visible()
        print("iPass box is visible")

    def test_click_ipass_button(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.click_i_pass_button()
        print("Click iPass box")

    def test_login_button_visible(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.is_login_button_visible()
        print("Login button is visible")

    def test_click_login_button(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.click_login_button()
        print("Click on login button")

    def test_send_username(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.send_username()
        print("Input username")

    def test_send_password(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.send_password()
        print("Input password")

    def test_click_sign_in_button(self):
        self.tollwayHomepage = TollwayHomepage(self.driver)
        self.tollwayHomepage.click_sign_in_button()
        print("Click Sign in button")

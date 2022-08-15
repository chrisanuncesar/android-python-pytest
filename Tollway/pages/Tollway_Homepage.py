from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class TollwayHomepage(Basepage):

    boxIPass = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='ONBOARDING_MENU_SCREEN_IPASS_CARD_BUTTON_I"
                                "-PASS']/android.view.ViewGroup")
    btnLogin = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"IPASS_LOGIN_BUTTON\"]/android.widget.TextView")
    lnkForgotUsername = (By.XPATH, "//android.widget.TextView[@text='Forgot Username?']")
    lnkForgotPassword = (By.XPATH, "//android.widget.TextView[@text='Forgot Password?']")
    lnkSignUp = (By.XPATH, "1//android.widget.TextView[@text='Don't have an I-PASS account? Sign Up']")
    inputUsername = (AppiumBy.XPATH, "//android.widget.EditText[@text='']")
    inputPassword = (AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")
    btnSignIn = (AppiumBy.XPATH, "//android.widget.Button[@text='SIGN IN']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_ipass_box_visible(self):
        self.is_visible(self.boxIPass)

    def click_i_pass_button(self):
        self.click(self.boxIPass)

    def is_login_button_visible(self):
        self.is_visible(self.btnLogin)

    def click_login_button(self):
        self.click(self.btnLogin)

    def send_username(self):
        self.send_keys(self.inputUsername, "admin")

    def send_password(self):
        self.send_keys(self.inputPassword, "password")

    def click_sign_in_button(self):
        self.click(self.btnSignIn)




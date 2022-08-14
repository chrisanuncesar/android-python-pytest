import pytest
from appium import webdriver
from config.Utils import Utilities as utils


@pytest.fixture(params=["android"], scope='class')
def init_driver(request):
    if request.param == "android":
        caps = {
            "appium:deviceName": "Pixel 2",
            "appium:udid": "emulator-5554",
            "appium:platformName": "Android",
            "appium:platformVersion": "11",
            "appium:app": utils.get_current_dir() + "/app/app-release.apk",
            "appium:automationName": "UiAutomator2"
        }
        web_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

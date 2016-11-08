import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = 'beta'
        desired_caps['app'] = PATH(
            '/Users/romanchernetskiy/msapp-android/FeedReader/build/outputs/apk/FeedReader-1.0.0.bfed008.apk'
        )

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # def test_find_elements(self):
    #     # pause a moment, so xml generation can occur
    #     sleep(2)
    #
    #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    #     self.assertEqual('API Demos', els[0].text)
    #
    #     el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Animat")]')
    #     self.assertEqual('Animation', el.text)
    #
    #     el = self.driver.find_element_by_accessibility_id("App")
    #     el.click()
    #
    #     els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
    #     # there are more, but at least 10 visible
    #     self.assertLess(10, len(els))
    #     # the list includes 2 before the main visible elements
    #     self.assertEqual('Action Bar', els[2].text)
    #
    #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    #     self.assertLess(10, len(els))
    #     self.assertEqual('Action Bar', els[1].text)

    def test_scroll(self):
        sleep(2)
        self.driver.find_element_by_class_name('android.widget.Button').click()
        el = self.driver.find_element_by_id('de.com.meinestadt.stadtleben:id/textView')
        self.assertEquals('Simply yours', el.text)
        el = self.driver.find_element_by_id('de.com.meinestadt.stadtleben:id/btn_why')
        self.assertEquals('Why Register?', el.text)
        self.driver.find_element_by_id('de.com.meinestadt.stadtleben:id/btn_close').click()
        sleep(5)
        # el = self.driver.find_element_by_accessibility_id('Views')


if __name__ == '__main__':
    ComplexAndroidTests.run()

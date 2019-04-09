from framework2.browser_engine import BrowserEngline
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.browserEngline = BrowserEngline()
        self.driver = self.browserEngline.open_browser()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver = self.browserEngline.quit_browser()

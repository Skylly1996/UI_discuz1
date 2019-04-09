import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_homepage_login import HomePage_login
from pageobjects.discuz_homepage_vote import HomePage_vote
from pageobjects.discuz_homepage_exit import HomePage_exit
import time


class DiscuzSearch4(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = HomePage_login(self.driver)
        home_page1.login("grf",'123456')
        home_page2=HomePage_vote(self.driver)
        home_page2.voting("你觉得每天很累吗","累","不累")
        home_page3=HomePage_exit(self.driver)
        home_page3.exit1()
        time.sleep(5)

if __name__=='__main__':
    unittest.main()

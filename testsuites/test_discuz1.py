import sys
sys.path.append('D:\python-webUI-DISCUZ')
import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_homepage_login import HomePage_login
from pageobjects.discuz_homepage_posting import HomePage_posting
from pageobjects.discuz_homepage_exit import HomePage_exit
import time

class DiscuzSearch1(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = HomePage_login(self.driver)
        home_page1.login("grf",'123456')
        home_page2=HomePage_posting(self.driver)
        home_page2.postNew("新的帖子","这是一个新帖子")
        home_page2.postReply("这是一个新的回帖")
        home_page3=HomePage_exit(self.driver)
        home_page3.exit1()
        time.sleep(5)

if __name__=='__main__':
    unittest.main()


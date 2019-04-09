import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_homepage_login import HomePage_login
from pageobjects.discuz_homepage_search import HomePage_search
from pageobjects.discuz_homepage_exit import HomePage_exit
import time


class DiscuzSearch3(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = HomePage_login(self.driver)
        home_page1.login("grf","123456")
        home_page2=HomePage_search(self.driver)
        title=home_page2.search_title("haotest")
        home_page3=HomePage_exit(self.driver)
        home_page3.exit1()
        try:
            self.assertEqual(title,'haotest',msg=title)
            print('True')
        except:
            print('Failed')

if __name__=='__main__':
    unittest.main()
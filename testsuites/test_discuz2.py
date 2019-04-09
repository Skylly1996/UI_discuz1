import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_homepage_login import HomePage_login
from pageobjects.discuz_homepage_posting import HomePage_posting
from pageobjects.discuz_homepage_manage import HomePage_management
from pageobjects.discuz_homepage_exit import HomePage_exit
from pageobjects.discuz_homepage_newBK import HomePage_newBK1
import time


class DiscuzSearch2(BaseTestCase):
    def test_discuz_search(self):
        home_page1 = HomePage_login(self.driver)
        home_page1.login("admin",'admin')
        home_page2=HomePage_posting(self.driver)
        home_page2.postDelete()
        home_page3=HomePage_management(self.driver)
        home_page3.manage1()
        home_page3.addNew1("haotest")
        home_page4=HomePage_exit(self.driver)
        home_page4.exit1()
        home_page1.login("grf","123456")
        home_page5=HomePage_newBK1(self.driver)
        home_page5.addNewMessage("新板块","这是新板块的发帖")
        home_page5.replyNewMessage("回的帖")
        home_page4.exit1()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()
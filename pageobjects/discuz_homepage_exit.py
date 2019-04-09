from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage_exit(BasePage):
    home_page_exit_search_loc = (By.LINK_TEXT, '退出')  # 退出网页的登录登录
    def exit1(self):
        self.click(*self.home_page_exit_search_loc)
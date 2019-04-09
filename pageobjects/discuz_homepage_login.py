from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage_login(BasePage):
    # 登录
    home_page_username_search_loc = (By.ID, 'ls_username')# 输入用户名
    home_page_password_search_loc = (By.ID, 'ls_password')# 输入密码
    home_page_submit_search_loc=(By.CSS_SELECTOR,'.pn em')# 点击登录
    def login(self,username,pwd):
        self.sendkeys(username,*self.home_page_username_search_loc)
        self.sendkeys(pwd,*self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        time.sleep(2)
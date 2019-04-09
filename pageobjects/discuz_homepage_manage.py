from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage_management(BasePage):
    home_page_guanli_search_loc = (By.CSS_SELECTOR, '#um > p:nth-child(2) > a:nth-child(16)')  # 点击管理中心
    home_page_guanliPwd_search_loc = (By.XPATH, '//*[@id="loginform"]/p[4]/input')  # 进入管理板块的密码
    home_page_guanliButton_search_loc = (By.NAME, 'submit')  # 进入管理板块的提交按钮
    home_page_GLluntan_search_loc = (By.ID, 'header_forum')  # 进入管理中心的论坛
    home_page_iframe_search_loc = (By.XPATH, '//*[@id="main"]')  # 添加板块的iframe的名称
    home_page_addBK_search_loc = (By.CSS_SELECTOR, '.lastboard .addtr')  # 添加一个新板块的框架
    home_page_BKname_search_loc = (By.NAME, 'newforum[1][]')  # 删除板块内的名称并设置新板块的名称
    home_page_newBKname_search_loc = (By.ID, 'submit_editsubmit')  # 提交新的板块
    home_page_exitBK_search_loc = (By.LINK_TEXT, '退出')  # 退出管理板块的登录
    def manage1(self):#进入管理中心
        self.click(*self.home_page_guanli_search_loc)
        self.windows_qie(1)
        self.click(*self.home_page_GLluntan_search_loc)  # 进入这里的论坛界面
        self.iframe_use(0)

    def addNew1(self,BKname):#添加新板块,管理员退出管理界面
        self.click(*self.home_page_addBK_search_loc)  # 添加新的板块
        self.clear(*self.home_page_BKname_search_loc)
        self.sendkeys(BKname, *self.home_page_BKname_search_loc)  # 写入新的板块名称
        self.click(*self.home_page_newBKname_search_loc)  # 提交，完成新板块的搭建
        time.sleep(3)
        self.click(*self.home_page_exitBK_search_loc)
        self.windows_qie(0)


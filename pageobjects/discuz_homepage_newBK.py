from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage_newBK1(BasePage):
    home_page_newBK_search_loc = (By.CSS_SELECTOR, 'tr .common')  # 选择新的板块并进入
    home_page_title_search_loc = (By.ID, 'subject')  # 输入帖子标题
    home_page_message_search_loc = (By.CSS_SELECTOR, '.pt')  # 输入帖子正文
    home_page_postbutton_search_loc = (By.CSS_SELECTOR, 'p .pn strong')  # 发送新帖按钮
    home_page_reply_search_loc = (By.ID, 'fastpostmessage')  # 输入回帖
    home_page_replybutton_search_loc = (By.XPATH, '//*[@id="fastpostsubmit"]')  # 点击按钮发送回帖
    def addNewMessage(self,BKname,message):
        self.click(*self.home_page_newBK_search_loc)
        # 在新的板块下发帖
        self.sendkeys(BKname, *self.home_page_title_search_loc)
        self.sendkeys(message, *self.home_page_message_search_loc)
        self.click(*self.home_page_postbutton_search_loc)
        time.sleep(5)
        # 回帖
    def replyNewMessage(self,reply):
        self.sendkeys(reply, *self.home_page_reply_search_loc)
        self.click(*self.home_page_replybutton_search_loc)
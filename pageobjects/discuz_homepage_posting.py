from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage_posting(BasePage):
    home_page_newbutton1_search_loc = (By.LINK_TEXT, '默认板块')  # 进入默认板块
    home_page_title_search_loc = (By.ID, 'subject')  # 输入帖子标题
    home_page_message_search_loc = (By.CSS_SELECTOR, '.pt')  # 输入帖子正文
    home_page_postbutton_search_loc = (By.CSS_SELECTOR, 'p .pn strong')  # 发送新帖按钮
    home_page_reply_search_loc = (By.ID, 'fastpostmessage')  # 输入回帖
    home_page_replybutton_search_loc = (By.XPATH, '//*[@id="fastpostsubmit"]')  # 点击按钮发送回帖
    home_page_newbutton1_search_loc = (By.LINK_TEXT, '默认板块')  # 进入默认板块
    home_page_delete1_search_loc = (By.NAME, 'moderate[]')  # 选中要删除的帖子
    home_page_delete2_search_loc = (By.CSS_SELECTOR, '#mdly > p:nth-child(6) > strong:nth-child(1) > a')  # 点击删除按钮
    home_page_delete3_search_loc = (By.CSS_SELECTOR, '#modsubmit > span')
    def postNew(self,title,message):
        # assert '发帖' in self.driver.title
        self.click(*self.home_page_newbutton1_search_loc)
        self.get_windows_img()
        self.sendkeys(title,*self.home_page_title_search_loc)
        self.sendkeys(message,*self.home_page_message_search_loc)
        self.click(*self.home_page_postbutton_search_loc)
        time.sleep(5)
    def postReply(self,reply):
        self.click(*self.home_page_newbutton1_search_loc)
        self.sendkeys(reply,*self.home_page_reply_search_loc)
        self.click(*self.home_page_replybutton_search_loc)

    def postDelete(self):
        self.click(*self.home_page_newbutton1_search_loc)
        self.click(*self.home_page_delete1_search_loc)
        self.click(*self.home_page_delete2_search_loc)
        self.click(*self.home_page_delete3_search_loc)
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage_search(BasePage):
    home_page_search_search_loc=(By.CSS_SELECTOR,'td input')#搜索框
    home_page_searchButton_search_loc=(By.CSS_SELECTOR,'td button')#点击搜索
    home_page_searchTitle_search_loc=(By.CSS_SELECTOR,'strong font')#点进搜索到的内容
    home_page_Title_search_loc = (By.CLASS_NAME, 'ts')  # 进入被搜索的帖子后的标题
    def search_title(self,title):
        # 搜索框搜索
        self.sendkeys(title,*self.home_page_search_search_loc)
        self.click(*self.home_page_searchButton_search_loc)
        time.sleep(2)
        self.windows_qie(1)
        #跳转页面并点入搜索到的内容
        self.click(*self.home_page_searchTitle_search_loc)
        self.windows_qie(2)
        time.sleep(5)
        title=self.find_element(*self.home_page_Title_search_loc).text
        time.sleep(2)
        return title
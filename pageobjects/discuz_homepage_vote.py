from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

# 继承BasePage类
class HomePage_vote(BasePage):
    home_page_fatie_search_loc=(By.CSS_SELECTOR,'#newspecial > img')#发帖按键
    home_page_vote_search_loc=(By.CSS_SELECTOR,'#editorbox > ul > li:nth-child(2) > a')#投票界面
    home_page_tiezi_search_loc=(By.CSS_SELECTOR,'#category_1>table>tbody>tr:nth-child(1)>td:nth-child(2)>h2>a')#随机进入一个帖子
    home_page_voteTitle_search_loc=(By.CSS_SELECTOR,'#subject')#投票的标题
    home_page_voteButton1_search_loc = (By.CSS_SELECTOR,'#pollm_c_1>p:nth-child(1)>input')#投票的选项
    home_page_voteButton2_search_loc = (By.CSS_SELECTOR, '#pollm_c_1>p:nth-child(2)>input')  # 投票的选项
    home_page_voteSubmit_search_loc=(By.CSS_SELECTOR,'.pn span')#提交投票界面
    home_page_Title_search_loc=(By.CLASS_NAME,'ts')#进入被搜索的帖子后的标题
    home_page_votepiao_search_loc=(By.CLASS_NAME,'s xst')#进入投票帖子
    home_page_voteToupiao_search_loc=(By.NAME,'pollanswers[]')#选一个选项进行投票
    home_page_voteTouSumbit_search_loc=(By.CSS_SELECTOR,'.pn span')#提交投票结果
    home_page_adio_frame_search_loc= (By.CSS_SELECTOR, ".pcht tr")  # 找到选票的整个文本框
    home_page_option_title_search_loc = (By.ID, "thread_subject")  # 发起投票的标题
    def voting(self,title,votebutton1,votebutton2):
        # 进入一个帖子
        self.click(*self.home_page_tiezi_search_loc)
        time.sleep(3)
        #发起投票
        self.click(*self.home_page_fatie_search_loc)
        self.click(*self.home_page_vote_search_loc)
        time.sleep(2)
        #填写信息，发起投票
        self.sendkeys(title,*self.home_page_voteTitle_search_loc)
        time.sleep(2)
        self.sendkeys(votebutton1, *self.home_page_voteButton1_search_loc)
        self.sendkeys(votebutton2, *self.home_page_voteButton2_search_loc)
        self.click(*self.home_page_voteSubmit_search_loc)
        time.sleep(2)
        #随机投票
        self.click(*self.home_page_votepiao_search_loc)#进入投票帖子
        self.click(*self.home_page_voteToupiao_search_loc)#选一个选项进行提交
        self.click(*self.home_page_voteTouSumbit_search_loc)#提交结果
        time.sleep(5)
        #进行统计
        print("投票内容及所在比例", self.get_ratios(*self.home_page_adio_frame_search_loc))
        print(self.find_text(*self.home_page_option_title_search_loc))
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

# 继承BasePage类
class HomePage(BasePage):
    # 定位器，通过元素属性定位元素对象
    # 登录
    home_page_username_search_loc = (By.ID, 'ls_username')# 输入用户名
    home_page_password_search_loc = (By.ID, 'ls_password')# 输入密码
    home_page_submit_search_loc=(By.CSS_SELECTOR,'.pn em')# 点击登录
    home_page_newbutton1_search_loc=(By.LINK_TEXT,'默认板块')# 进入默认板块
    home_page_title_search_loc=(By.ID,'subject')# 输入帖子标题
    home_page_message_search_loc=(By.CSS_SELECTOR,'.pt')# 输入帖子正文
    home_page_postbutton_search_loc=(By.CSS_SELECTOR,'p .pn strong')# 发送新帖按钮
    home_page_reply_search_loc=(By.ID,'fastpostmessage')# 输入回帖
    home_page_replybutton_search_loc = (By.XPATH, '//*[@id="fastpostsubmit"]')  # 点击按钮发送回帖
    home_page_delete1_search_loc=(By.NAME,'moderate[]')#选中要删除的帖子
    home_page_delete2_search_loc=(By.CSS_SELECTOR,'#mdly > p:nth-child(6) > strong:nth-child(1) > a')# 点击删除按钮
    home_page_delete3_search_loc=(By.CSS_SELECTOR,'#modsubmit > span')
    home_page_guanli_search_loc=(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(16)')#点击管理中心
    home_page_guanliPwd_search_loc=(By.XPATH,'//*[@id="loginform"]/p[4]/input')#进入管理板块的密码
    home_page_guanliButton_search_loc=(By.NAME,'submit')#进入管理板块的提交按钮
    home_page_GLluntan_search_loc=(By.ID,'header_forum')#进入管理中心的论坛
    home_page_iframe_search_loc=(By.XPATH,'//*[@id="main"]')#添加板块的iframe的名称
    home_page_addBK_search_loc=(By.CSS_SELECTOR,'.lastboard .addtr')#添加一个新板块的框架
    home_page_BKname_search_loc = (By.NAME, 'newforum[1][]')#删除板块内的名称并设置新板块的名称
    home_page_newBKname_search_loc=(By.ID,'submit_editsubmit')#提交新的板块
    home_page_exitBK_search_loc = (By.LINK_TEXT, '退出')  # 退出管理板块的登录
    home_page_exit_search_loc=(By.LINK_TEXT,'退出')# 退出网页的登录登录
    home_page_newBK_search_loc=(By.CSS_SELECTOR,'tr .common')#选择新的板块并进入
    home_page_search_search_loc=(By.CSS_SELECTOR,'td input')#搜索框
    home_page_searchButton_search_loc=(By.CSS_SELECTOR,'td button')#点击搜索
    home_page_searchTitle_search_loc=(By.CSS_SELECTOR,'strong font')#点进搜索到的内容
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



    def search1(self,username,pwd,title,message,reply):
        self.sendkeys(username,*self.home_page_username_search_loc)
        self.sendkeys(pwd,*self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        time.sleep(3)
        # assert '发帖' in self.driver.title
        self.click(*self.home_page_newbutton1_search_loc)
        self.get_windows_img()
        self.sendkeys(title,*self.home_page_title_search_loc)
        self.sendkeys(message,*self.home_page_message_search_loc)
        self.click(*self.home_page_postbutton_search_loc)
        time.sleep(15)
        # 回帖
        self.sendkeys(reply,*self.home_page_reply_search_loc)
        self.click(*self.home_page_replybutton_search_loc)
        # 退出
        self.click(*self.home_page_exit_search_loc)



    def search2(self,username1,username2,pwd1,pwd2,BKname,reply,message):
        # 管理员登录
        self.sendkeys(username1,*self.home_page_username_search_loc)
        self.sendkeys(pwd1,*self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        # 进入默认板块
        self.click(*self.home_page_newbutton1_search_loc)

        # 删帖子
        self.click(*self.home_page_delete1_search_loc)
        self.click(*self.home_page_delete2_search_loc)
        self.click(*self.home_page_delete3_search_loc)
        # 进入管理中心
        self.click(*self.home_page_guanli_search_loc)
        self.windows_qie(1)
        # self.sendkeys(pwd1,*self.home_page_guanliPwd_search_loc)
        # self.click(*self.home_page_guanliButton_search_loc)#登陆成功
        self.click(*self.home_page_GLluntan_search_loc)#进入这里的论坛界面

        self.iframe_use(0)
        # time.sleep(3)
        self.click(*self.home_page_addBK_search_loc)#添加新的板块
        self.clear(*self.home_page_BKname_search_loc)
        self.sendkeys(BKname,*self.home_page_BKname_search_loc)#写入新的板块名称
        self.click(*self.home_page_newBKname_search_loc)#提交，完成新板块的搭建
        time.sleep(3)
        # 管理员退出管理中心界面
        self.click(*self.home_page_exitBK_search_loc)
        self.windows_qie(0)
        # 管理员退出
        self.click(*self.home_page_exit_search_loc)
        #用户登录
        self.sendkeys(username2, *self.home_page_username_search_loc)
        self.sendkeys(pwd2, *self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        time.sleep(5)
        # 进入新的板块
        self.click(*self.home_page_newBK_search_loc)
        # 在新的板块下发帖
        self.sendkeys(BKname,*self.home_page_title_search_loc)
        self.sendkeys(message,*self.home_page_message_search_loc)
        self.click(*self.home_page_postbutton_search_loc)
        time.sleep(15)
        # 回帖
        self.sendkeys(reply,*self.home_page_reply_search_loc)
        self.click(*self.home_page_replybutton_search_loc)
        # 退出
        self.click(*self.home_page_exit_search_loc)

    def search3(self,username,pwd,title):
        #登录
        self.sendkeys(username, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        time.sleep(2)
        # 搜索框搜索
        self.sendkeys(title,*self.home_page_search_search_loc)
        self.click(*self.home_page_searchButton_search_loc)
        time.sleep(2)
        self.windows_qie(1)
        #跳转页面并点入搜索到的内容
        self.click(*self.home_page_searchTitle_search_loc)
        self.windows_qie(2)
        title=self.find_element(*self.home_page_Title_search_loc).text
        # return title
        # time.sleep(2)
        #退出
        self.click(*self.home_page_exit_search_loc)
        time.sleep(2)
        return title

    def search4(self, username, pwd,title,votebutton1,votebutton2):
        # 登录
        self.sendkeys(username, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        self.click(*self.home_page_submit_search_loc)
        time.sleep(3)
        # 进入一个帖子
        self.click(*self.home_page_tiezi_search_loc)
        #发起投票
        self.click(*self.home_page_fatie_search_loc)
        self.click(*self.home_page_vote_search_loc)
        #填写信息，发起投票
        self.sendkeys(title,*self.home_page_voteTitle_search_loc)
        self.sendkeys(votebutton1, *self.home_page_voteButton1_search_loc)
        self.sendkeys(votebutton2, *self.home_page_voteButton2_search_loc)
        self.click(*self.home_page_voteSubmit_search_loc)
        #随机投票
        self.click(*self.home_page_votepiao_search_loc)#进入投票帖子
        self.click(*self.home_page_voteToupiao_search_loc)#选一个选项进行提交
        self.click(*self.home_page_voteTouSumbit_search_loc)#提交结果
        #进行统计
        print("投票内容及所在比例", self.get_ratios(*self.home_page_adio_frame_search_loc))
        print(self.find_text(*self.home_page_option_title_search_loc))
        #退出
        self.click(*self.home_page_exit_search_loc)





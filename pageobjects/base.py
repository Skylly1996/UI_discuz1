from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework2.logger import Logger
import time
import os.path


# create a Logger instance
logger=Logger(logger='BasePage').getlog()

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info('Click back on current page')

    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page')

    def open_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except Exception as e:
            logger.error('Failed to quit the browser with %s'%e)

    def find_element(self, *loc):  # 显式等待
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            # logger.error('找到页面元素---'%loc)
        except:
            print('')
            # logger.error("%s页面未找到%s元素" %loc)
     # 输入
    def sendkeys(self, text, *loc):
        el = self.find_element (* loc)
        try:
            el.send_keys(text)
            logger.info('输入内容%s'%(el).text)
        except Exception as e:
            logger.error('Failed to type in input box with %s' % e)
            # self.get_windows_img()

    # 清除文本框
    def clear(self, *loc):
        ele = self.find_element(*loc)
        try:
            ele.clear()
        except Exception as e:
            print('clear failed')

    def click(self, *loc):
        ele = self.find_element(*loc)
        try:
          ele.click()
        except Exception as e:
           print('')

# 保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder:/screenshots')
        except Exception as e:
            self.get_windows_img()
            logger.error('Failed  to take screenshots!%s' % e)

    # def get_windows_img(self):  #截图
    #     file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'  #找文件夹
    #     if not os.path.exists(file_path):
    #         os.mkdir(file_path)  #创建文件夹
    #     rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #     screen_name=file_path + rq + '.png'   #图片保存格式
    #     try:
    #         self.driver.get_screenshot_as_file(screen_name)
    #         logger.info('截图保存到 /screenshots')
    #     except Exception as e:
    #         self.get_windows_img()
    #         logger.error('获取截图失败，因为%s'%e)


    def windows_qie(self,x):#窗口切换
        self.driver.switch_to.window(self.driver.window_handles[x])

    def iframe_use(self,x):
        self.driver.switch_to.frame(x)

    def find_elements(self, *loc):  # 显式等待
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
            # logger.error('找到页面元素---'%loc)
        except:
            print('')

    def get_ratios(self, *loc):
        e1 = self.find_elements(*loc)
        ratio_list = []
        choice_list = []
        for i in range(0, len(e1) - 1):
            if i % 2 != 0:
                ratio_list.append(e1[i].text)
            else:
                choice_list.append(e1[i].text)
        return ratio_list, choice_list

    def find_text(self,*loc):#取得文本并返回
        el = self.find_element(*loc)
        text = el.text
        return text
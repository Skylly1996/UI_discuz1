import sys
sys.path.append('D:\python-webUI-DISCUZ')
import unittest
import HTMLTestRunner
import os
current_path=os.path.abspath(__file__)
a_path=os.path.dirname(current_path)
b_path=os.path.dirname(a_path)
from framework2.logger import Logger
from testsuites.test_discuz1 import DiscuzSearch1
from testsuites.test_discuz2 import DiscuzSearch2
from testsuites.test_discuz3 import DiscuzSearch3
from testsuites.test_discuz4 import DiscuzSearch4

file_path=os.path.dirname(os.path.abspath("."))+"/test_report"

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Logger))
suite.addTest(unittest.makeSuite(DiscuzSearch1))
suite.addTest(unittest.makeSuite(DiscuzSearch2))
suite.addTest(unittest.makeSuite(DiscuzSearch3))
suite.addTest(unittest.makeSuite(DiscuzSearch4))

if __name__=="__main__":
    html_report=file_path+r"\report.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="关于Discuz的测试报告")
    runner.run(suite)

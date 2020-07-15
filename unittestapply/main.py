import unittest
s=unittest.TestLoader().discover(r"/Users/zhl/Documents/lenmon/lesson/unittestapply")
#BeautifulReport
from BeautifulReport import BeautifulReport
br=BeautifulReport(s)
br.report('我的测试报告')
import unittest
import os
cases_dir=os.path.dirname(os.path.abspath(__file__))
s=unittest.TestLoader().discover(cases_dir)
#BeautifulReport
from BeautifulReport import BeautifulReport
br=BeautifulReport(s)
br.report('我的测试报告')
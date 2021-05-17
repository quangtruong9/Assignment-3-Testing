import unittest
import openpyxl 
from datetime import datetime
from selenium import webdriver
from TestUtils import TestUtil
import run

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(run.PATH)
        self.driver.get("https://www.vietnamworks.com/salary/all-jobs")
    
    #test case tương úng với test case trong file excel
    def test_TC_AM_001(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        result = True if self.driver.find_element_by_class_name("gross-number") else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-AM-001"))

    def tearDown(self):
        self.driver.close()


import unittest
import openpyxl 
from datetime import datetime
from selenium import webdriver
from TestUtils import TestUtil
from selenium.webdriver.support.ui import Select
import run


import time
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(run.PATH)
        self.driver.maximize_window()
        self.driver.get("https://www.vietnamworks.com/companies")

    def test_TC_EC_001(self):
        category = Select(self.driver.find_element_by_id('category-select'))
        category.select_by_value('35')

        self.driver.implicitly_wait(5)

        location = Select(self.driver.find_element_by_id('location-select'))
        location.select_by_value('29')

        self.driver.implicitly_wait(5)

        company = self.driver.find_element_by_id('company-name-search')
        company.send_keys('FPT')
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[@class='company-profile-group']/div[1]/div/div[1]/strong")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-001"))
    
    def test_TC_EC_002(self):
        category = Select(self.driver.find_element_by_id('category-select'))
        category.select_by_value('35')

        self.driver.implicitly_wait(5)

        location = Select(self.driver.find_element_by_id('location-select'))
        location.select_by_value('29')

        self.driver.implicitly_wait(5)

        company = self.driver.find_element_by_id('company-name-search')
        company.send_keys('FPT')
        time.sleep(2)

        index = Select(self.driver.find_element_by_id('index-select'))
        index.select_by_value('vnw_company_v1_followers_desc')

        try:
            self.driver.find_element_by_xpath("//div[@class='company-profile-group']/div[1]/div/div[1]/strong")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-002"))

    def test_TC_EC_003(self):
        category = Select(self.driver.find_element_by_id('category-select'))
        category.select_by_value('11')

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('btn-filter-company').click()
        time.sleep(2)

        index = Select(self.driver.find_element_by_id('index-select'))
        index.select_by_value('vnw_company_v1_views_desc')

        try:
            self.driver.find_element_by_xpath("//div[@class='company-profile-group']/div[1]/div/div[1]/strong")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-003"))
    
    def test_TC_EC_004(self):
        location = Select(self.driver.find_element_by_id('location-select'))
        location.select_by_value('24')

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('btn-filter-company').click()
        time.sleep(2)

        self.driver.find_element_by_id('company-list__set-open-jobs').click()

        try:
            self.driver.find_element_by_xpath("//div[@class='company-profile-group']/div[1]/div/div[1]/strong")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-004"))

    def test_TC_EC_005(self):
        company = self.driver.find_element_by_id('company-name-search')
        company.send_keys('FPT')
        time.sleep(2)

        index = Select(self.driver.find_element_by_id('index-select'))
        index.select_by_value('vnw_company_v1_firstPublishedOn_desc')

        try:
            self.driver.find_element_by_xpath("//div[@class='company-profile-group']/div[1]/div/div[1]/strong")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-005"))

    def test_TC_EC_006(self):
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element_by_id("slick-slide10")
            result = True
        except:
            result = False  
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-006"))

    def test_TC_EC_007(self):
        company = self.driver.find_element_by_id('company-name-search')
        company.send_keys('this is not real')
        time.sleep(2)

        try:
            self.driver.find_element_by_class_name("company-list__no-result")
            result = True
        except:
            result = False  

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-EC-007"))

    def tearDown(self):
        self.driver.close()

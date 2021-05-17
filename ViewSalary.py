import unittest
import openpyxl 
from datetime import datetime
from selenium import webdriver
from TestUtils import TestUtil
import run


import time
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(run.PATH)
        self.driver.maximize_window()
        self.driver.get("https://www.vietnamworks.com/salary/all-jobs")
    
    #test case tương úng với test case trong file excel
    def test_TC_VS_001(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()        
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        result = True if self.driver.find_element_by_class_name("gross-number") else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-001"))

    def test_TC_VS_002(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        result = True if self.driver.find_element_by_class_name("gross-number") else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-002"))
    
    def test_TC_VS_003(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()        
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        initial_val = self.driver.find_element_by_class_name('common-salary-number').text
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ha Noi']").click()
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        second_val = self.driver.find_element_by_class_name('common-salary-number').text
        result = initial_val==second_val
        self.assertTrue(TestUtil.checkTestcase(result,False,"TC-VS-003"))

    def test_TC_VS_004(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(3)
        initial_val = self.driver.find_element_by_class_name('gross-number').text

        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[2]").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[2]/div/div/div[2]/div[2]/div[3]").click()
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[2]").click()
        time.sleep(3)
        second_val = self.driver.find_element_by_class_name('gross-number').text
        result = initial_val == second_val
        self.assertTrue(TestUtil.checkTestcase(result,False,"TC-VS-004"))

    def test_TC_VS_005(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(3)
        initial_val = self.driver.find_element_by_class_name('gross-number').text

        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[3]").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[3]/div/div/div[2]/div[2]/div[3]").click()
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[3]").click()
        time.sleep(3)
        second_val = self.driver.find_element_by_class_name('gross-number').text
        result = initial_val == second_val
        self.assertTrue(TestUtil.checkTestcase(result,False,"TC-VS-005"))

    def test_TC_VS_006(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('Software Engineer')
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(3)
        initial_val = self.driver.find_element_by_class_name('gross-number').text

        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[4]").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[4]/div/div/div[2]/div[2]/div[2]").click()
        self.driver.find_element_by_xpath("//div[@class='left-bar']/div[4]").click()
        time.sleep(3)
        second_val = self.driver.find_element_by_class_name('gross-number').text
        result = initial_val == second_val
        self.assertTrue(TestUtil.checkTestcase(result,False,"TC-VS-006"))

    def test_TC_VS_007(self):
        search = self.driver.find_element_by_id('main-search-bar')
        search.send_keys('this is not real')
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(2)
        try:
            self.driver.find_element_by_class_name("gross-number")
            result = True
        except: 
            result = False
    
        self.assertTrue(TestUtil.checkTestcase(result,False,"TC-VS-007"))

    def test_TC_VS_008(self):
        initial_val = self.driver.find_element_by_tag_name('title').text
        self.driver.find_element_by_class_name("location-wrapper").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//div[@class='select-options']/div[@title='Ho Chi Minh']").click()
        self.driver.find_element_by_class_name("btn-search").click()
        self.driver.implicitly_wait(3)
        second_val = self.driver.find_element_by_tag_name('title').text

        result = initial_val == second_val
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-008"))

    def test_TC_VS_009(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//div[@class='tour-actions']/span[@class='close-action']").click()
        self.driver.find_element_by_xpath("//div[@class='job-panel-body']/div[1]/span[1]/a").click()
        self.driver.implicitly_wait(3)

        try:
            self.driver.find_element_by_class_name('gross-number')
            result = True
        except:
            result = False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-009"))

    def test_TC_VS_010(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//div[@class='tour-actions']/span[@class='close-action']").click()
        self.driver.find_element_by_xpath("//div[@class='list-jobItem']/div[1]/div[3]/span[2]").click()
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element_by_class_name('gross-number')
            result = True
        except:
            result = False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-010"))

    def test_TC_VS_011(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//div[@class='tour-actions']/span[@class='close-action']").click()
        search = self.driver.find_element_by_xpath("//div[@class='view-salary-by-job']/input")
        search.send_keys('Engineer')
        self.driver.find_element_by_xpath("//div[@class='view-salary-by-job']/a").click()
        self.driver.implicitly_wait(3)

        try:
            self.driver.find_element_by_class_name('gross-number')
            result = True
        except:
            result = False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-011"))

    def test_TC_VS_012(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//div[@class='tour-actions']/span[@class='close-action']").click()
        initial_val = self.driver.find_element_by_tag_name('title').text


        self.driver.find_element_by_xpath("//div[@class='view-salary-by-job']/a").click()
        self.driver.implicitly_wait(3)
        second_val = self.driver.find_element_by_tag_name('title').text
        result = initial_val == second_val
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-012"))

    def tearDown(self):
        self.driver.close()


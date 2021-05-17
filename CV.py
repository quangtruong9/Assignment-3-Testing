import unittest
import openpyxl 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from TestUtils import TestUtil
import run

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(run.PATH)
        self.driver.maximize_window()
        self.driver.get("https://wowcv.vietnamworks.com/en")
       
    
    #test case tương úng với test case trong file excel    
    def test_TC_CV_001(self):
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[1]/div[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[2]/div[2]/a').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('uchihaobito16081999@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="login__password"]').send_keys('Anhtripro113doma')
        self.driver.find_element_by_xpath('//*[@id="button-login"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="introduction-block"]/button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="pdfViewerContainer"]/div[4]/button').click()
        expect_text = "Also update this information into your VietnamWorks' profile."
        actual_text = self.driver.find_element_by_xpath('/html/body/div[20]/div[2]/div[2]/div/span').text
        result = True if expect_text in actual_text else False
        self.assertTrue(TestUtil.checkTestcase(result, True,"TC-CV-001"))

    def test_TC_CV_002(self):
        self.driver.find_element_by_xpath('//*[@id="introduction-block"]/button').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="scrollable-basicInfo"]/div[2]/div[1]/div[1]/div[2]/div/input').send_keys('Đức Trí')
        self.driver.find_element_by_xpath('//*[@id="scrollable-basicInfo"]/div[2]/div[1]/div[2]/div[2]/div/input').send_keys('Hoàng')
        self.driver.find_element_by_xpath('//*[@id="scrollable-basicInfo"]/div[2]/div[1]/div[3]/div[2]/div/input').send_keys('CEO')
        self.driver.find_element_by_xpath('//*[@id="scrollable-basicInfo"]/div[2]/div[1]/div[5]/div[2]/div/input').send_keys('10')
        self.driver.find_element_by_xpath('//*[@id="scrollable-contactInformation"]/div/div[1]/div[1]/div/div/div/input').send_keys('123123123333113312123@gmail.com')
        expect_text = 'Email is invalid'
        #actual_text = self.driver.find_element_by_xpath('//*[@id="scrollable-contactInformation"]/div/div[1]/div[1]/div/span[2]').text
        result = True if expect_text in self.driver.page_source else False

        self.assertTrue(TestUtil.checkTestcase(result, True,"TC-CV-002"))

    def test_TC_CV_003(self):
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[1]/div[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[3]/div[2]/div[2]/a').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('uchihaobito16081999@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="login__password"]').send_keys('Anhtripro113doma')
        self.driver.find_element_by_xpath('//*[@id="button-login"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="introduction-block"]/button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="scrollable-contactInformation"]/div/div[1]/div[1]/div/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="scrollable-contactInformation"]/div/div[1]/div[1]/div/div/div/input').send_keys('fakeemail@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="pdfViewerContainer"]/div[4]/button').click()
        expect_text = "Also update this information into your VietnamWorks' profile."
        actual_text = self.driver.find_element_by_xpath('/html/body/div[20]/div[2]/div[2]/div/span').text
        result = False if expect_text in actual_text else True
        self.assertTrue(TestUtil.checkTestcase(result, False,"TC-CV-003"))
        

    def tearDown(self):
        self.driver.close()


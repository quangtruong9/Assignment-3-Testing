from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import xlwt
from xlwt import Workbook
import unittest
import openpyxl 
from datetime import datetime
from TestUtils import TestUtil
import run

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(run.PATH)
        self.driver.get("https://secure.vietnamworks.com/login/en?client_id=3&utm_source=&utm_medium=Header")
    
    #test case tương úng với test case trong file excel
    def test_TC_LI_001(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('dkhuong992810@gmail.com')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('dinhkhuong991')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "Wrong email or password. Please check again."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-001"))

    def test_TC_LI_002(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('a@dummy.com')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "Invalid email."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-002"))

    def test_TC_LI_003(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('dummyemail')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "The Email must be a valid Email address."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-003"))

    def test_TC_LI_004(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('asdblakbfoiu1be12inlk;jakqbhowidboiboib2og@ajshbdflakjhb')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "The Email must be a valid Email address."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-004"))

    def test_TC_LI_005(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('dummyemail@gmail.com')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('dummy123')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "Wrong email or password. Please check again."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-005"))

    def test_TC_LI_006(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[1]/span/strong').text
        expect = "The Email field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-006"))

    def test_TC_LI_007(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys('dummyemail@gmail.com')
        password = self.driver.find_element(By.ID,"login__password")
        password.send_keys('')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-login")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="form-login"]/div[2]/span/strong').text
        expect = "The Password field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-LI-007"))

    def tearDown(self):
        self.driver.close()
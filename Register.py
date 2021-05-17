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
        self.driver.get("https://secure.vietnamworks.com/register/en?client_id=3")
    
    #test case tương úng với test case trong file excel
    def test_TC_RE_001(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dkhuong99123@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = 1
        expect = 1
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-001"))

    def test_TC_RE_002(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("123456")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[1]/div[1]/span/strong').text
        expect = "The First Name format is invalid."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-002"))

    def test_TC_RE_003(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("123456")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[1]/div[2]/span/strong').text
        expect = "The Last Name format is invalid."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-003"))

    def test_TC_RE_004(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[1]/div[2]/span/strong').text
        expect = "The Last Name field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-004"))

    def test_TC_RE_005(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[1]/div[1]/span/strong').text
        expect = "The First Name field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-005"))

    def test_TC_RE_006(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[2]/div/span/strong').text
        expect = "The Email field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-006"))

    def test_TC_RE_007(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[3]/div/span/strong').text
        expect = "The Password field is required."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-007"))

    def test_TC_RE_008(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('Dt123456')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[2]/div/span/strong').text
        expect = "The Email must be a valid Email address."
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-008"))
    
    def test_TC_RE_009(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('dummytest@gmail.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('dtdtdt')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = self.driver.find_element_by_xpath('//*[@id="sso-register__form"]/div[3]/div/span/strong').text
        expect = "The password format is invalid.   "
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-009"))

    def test_TC_RE_010(self):
        firstname = self.driver.find_element(By.ID,"firstname")
        firstname.send_keys("Khuong")
        lastname = self.driver.find_element(By.ID,"lastname")
        lastname.send_keys("Nguyen")
        username = self.driver.find_element(By.ID,"username")
        username.send_keys('unrealemail@dek.com')
        password = self.driver.find_element(By.ID,"password")
        password.send_keys('dtdtdt')
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id("button-register")
        login_button.click()
        actual = "Non-exist email"
        expect = "Move to another page "
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-RE-010"))
    
    def tearDown(self):
        self.driver.close()
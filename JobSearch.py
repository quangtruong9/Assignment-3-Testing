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
        self.driver.get("https://www.vietnamworks.com/ho-chi-minh-jobs-v29-en")
        
    #test case tương úng với test case trong file excel
    # def test_TC_VS_001(self):
    #     search = self.driver.find_element_by_id('main-search-bar')
    #     search.send_keys('Software Engineer')
    #     self.driver.find_element_by_class_name("btn-search").click()
    #     self.driver.implicitly_wait(2)
    #     result = True if self.driver.find_element_by_class_name("gross-number") else False

    #     self.assertTrue(TestUtil.checkTestcase(result,True,"TC-VS-001"))

    def test_TC_JO_001(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        search.send_keys('IT',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        self.driver.implicitly_wait(6)
        self.driver.implicitly_wait(5)
        expect_text = 'jobs matched'
        expect_jobs = 'IT'
        expect_place = 'Ho Chi Minh'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_jobs in actual_jobs and expect_text in actual_text and expect_place in actual_place else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-JO-001"))
    
    def test_TC_JO_002(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        search.send_keys('sugar daddy',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'We have not found jobs for this search at the moment'
        self.driver.implicitly_wait(10)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[1]/div[1]/div/h1').text
        result = True if  expect_text in actual_text else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-002"))

    def test_TC_JO_003(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        search.send_keys('"SELECT * from users"',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'We have not found jobs for this search at the moment'
        self.driver.implicitly_wait(10)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[1]/div[1]/div/h1').text
        result = True if expect_text in actual_text else False
        
        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-003"))

    def test_TC_JO_004(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        self.driver.implicitly_wait(10)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-004"))

    def test_TC_JO_005(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ha Noi')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ha Noi'
        self.driver.implicitly_wait(10)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-005"))

    def test_TC_JO_006(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Mars')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Mars'
        self.driver.implicitly_wait(10)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs else False

        self.assertTrue(TestUtil.checkTestcase(result, False, "TC-JO-006"))

    def test_TC_JO_007(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ho Chi Minh')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/input').send_keys("IT")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        expect_category = 'IT - Software'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong[2]').text
        actual_category = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong[1]').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs and expect_category == actual_category else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-007"))

    def test_TC_JO_008(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ho Chi Minh')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[4]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-008"))

    def test_TC_JO_009(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ho Chi Minh')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[1]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[3]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'jobs matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        self.driver.implicitly_wait(2)
        not_found_result = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[1]/div[1]/div/h1').text
        expect_not_found_result = 'We have not found jobs for this search at the moment'
        result = True if expect_not_found_result in not_found_result else False

        self.assertTrue(TestUtil.checkTestcase(result, False, "TC-JO-009"))


    def test_TC_JO_010(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ho Chi Minh')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-010"))

    def test_TC_JO_011(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/input').send_keys('Ho Chi Minh')
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[2]/div[1]/div/div[2]/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div').click()
        search.send_keys('Computer Science Engineer',Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="main-search-bar"]').clear()
        expect_text = 'matched'
        expect_jobs = 'Computer Science Engineer'
        expect_place = 'Ho Chi Minh'
        expect_time = 'Full-time'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]').text
        actual_jobs = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/strong').text
        actual_place = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong[2]').text
        actual_time = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[2]/strong[1]').text
        result = True if expect_text in actual_text and expect_place in actual_place and expect_jobs in actual_jobs and expect_time in actual_time else False

        self.assertTrue(TestUtil.checkTestcase(result, True, "TC-JO-0011"))

    def test_TC_JO_012(self):
        search = self.driver.find_element(By.ID,"main-search-bar")
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[4]/div/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("aaa111333222a@gmail.com")
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/form/div[2]/div[2]/button').click()
        expect_text = 'Please enter a valid Email address.'
        self.driver.implicitly_wait(2)
        actual_text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/form/div[6]/label').text
        result = True if expect_text in actual_text else False

        self.assertTrue(TestUtil.checkTestcase(result, False, "TC-JO-0012"))

    def tearDown(self):
        self.driver.close()


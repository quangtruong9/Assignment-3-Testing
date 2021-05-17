import sys
import os
import platform
import json
import re
import hashlib
import urllib
from time import sleep as delay
import pywinauto
import pygetwindow as gw
import pyautogui

import validators
import pandas as pd
from datetime import datetime, date, timedelta
from time import time
from datetime import datetime
from urllib.parse import urlsplit
from urllib.parse import urlparse
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import selenium.common.exceptions
from selenium.webdriver import ActionChains
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)

import xlwt
from xlwt import Workbook
import unittest
import openpyxl 
from datetime import datetime
from TestUtils import TestUtil
import run


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):

        self.input_files_path = os.path.join(os.path.abspath(os.getcwd()), "input_files")

        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # hide popup
        # chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--log-level=OFF')
        
        self.driver = webdriver.Chrome(executable_path = run.PATH, chrome_options=chrome_options)

        url = "https://www.vietnamworks.com/dang-nhap?type=login&redirectURL=https%3A%2F%2Fwww.vietnamworks.com%2F%3Futm_source%3D%26utm_medium%3DHeader"
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        except TimeoutException:
            return

        email = self.driver.find_element_by_id("email")
        email.send_keys("ngthquoczinh@gmail.com")

        passw = self.driver.find_element_by_id("login__password")
        passw.send_keys("(vnw)NG1-EU1-MI1")

        login = self.driver.find_element_by_id("button-login")
        login.click()

    def set_input(self, xpath, value):
        try:
            _input = self.driver.find_element_by_xpath(xpath)
            _input.send_keys(Keys.CONTROL, 'a')
            _input.send_keys(value)
            return True
        except:
            return False

    def select_search(self, xpath, key):
        try:
            dropbox = self.driver.find_element_by_xpath(xpath)
            if dropbox.find_element_by_class_name("active-item").text != key:
                dropbox.click()
                delay(0.5)
                dropbox.find_element_by_css_selector(".input-item > input").send_keys(key)
                delay(0.5)
                dropbox.find_element_by_css_selector(".select-options > div").click()
            return True
        except:
            return False

    def _test_TC_PM_001(self):
        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"/html/body/div[1]/div/div[6]/div[2]/div[1]"))).click()
        
        input_first_name = "//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/input"
        self.set_input(input_first_name, "Quoc Minh")

        input_last_name = "//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/input"
        self.set_input(input_last_name, "Nguyen")

        input_job_title = "//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[3]/div[1]/div[3]/div[2]/div/input"
        self.set_input(input_job_title, "IT")

        _job_level = "Entry Level"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[1]/div/div[3]/div[1]/div[4]/div[2]/div/div""",
            _job_level
        )

        self.driver.find_element_by_xpath("//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[3]/div[3]/div[2]/button[2]").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = "success" in response
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-001"))

    def _test_TC_PM_002(self):
        self.driver.get("https://www.vietnamworks.com/my-profile")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div"))).click()
        
        delay(0.5)
        window = pyautogui.getWindowsWithTitle(self.driver.title)[0]
        window.maximize
        window.center
        # pyautogui.click(window.center)
        # cv_file1 = "C:\\Users\\Minh\\Downloads\\vs_buildtools.exe"
        cv_file1 = os.path.join(self.input_files_path, "image.jpg")
        pyautogui.write(cv_file1)
        delay(0.5)
        pyautogui.press('enter')
        delay(0.5)
        ava_update_warining = "ok"
        try:
            ava_update_warining = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div[3]")
        except:
            ""
        actual = False
        if ava_update_warining == "ok":
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]").click()
            actual = True
        else:
            "Failed"
            # print("failed")

        
        expect = True
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-002"))


    def test_TC_PM_003(self):
        self.driver.get("https://www.vietnamworks.com/my-profile")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div"))).click()
        
        delay(0.5)
        window = pyautogui.getWindowsWithTitle(self.driver.title)[0]
        window.maximize
        window.center
        cv_file1 = os.path.join(self.input_files_path, "image.exe")
        pyautogui.write(cv_file1)
        delay(0.5)
        pyautogui.press('enter')
        delay(0.5)
        ava_update_warining = "ok"
        try:
            ava_update_warining = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div[3]")
        except:
            ""
        actual = False
        if ava_update_warining == "ok":
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]").click()
            actual = True
        else:
            "Failed"
            # print("failed")

        
        expect = True
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-003"))

    # def test_TC_PM_004(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-004"))

    # def test_TC_PM_005(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-005"))

    # def test_TC_PM_006(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-006")) 

    # def test_TC_PM_007(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-007"))

    # def test_TC_PM_008(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-008"))

    # def test_TC_PM_009(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-009"))

    # def test_TC_PM_010(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-010"))

    # def test_TC_PM_011(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-011"))

    # def test_TC_PM_012(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-012")) 

    # def test_TC_PM_013(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-013"))

    # def test_TC_PM_014(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-014")) 

    # def test_TC_PM_015(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-015"))

    # def test_TC_PM_016(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-016"))

    # def test_TC_PM_017(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-017"))

    # def test_TC_PM_018(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-018"))

    # def test_TC_PM_019(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-019"))

    # def test_TC_PM_020(self):
    #     self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-0020"))

    def tearDown(self):
        ""
        # self.driver.close() 
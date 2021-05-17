import sys
import os
import platform
import json
import re
import hashlib
import urllib
from time import sleep as delay
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
        chrome_options.add_argument("--window-size=1920,1080")
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
        # try:
        _input = self.driver.find_element_by_xpath(xpath)
        _input.send_keys(Keys.CONTROL, 'a')
        _input.send_keys(value)
        return True
        # except:
        #     return False

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
        """ Update basic info """

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
        """ Update ava profile with IMG file """

        self.driver.get("https://www.vietnamworks.com/my-profile")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div"))).click()
        
        delay(0.5)
        window = pyautogui.getWindowsWithTitle(self.driver.title)[0]
        window.maximize
        window.center
        delay(1)
        ava_file1 = os.path.join(self.input_files_path, "image.jpg")
        pyautogui.write(ava_file1)
        delay(0.5)
        pyautogui.press('enter')
        delay(1)
        ava_update_warining = "ok"
        try:
            ava_update_warining = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div[3]")
        except:
            ""
        delay(1)
        actual = False
        if ava_update_warining == "ok":
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]").click()
            actual = True
        else:
            "Failed"
        
        expect = True
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-002"))


    def _test_TC_PM_003(self):
        """ Update ava profile with EXE file """

        self.driver.get("https://www.vietnamworks.com/my-profile")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div"))).click()
        
        delay(0.5)
        window = pyautogui.getWindowsWithTitle(self.driver.title)[0]
        window.maximize
        window.center
        delay(1)
        ava_file2 = os.path.join(self.input_files_path, "image.exe")
        pyautogui.write(ava_file2)
        delay(0.5)
        pyautogui.press('enter')
        delay(0.5)
        ava_update_warining = "ok"
        try:
            ava_update_warining = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[6]/div[2]/div[1]/div/div[1]/div/div[3]")
        except:
            ""
        delay(1)
        actual = False
        if ava_update_warining == "ok":
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/button[2]").click()
            actual = True
        else:
            "Failed"
            # print("failed")

        
        expect = False
        result = True if (actual == expect) else False
        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-003"))

    def _test_TC_PM_004(self):
        """ Right contact info """
        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "0946372514"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "17/9/1999"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Local Vietnamese"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )

        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )

        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(expect,True,"TC-PM-004"))

    def _test_TC_PM_005(self):
        """ Wrong phone number """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "9999999999"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "17/9/1999"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Local Vietnamese"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )

        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-005"))

    def _test_TC_PM_006(self):
        """ Wrong date-of-birth """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Local Vietnamese"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )

        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-006"))

    def _test_TC_PM_007(self):
        """ Foreigner in Vietnam """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )

        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-007"))

    def _test_TC_PM_008(self):
        """ Empty Nationality """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = ""
        try:
            self.select_search(
                """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
                _nationality
            )
        except:
            ""

        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-008"))

    def test_TC_PM_009(self):
        """ Fake address """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )


        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "123456 ABCD EFGH DONT KNOW"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-009"))

    def _test_TC_PM_010(self):
        """ Invalid address """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )


        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )
        
        _address = "<script> alert('alert') </script>"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-010"))

    def _test_TC_PM_011(self):
        """ Empty district """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "094637251"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )


        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = ""
        try:
            self.select_search(
                """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
                _district
            )
        except:
            ""
        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-011"))

    def _test_TC_PM_012(self):
        """ Long phone number """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "0239257298732482374923"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )


        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )

        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-012"))

    def _test_TC_PM_013(self):
        """ Invalid phone number with alphabet characters """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"//*[@id='__next']/div/div[6]/div[2]/div[3]/div/div"))).click()

        _cell_number = "0923n4877h"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/input""",
            _cell_number
        )

        _date_of_b = "35/5/2119"
        self.set_input(
            """/html/body/div[1]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/div/div/div/div/input""",
            _date_of_b
        )

        _nationality = "Foreigner"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div""",
            _nationality
        )


        _country = "Vietnam"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/div/div""",
            _country
        )

        _province = "Ho Chi Minh"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[1]/div/div/div""",
            _province
        )

        _district = "District 2"
        self.select_search(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[5]/div[2]/div/div""",
            _district
        )

        
        _address = "1 Thao Dien"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[6]/div/div/div/div/input""",
            _address
        )

        self.driver.execute_script("""document.getElementById("marital-status-1-radio").click()""")

        delay(0.1)
        self.driver.execute_script("""document.getElementById("gender-1-radio").click()""")

        # submit
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[3]/div/div/div[7]/div[2]/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-013"))

    def _test_TC_PM_014(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        sumary_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[4]""")))

        try:
            sumary_block.find_element_by_class_name("globalAddButton").click()
        except:
            try:
                sumary_block.find_element_by_class_name("EditIcon").click()
            except:
                ""
        sumary_content = "Hello, World! I am Selenium"
        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/div""").send_keys(sumary_content)

        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[2]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-014"))

    def _test_TC_PM_015(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        sumary_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[4]""")))

        try:
            sumary_block.find_element_by_class_name("globalAddButton").click()
        except:
            try:
                sumary_block.find_element_by_class_name("EditIcon").click()
            except:
                ""
        sumary_content = "Link: https://www.google.com.vn/"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/div""",
            sumary_content
        )

        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[2]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-015"))

    def _test_TC_PM_016(self):
        """ Long sumary characters """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        sumary_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[4]""")))

        try:
            sumary_block.find_element_by_class_name("globalAddButton").click()
        except:
            try:
                sumary_block.find_element_by_class_name("EditIcon").click()
            except:
                ""
        sumary_content = "Hello, World! I am Selenium "*10
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/div""",
            sumary_content
        )

        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[2]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-016"))

    def _test_TC_PM_017(self):
        """ Another sumary """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        sumary_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[4]""")))

        try:
            sumary_block.find_element_by_class_name("globalAddButton").click()
        except:
            try:
                sumary_block.find_element_by_class_name("EditIcon").click()
            except:
                ""
        sumary_content = "Hello, World! \n\n\n I am Selenium"
        self.set_input(
            """//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/div""",
            sumary_content
        )

        self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[4]/div/div[2]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-017"))

    def _test_TC_PM_018(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        education_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[6]""")))

        try:
            education_block.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[6]/div/div[2]/div/div/div/div/div[3]""").click()
        except:
            try:
                education_block.find_element_by_class_name("globalAddButton").click()
            except:
                ""

        _subject = "Programming"
        self.set_input(
            """//*[@id="education-form-0"]/div[2]/div[1]/div/div/div[2]/input""",
            _subject
        )

        _school = "ABCDEFGH University"
        self.set_input(
            """//*[@id="education-form-0"]/div[2]/div[2]/div[1]/div/div[2]/input""",
            _school
        )

        _qualification = "Bachelors"
        self.select_search(
            """//*[@id="education-form-0"]/div[2]/div[2]/div[2]/div/div[2]""",
            _qualification
        )

        self.driver.find_element_by_xpath("""//*[@id="education-form-0"]/div[3]/div[2]/button[3]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-018"))

    def _test_TC_PM_019(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        education_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[7]""")))

        education_block.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]""").click()
        _skill = "IT Software"
        if len(education_block.find_elements_by_class_name("list-added-skills")) == 0:

            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/button[2]""").click()
        else:
            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[4]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-019"))

    def _test_TC_PM_020(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        education_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[7]""")))

        education_block.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]""").click()
        _skill = "It is not job, it is spam"
        if len(education_block.find_elements_by_class_name("list-added-skills")) == 0:

            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/button[2]""").click()
        else:
            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[4]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-020"))

    def _test_TC_PM_021(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        education_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[7]""")))

        education_block.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]""").click()
        _skill = "It is not job, it is spam"
        if len(education_block.find_elements_by_class_name("list-added-skills")) == 0:

            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/button[2]""").click()
        else:
            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[4]/div/button[1]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = False
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-021"))

    def _test_TC_PM_022(self):
        """  """

        self.driver.get("https://www.vietnamworks.com/my-profile")
        education_block = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,"""//*[@id="__next"]/div/div[6]/div[2]/div[7]""")))

        education_block.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]""").click()
        _skill = "123456789"
        if len(education_block.find_elements_by_class_name("list-added-skills")) == 0:

            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[2]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/button[2]""").click()
        else:
            self.set_input(
                """//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[3]/div/div[1]/div/div/input""",
                _skill
            )
            self.driver.find_element_by_xpath("""//*[@id="__next"]/div/div[6]/div[2]/div[7]/div/div[4]/div/button[2]""").click()

        delay(0.5)
        response = self.driver.find_element_by_xpath("//*[@id='__next']/div/div[7]").text

        actual = False
        if "success" in response:
            actual = True
                
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-022"))

    def _test_TC_PM_023(self):
        self.driver.get("https://www.vietnamworks.com/my-career-center/dashboard")
        
        
        button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH,
            """//*[@id="profileUploadAttachForm"]/div[1]/a""")))
        
        self.driver.execute_script(
        """
            function getElementByXpath(path) {
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            }
            getElementByXpath("//*[@id='profileUploadAttachForm']/div[1]/a").click()
        """)

        upload_cv_button = self.driver.find_element_by_class_name(
            "drag-drop-area")
        upload_cv_button.click()

        delay(0.5)
        window = pyautogui.getWindowsWithTitle(self.driver.title)[0]
        window.maximize
        window.center
        delay(1)
        cv_file1 = os.path.join(self.input_files_path, "100kb.pdf")
        pyautogui.write(cv_file1)
        delay(0.2)
        pyautogui.press('enter')
        delay(4)
        result = "none"
        try:
            result = self.driver.find_element_by_css_selector(
            "body > div:nth-child(2) > div > div.modal.fade.global__upload-cv-modal.in > div > div > div.upload-progress.row > div.step.first-step.col-md-5.text-center.completed")
            result = result.text
        except:
            ""
        # print(result)
        actual = False
        if result=='UPLOAD CV':
            actual = True
        else:
            """print("failed")"""
                        
        expect = True
        result = True if (actual == expect) else False

        self.assertTrue(TestUtil.checkTestcase(result,True,"TC-PM-022"))

    def tearDown(self):
        ""
        self.driver.close() 
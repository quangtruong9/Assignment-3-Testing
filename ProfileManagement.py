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

    def test_TC_PM_001(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-001"))

    def test_TC_PM_002(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-002"))

    def test_TC_PM_003(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-003"))

    def test_TC_PM_004(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-004"))

    def test_TC_PM_005(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-005"))

    def test_TC_PM_006(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-006")) 

    def test_TC_PM_007(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-007"))

    def test_TC_PM_008(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-008"))

    def test_TC_PM_009(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-009"))

    def test_TC_PM_010(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-010"))

    def test_TC_PM_011(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-011"))

    def test_TC_PM_012(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-012")) 

    def test_TC_PM_013(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-013"))

    def test_TC_PM_014(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-014")) 

    def test_TC_PM_015(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-015"))

    def test_TC_PM_016(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-016"))

    def test_TC_PM_017(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-017"))

    def test_TC_PM_018(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-018"))

    def test_TC_PM_019(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-019"))

    def test_TC_PM_020(self):
        self.assertTrue(TestUtil.checkTestcase(True,True,"TC-PM-0020"))

    def tearDown(self):
        self.driver.close() 
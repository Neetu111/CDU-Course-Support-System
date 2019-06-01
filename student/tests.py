# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class CreateStudyPlan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_study_plan(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/student/")
        driver.find_element_by_id("id_CourseCode").click()
        Select(driver.find_element_by_id("id_CourseCode")).select_by_visible_text("XENG01")
        driver.find_element_by_id("id_Field").click()
        driver.find_element_by_id("id_Semester").click()
        Select(driver.find_element_by_id("id_Semester")).select_by_visible_text("1")
        driver.find_element_by_id("id_Year").click()
        Select(driver.find_element_by_id("id_Year")).select_by_visible_text("3")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Year:'])[1]/following::button[1]").click()
        self.accept_next_alert = True
        driver.find_element_by_id("unit1").click()
        self.assertEqual(
            "Selected Unit \nDesign and Innovation: Communicating Technology-CUC106\nNo pre-requisite required",
            self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SMA209'])[1]/following::input[1]").click()
        self.accept_next_alert = True
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='CUC106'])[1]/following::label[1]").click()
        self.assertEqual("Selected Unit \nCultural Intelligence and Capability-CUC107\nNo pre-requisite required",
                         self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SMA209'])[1]/following::input[1]").click()
        self.accept_next_alert = True
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ENG151'])[1]/following::label[1]").click()
        self.assertEqual(
            "Selected Unit \nProcess Analysis-ENG246\nFollowing pre-requisite are required \nConfirm that you have passed these units",
            self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SMA209'])[1]/following::input[1]").click()
        self.accept_next_alert = True
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ENG247'])[1]/following::label[1]").click()
        self.assertEqual(
            "Selected Unit \nSeparation Process Principles-ENG341\nFollowing pre-requisite are required \nConfirm that you have passed these units",
            self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SMA209'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Separation Process Principles'])[1]/following::input[3]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SE'])[2]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='SE'])[2]/following::button[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
from selenium import webdriver
from student.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time





class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self, CourseCode):
        self.browser = webdriver.Chrome('testing/chromedriver.exe')


    def tearDown(self, CourseCode):
        self.browser.close()


    def tests_no_project_alert_is_displayed(self, CourseCode):
        self.browser.get(self.live_server_url)
        time.sleep(20)
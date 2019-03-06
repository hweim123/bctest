# encoding=utf-8
#author

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
    def login(self):
        try:
            wait = WebDriverWait(driver, 10, 0.2)
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(""))
        // *[ @ id = "page-login"] / div[2] / div / div[2] / div / div[1] / input
        // *[ @ id = "page-login"] / div[2] / div / div[2] / div / div[1] / input

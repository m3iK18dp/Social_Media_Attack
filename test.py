#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
import threading
from optparse import *
import time
import sys
import io
import os
try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
try:
    import requests
except:
    os.system("pip install requests")
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip install colorama")
import os
# os.system('taskkill /f /im geckodriver.exe')
# os.system('taskkill /f /im firefox.exe')


# browser = webdriver.Firefox()
# browser.implicitly_wait(5)
# browser.get("https://accounts.hahalolo.com/sign-in/")
# browser.find_element(By.ID, "accountId").send_keys('pk4824829@gmail.com')
# browser.find_element(By.ID, "password").send_keys('Abcde@12345')
# print(browser.find_element_by_tag_name('html').id)
# browser.find_element(
#     By.XPATH, "//div[@id='app']/div/div/div/div/div[2]/div/div/div/div[2]").click()
# time.sleep(2)
# print(browser.find_element_by_tag_name('html').id)
# def send_keys(element, key):
#     for s in list(key):
#         element.send_keys(s)
#         time.sleep(0.01)


# brows = webdriver.Firefox()
# brows.set_window_size(960, 540)
# brows.set_page_load_timeout(30)
# brows.implicitly_wait(5)
# brows.get("https://identity.flickr.com/login")
# send_keys(brows.find_element(
#     By.XPATH, "//input[@id='login-email']"), 'pk4824829@gmail.com')
# brows.find_element(
#     By.XPATH, "//form/button").click()
# time.sleep(2)
# send_keys(brows.find_element(
#     By.XPATH, "//input[@id='login-password']"), '123456789')
# brows.find_element(
#     By.XPATH, "//form/button").click()
# time.sleep(2)
# brows.find_element(
#     By.XPATH, "//input[@id='login-password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
# try:
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.set_page_load_timeout(120)
driver.get("https://myspace.com/signup")
button = driver.find_element(
    By.XPATH, "//button[@class='emaillogin massive']").send_keys(Keys.ENTER)
driver.find_element(
    By.XPATH, "//input[@id='signupEmailEmail']").send_keys("pk4824829@gmail.com")
driver.find_element(
    By.XPATH, "//input[@id='signupEmailPassword']").send_keys("pk4824829@gmail.com")
time.sleep(2)
driver.implicitly_wait(15)
if "This email address was already used to create an account. Try using another" in driver.find_element(By.XPATH, "//input[@id='signupEmailEmail']/../p/div/div[2]").text:
    print("1")
# except:
#     print
# finally:
driver.quit()
print("2")

#!/usr/bin/python
# -*- coding: utf-8 -*-
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
try:
    import requests
except:
    os.system("pip install requests")
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip install colorama")


def search_social_media_from_gmail(gmail):
    # [[function,result,social_media_name,webdriver,status]]
    social_medias = [[facebook, False, 'facebook', None, False],
                     [instagram, False, 'instagram', None, False]]
    ops = Options()
    ops.headless = True
    for social_media in social_medias:
        threading.Thread(
            target=social_media[0], args=(ops, gmail, social_media), name=social_media[2], daemon=True).start()
    time.sleep(5)
    while len(social_medias) != 0:
        for social_media in social_medias:
            sm = social_media
            print(sm)
            if sm[4]:
                if social_media[1]:
                    print(Fore.LIGHTGREEN_EX+"[V] " +
                          social_media[2] + Fore.RESET)
                if social_media[3] != None:
                    time.sleep(0.5)
                    social_media[3].quit()
                social_medias.remove(social_media)
        time.sleep(1)
    for social_media in social_medias:
        print(social_media)


def facebook(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.facebook.com/login/identify")
        driver.find_element(
            By.XPATH, "//input[@id='identify_email']").send_keys(gmail)
        old_id = driver.find_element_by_tag_name('html').id
        driver.find_element(By.XPATH, "//button[@id='did_submit']").click()
        time.sleep(5)
        if old_id != driver.find_element_by_tag_name('html').id:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def instagram(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.instagram.com/accounts/password/reset/")
        driver.find_element(
            By.XPATH, "//form/label/input").send_keys(gmail)
        old_id = driver.find_element_by_tag_name('html').id
        driver.find_element(
            By.XPATH, "//main/div[2]/div/div/div/div/div[5]/button").click()
        time.sleep(5)
        if old_id != driver.find_element_by_tag_name('html').id:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


search_social_media_from_gmail("pk4824829@gmail.com")

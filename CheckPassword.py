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
from selenium.webdriver.support.select import Select
try:
    import requests
except:
    os.system("pip install requests")
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip install colorama")


def search_social_media_from_gmail(gmail):
    # [[function, result, social_media_name, webdriver, status]]
    # social_medias = [[facebook, False, 'Facebook', None, False],
    #                  [instagram, False, 'Instagram', None, False],
    #                  [tiktok, False, 'Tiktok', None, False],
    #                  [twitter, False, 'Twitter', None, False],
    #                  [youtube, False, 'Youtube', None, False]
    # [hahalolo, False, 'Hahalolo', None, False],
    #                  [biztime, False, 'Biztime', None, False],
    #                  [flickr, False, 'Flickr', None, False],
    #                  [tumblr, False, 'Tumblr', None, False],
    #                  [snapchat, False, 'Snapchat', None, False],
    #                  [pinterest, False, 'pinterest', None, False]]
    social_medias = [[myspace, False, 'myspace', None, False]]
    ops = Options()
    ops.headless = True
    for social_media in social_medias:
        threading.Thread(
            target=social_media[0], args=(ops, gmail, social_media), name=social_media[2], daemon=True).start()
    while len(social_medias) != 0:
        for social_media in social_medias:
            sm = social_media
            print(sm)
            if sm[4]:
                if social_media[1]:
                    print(Fore.LIGHTGREEN_EX+"[V] " +
                          social_media[2] + Fore.RESET)
                if social_media[3] != None:
                    social_media[3].quit()
                social_medias.remove(social_media)
        time.sleep(0.5)


def facebook(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.facebook.com/login")
        driver.find_element(
            By.XPATH, "//input[@id='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@id='loginbutton']").click()
        driver.find_element(By.XPATH, "//div[@id='loginform']/div[2]/div[2]")
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
        driver.get("https://www.instagram.com/")
        driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div/div/label/input').send_keys(gmail)
        driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("      ")
        driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        if "Rất tiếc, mật khẩu của bạn không đúng" in driver.find_element(
                By.XPATH, "//p[@id='slfErrorAlert']").text:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def tiktok(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.tiktok.com/login/email/forget-password")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@type='button']").click()
        try:
            driver.find_element(By.XPATH, "//form/div[3]/div[2]")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def twitter(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://twitter.com/i/flow/signup")
        driver.find_element(By.XPATH, "//div[5]").click()
        driver.find_element(By.XPATH, "//div[2]/div/div/div[2]/div[3]").click()
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//span[contains(text(),'Email này đã được sử dụng.')]")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def youtube(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://accounts.google.com/ServiceLogin")
        driver.find_element(
            By.XPATH, "//input[@id='identifierId']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@id='identifierNext']").click()
        try:
            driver.find_element(
                By.XPATH, "//section/div/div/div[1]/div/div[2]/div/div")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def hahalolo(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://accounts.hahalolo.com/forgot-password/")
        driver.find_element(
            By.XPATH, "//input[@name='phoneOrEmail']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-fullWidth']").click()
        driver.find_element(
            By.XPATH, "//span[normalize-space()='Xác minh tài khoản']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def biztime(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://biztime.com.vn/forgot-password")
        driver.find_element(
            By.XPATH, "//input[@name='recoveremail']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form[@id='forgot-form']//button[@type='submit'][contains(text(),'Khôi phục')]").click()
        driver.implicitly_wait(15)
        driver.find_element(
            By.XPATH, "//div[@class='valign tag_auth_animation']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def flickr(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://identity.flickr.com/forgot-password")
        driver.find_element(
            By.XPATH, "//input[@id='forgot-password-email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//form/div[2]/p']")
        except:
            social_media[1] = True
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        social_media[4] = True


def tumblr(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(120)
        driver.get("https://www.tumblr.com/register")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@name='password']").send_keys("         ")
        driver.find_element(
            By.XPATH, "//form//button").click()
        Select(driver.find_element(
            By.XPATH, "//select[@name='month']")).select_by_value("2")
        Select(driver.find_element(
            By.XPATH, "//select[@name='day']")).select_by_value("18")
        Select(driver.find_element(
            By.XPATH, "//select[@name='year']")).select_by_value("2001")
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.find_element(
            By.XPATH, "//input[@id='onboardingBlogname']").send_keys(gmail.split('@')[0])
        driver.find_element(
            By.XPATH, "//section//button").click()
        try:
            driver.find_element(
                By.XPATH, "//div[@class='oFCPF']")
        except:
            social_media[1] = True
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        social_media[4] = True


def snapchat(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.linkedin.com/login")
        driver.find_element(
            By.XPATH, "//input[@id='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@id='password']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "(//form)[2]//button").click()
        driver.implicitly_wait(15)
        driver.find_element(
            By.XPATH, "//div[@id='organic-otp-link-in-error-message']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def pinterest(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.pinterest.com/login/")
        driver.find_element(
            By.XPATH, "//input[@id='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.implicitly_wait(15)
        driver.find_element(
            By.XPATH, "//span[@id='password-error']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

# not


def reddit(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.pinterest.com/login/")
        driver.find_element(
            By.XPATH, "//input[@id='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.implicitly_wait(15)
        driver.find_element(
            By.XPATH, "//span[@id='password-error']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True
# not


def myspace(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://myspace.com/signin")
        driver.find_element(
            By.XPATH, "//input[@id='login.email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@id='login.password']").send_keys(" ")
        driver.find_element(
            By.XPATH, "//button[normalize-space()='Sign In']").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//div[contains(text(),'Invalid email and/or password. Please try again.')]")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

# not


def linkedin(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://www.linkedin.com/login")
        driver.find_element(
            By.XPATH, "//input[@id='login.email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@id='login.password']").send_keys(" ")
        old_id = driver.find_element_by_tag_name('html').id
        driver.find_element(
            By.XPATH, "//button[normalize-space()='Sign In']").click()
        while driver.find_element_by_tag_name('html').id == old_id:
            continue
        if "That's not the right password" in driver.find_element(By.XPATH, "//div[@id='error-for-password']").text:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True
# not


def desentric(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://desentric.com//guest?auth=forgot_pass")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(By.XPATH, "//form/div/div[2]/div")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

# not


def zoimas(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://zoimas.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//p[normalize-space()='We couldn't find the username.']")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True
# not


def befilo(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://befilo.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//p[normalize-space()='We couldn't find the username.']")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

# not


def opportunity(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://befilo.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.implicitly_wait(15)
        if driver.find_element(
                By.XPATH, "//div[@id='account_help']/div/h2").text == "Success":
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True
# not


def flipboard(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://befilo.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//p[normalize-space()='We couldn't find the username.']")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

# not


def xing(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox()
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(120)
        driver.get("https://login.xing.com/recovery")
        driver.find_element(
            By.XPATH, "//input[@id='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()
        driver.implicitly_wait(15)
        try:
            driver.find_element(
                By.XPATH, "//form/div[2]/div/div/div/p")
        except:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


search_social_media_from_gmail("pk4824829@gmail.com")
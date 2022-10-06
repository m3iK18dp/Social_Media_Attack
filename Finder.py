#!/usr/bin/python
# -*- coding: utf-8 -*-
# ============Author: m3iK18dp=============
# ===============2022/10===================
import threading
from optparse import *
import time
import io
import os
try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip install colorama")


def search_social_media_by_gmail(gmail):
    # [[function, result, social_media_name, webdriver, status]]
    social_medias = [[facebook, False, 'Facebook', None, False],
                     [instagram, False, 'Instagram', None, False],
                     [tiktok, False, 'Tiktok', None, False],
                     [twitter, False, 'Twitter', None, False],
                     [youtube, False, 'Youtube', None, False],
                     [hahalolo, False, 'Hahalolo', None, False],
                     [biztime, False, 'Biztime', None, False],
                     [flickr, False, 'Flickr', None, False],
                     [tumblr, False, 'Tumblr', None, False],
                     [pinterest, False, 'Pinterest', None, False],
                     [zoimas, False, 'Zoimas', None, False],
                     [befilo, False, 'Befilo', None, False],
                     [opportunity, False, 'Opportunity', None, False],
                     [flipboard, False, 'Flipboard', None, False],
                     [xing, False, 'Xing', None, False],
                     [linkedin, False, 'Linkedin', None, False],
                     [desentric, False, 'Desentric', None, False],
                     [quora, False, 'Quora', None, False]]
    ops = Options()
    ops.headless = True
    for social_media in social_medias:
        threading.Thread(
            target=social_media[0], args=(ops, gmail, social_media), name=social_media[2], daemon=True).start()
    threading.Thread(target=check_and_kill, args=(gmail, social_medias,),
                     name="check_and_kill", daemon=True).start()
    while input(Fore.LIGHTMAGENTA_EX +
                "[!] If you want to stop using Finder, press enter..."+Fore.RESET+'\n') != "" and len(social_medias) != 0:
        continue
    for social_media in social_medias:
        if social_media[3] != None:
            social_media[3].quit()


def check_and_kill(gmail, social_medias):
    str = gmail
    while len(social_medias) != 0:
        for social_media in social_medias:
            sm = social_media
            if sm[4]:
                if social_media[1]:
                    str += "-"+(social_media[2].lower())
                    print(Fore.LIGHTGREEN_EX+"[V] " +
                          social_media[2] + Fore.RESET)
                if social_media[3] != None:
                    social_media[3].quit()
                social_medias.remove(social_media)
    io.open("Finder_result.txt", "a").write(str+"\n")
    print(Fore.LIGHTMAGENTA_EX +
          "[!] Success Finder, press enter to exit..."+Fore.RESET)


def facebook(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
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
        driver.set_page_load_timeout(60)
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
        driver.set_page_load_timeout(60)
        driver.get("https://www.tiktok.com/login/email/forget-password")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@type='button']").click()
        try:
            driver.find_element(By.XPATH, "//form/div[3]/div[2]")
        except selenium.common.exceptions.NoSuchElementException:
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
        driver.set_page_load_timeout(60)
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
    time.sleep(5)
    social_media[1] = True
    social_media[4] = True


def hahalolo(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://accounts.hahalolo.com/sign-up/")
        driver.find_element(
            By.XPATH, "//input[@name='firstName']").send_keys('a')
        driver.find_element(
            By.XPATH, "//input[@name='lastName']").send_keys('a')
        driver.find_element(
            By.XPATH, "//input[@name='phoneOrEmail']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@id='password']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@name='confirmPassword']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "(//button)[1]").click()
        driver.find_element(By.XPATH, "(//span)[56]")
        social_media[1] = True
    except selenium.common.exceptions.NoSuchElementException:
        print
    finally:
        driver.quit()
        social_media[4] = True


def biztime(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://biztime.com.vn/forgot-password")
        driver.find_element(
            By.XPATH, "//input[@name='recoveremail']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form[@id='forgot-form']//button[@type='submit'][contains(text(),'Khôi phục')]").click()
        driver.find_element(
            By.XPATH, "//div[@class='valign tag_auth_animation']")
        social_media[1] = True
    except selenium.common.exceptions.NoSuchElementException:
        print
    finally:
        driver.quit()
        social_media[4] = True


def flickr(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://identity.flickr.com/forgot-password")
        driver.find_element(
            By.XPATH, "//input[@id='forgot-password-email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        try:
            driver.find_element(
                By.XPATH, "//form/div[2]/p']")
        except selenium.common.exceptions.NoSuchElementException:
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
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
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
            By.XPATH, "(//button)[6]").click()
        try:
            driver.find_element(
                By.XPATH, "//div[@class='oFCPF']")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        social_media[4] = True


def pinterest(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://www.pinterest.com/login/")
        driver.find_element(
            By.XPATH, "//input[@id='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        driver.find_element(
            By.XPATH, "//span[@id='password-error']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def linkedin(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get(
            "https://www.linkedin.com/checkpoint/rp/request-password-reset")
        driver.find_element(
            By.XPATH, "//input[@id='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//button[@id='reset-password-submit-button']").click()
        try:
            driver.find_element(
                By.XPATH, "//h1[normalize-space()='We sent a code to your email']")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def desentric(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(2)
        driver.set_page_load_timeout(60)
        driver.get("https://desentric.com//guest?auth=forgot_pass")
        try:
            driver.find_element(By.XPATH, "(//button)[2]").click()
        except:
            print
        time.sleep(2)
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        try:
            driver.find_element(By.XPATH, "//form/div/div[2]/div")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def zoimas(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://zoimas.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.find_element(
            By.XPATH, "//input[@name='n']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def befilo(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://befilo.com//recover")
        driver.find_element(
            By.XPATH, "//input[@name='username']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//input[@value='Recover']").click()
        driver.find_element(
            By.XPATH, "//input[@name='n']")
        social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def opportunity(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://myopportunity.com/signin/forgot")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//button").click()
        try:
            driver.find_element(
                By.XPATH, "//label[normalize-space()='Email is not valid.']")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def flipboard(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://accounts.flipboard.com/accounts/forgotPassword")
        driver.find_element(
            By.XPATH, "//input[@name='email']").send_keys(gmail)
        driver.find_element(
            By.XPATH, "//form//input[3]").click()
        if driver.find_element(By.XPATH, "//h2").text == "Success!":
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def xing(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(60)
        driver.get("https://login.xing.com/recovery")
        driver.find_element(
            By.XPATH, "//input[@id='username']").send_keys(gmail)
        try:
            driver.find_element(
                By.XPATH, "//button[@id='consent-accept-button']").click()
        except:
            print
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(
                By.XPATH, "//form/div[2]/div/div/div/p")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True


def quora(ops, gmail, social_media):
    try:
        driver = webdriver.Firefox(options=ops)
        social_media[3] = driver
        driver.implicitly_wait(2)
        driver.set_page_load_timeout(60)
        driver.get("https://www.quora.com/")
        driver.find_element(
            By.XPATH, "//input[@id='email']").send_keys(gmail)
        try:
            driver.find_element(
                By.XPATH, "//input[@id='email']/../../div[3]")
        except selenium.common.exceptions.NoSuchElementException:
            social_media[1] = True
    except:
        print
    finally:
        driver.quit()
        social_media[4] = True

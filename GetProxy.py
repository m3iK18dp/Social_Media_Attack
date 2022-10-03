#!/usr/bin/python
# -*- coding: utf-8 -*-
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
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
try:
    import requests
except:
    os.system("pip install requests")
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
url_list = ['https://www.facebook.com/login', 'https://www.youtube.com/',
            'https://www.instagram.com', 'https://www.tiktok.com/login/phone-or-email/email', 'https://twitter.com/i/flow/login', 'https://www.gapo.vn/', 'https://biztime.com.vn/', 'https://accounts.hahalolo.com/sign-in/']
social_name = ['facebook', 'youtube', 'instagram',
               'tiktok', 'twitter', 'gapo', 'biztime', 'hahalolo']
# ===============================Get Proxy List============================


def getProxies(getProxies, type):
    if type != None:
        types = str(type).split("|")
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
    func_load = [getProxies_switcher,
                 getProxies_spys_1, getProxies_spys_2, getProxies_spys_3, getProxies_free_proxy_list, getProxies_cybersyndrome_1, getProxies_cybersyndrome_2, getProxies_cybersyndrome_3, getProxies_foxtools, getProxies_premproxy_1, getProxies_premproxy_2, getProxies_premproxy_3, getProxies_premproxy_4]
    threads_get = []
    threads_webdriver = []
    for index_func in range(0, len(func_load)):
        if index_func == 0:
            threads_get.append(threading.Thread(
                target=func_load[index_func], args=(index_type, getProxies,), name="Thread_"+str(index_func), daemon=True))
        else:
            threads_webdriver.append(None)
            threads_get.append(threading.Thread(
                target=func_load[index_func], args=(ops, capabilities, index_type, threads_webdriver, index_func-1, getProxies,), name="Thread_"+str(index_func), daemon=True))
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


def getProxies_switcher(index_type, getProxies):
    try:
        io.open("proxy_list_switcher.txt", "a+")
        get_str = io.open("proxy_list_switcher.txt", "r").readlines()
        for i in range(1, len(get_str)):
            check_proxy(get_str[i].split(",")[0], index_type, getProxies)
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from switcher"+Fore.RESET)


def getProxies_spys_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
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
                check_proxy(proxy, index_type, getProxies)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX+"[!] Error get proxy from "+url+Fore.RESET)
        driver.quit()


def getProxies_spys_txt(ops, capabilities, index_type, url, threads_webdriver, index_in_threads_webdriver, getProxies):
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
                check_proxy(check_1[i].split(" ")[0], index_type, getProxies)
            first_get = False
    except:
        driver.quit()
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from "+url+Fore.RESET)


def getProxies_spys_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_spys_txt(ops, capabilities, index_type,
                        "https://spys.me/proxy.txt", threads_webdriver, index_in_threads_webdriver, getProxies)


def getProxies_spys_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_spys_txt(ops, capabilities, index_type,
                        "https://spys.me/socks.txt", threads_webdriver, index_in_threads_webdriver, getProxies)


def getProxies_free_proxy_list(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
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
                check_proxy(proxy, index_type, getProxies)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from "+url+Fore.RESET)
        driver.quit()


def getProxies_cybersyndrome(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, index_url, getProxies):
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
                check_proxy(proxy, index_type, getProxies)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!"+index_url+"] Error get proxy from http://www.cybersyndrome.net"+Fore.RESET)
        driver.quit()


def getProxies_cybersyndrome_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_cybersyndrome(ops, capabilities, index_type,
                             threads_webdriver, index_in_threads_webdriver, 0, getProxies)


def getProxies_cybersyndrome_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_cybersyndrome(ops, capabilities, index_type,
                             threads_webdriver, index_in_threads_webdriver, 1, getProxies)


def getProxies_cybersyndrome_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_cybersyndrome(ops, capabilities, index_type,
                             threads_webdriver, index_in_threads_webdriver, 2, getProxies)


def getProxies_foxtools(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
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
                check_proxy(proxy, index_type, getProxies)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!] Error get proxy from http://foxtools.ru/Proxy"+Fore.RESET)
        driver.quit()


def getProxies_premproxy(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, a, b, getProxies):
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
                for row in range(1, 100):
                    try:
                        td_text = driver.find_element(
                            By.XPATH, "//table[@id='proxylistt']/tbody/tr["+str(row)+"]/td[1]").text
                        if td_text == "Select All Proxies":
                            continue
                        proxies.append(td_text)
                    except:
                        break
            driver.quit()
            for proxy in proxies:
                check_proxy(proxy, index_type, getProxies)
            first_get = False
    except:
        print(Fore.LIGHTMAGENTA_EX +
              "[!"+str(index_in_threads_webdriver)+"] Error get proxy from https://premproxy.com/list" + Fore.RESET)
        driver.quit()


def getProxies_premproxy_1(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_premproxy(ops, capabilities, index_type,
                         threads_webdriver, index_in_threads_webdriver, 1, 3, getProxies)


def getProxies_premproxy_2(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_premproxy(ops, capabilities, index_type,
                         threads_webdriver, index_in_threads_webdriver, 4, 7, getProxies)


def getProxies_premproxy_3(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_premproxy(ops, capabilities, index_type,
                         threads_webdriver, index_in_threads_webdriver, 8, 11, getProxies)


def getProxies_premproxy_4(ops, capabilities, index_type, threads_webdriver, index_in_threads_webdriver, getProxies):
    getProxies_premproxy(ops, capabilities, index_type,
                         threads_webdriver, index_in_threads_webdriver, 12, 15, getProxies)
# ================================CHECK AND Export PROXY=============================


def check_proxy(myproxy, index_type, getProxies):
    for s in index_type:
        try:
            io.open(getProxies, "a+")
            list_in_file = io.open(getProxies, "r").readlines()
            get_str = "" if len(list_in_file) == 0 else list_in_file.pop()
            if not social_name[s]+"-"+myproxy in get_str:
                requests.get(url_list[s],
                             proxies={'https': myproxy, 'http': myproxy}, timeout=1)
                io.open(getProxies, "w").write(
                    social_name[s]+"-"+myproxy+","+get_str)
                print(Fore.LIGHTGREEN_EX+"[V]"+social_name[s] +
                      "-"+myproxy+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"[X]"+social_name[s] +
                  "-"+myproxy+Fore.RESET)

# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# from ast import arg
# from re import T
# import smtplib
# import threading
# from optparse import *
# import time
# import os
# import sys
# import io
# from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import selenium.common.exceptions
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.select import Select
# import requests
# from colorama import Fore, Back, Style
# R = '\033[31m'  # red
# G = '\033[32m'  # green
# W = '\033[0m'  # white (normal)


# def getProxyList():
#     if options.type != None:
#         types = str(options.type).split("|")
#         index_type = []
#         for t in types:
#             index_type.append(social_name.index(t))
#     else:
#         index_type = [0, 1, 2, 3, 4, 5, 6, 7]
#     proxy = Proxy()
#     proxy.proxy_type = ProxyType.MANUAL
#     capabilities = webdriver.DesiredCapabilities.FIREFOX
#     proxy.http_proxy = ''
#     proxy.ssl_proxy = ''
#     proxy.add_to_capabilities(capabilities)
#     ops = Options()
#     ops.headless = True
#     t0 = threading.Thread(
#         target=getProxyList_switcher, args=(index_type,), name="getProxyList_switcher")
#     t1 = threading.Thread(
#         target=getProxyList_spys, args=(ops, capabilities, index_type,), name="getProxyList_spys")
#     t2 = threading.Thread(
#         target=getProxyList_freeproxylist, args=(ops, capabilities, index_type,), name="getProxyList_freeproxylist")
#     t3 = threading.Thread(
#         target=getProxyList_cybersyndrome, args=(ops, capabilities, index_type,), name="getProxyList_cybersyndrome")
#     t4 = threading.Thread(
#         target=getProxyList_foxtools, args=(ops, capabilities, index_type,), name="getProxyList_foxtools")
#     t5 = threading.Thread(
#         target=getProxyList_premproxy, args=(ops, capabilities, index_type,), name="getProxyList_premproxy")
#     # t0.start()
#     t1.start()
#     # t2.start()
#     # t3.start()
#     # t4.start()
#     # t5.start()


# def getProxyList_switcher(index_type):
#     try:
#         io.open("proxy_list_switcher.txt", "a+")
#         get_str = io.open("proxy_list_switcher.txt", "r").readlines()
#         for i in range(1, len(get_str)):
#             check_proxy(get_str[i].split(",")[0], index_type)
#     except:
#         print(Fore.LIGHTRED_EX+"[!] Error get proxy from switcher"+Fore.RESET)


# def getProxyList_spys(ops, capabilities, index_type):
#     try:
#         driver = webdriver.Firefox(
#             desired_capabilities=capabilities)
#         driver.implicitly_wait(5)
#         first_get = True
#         driver.get("https://spys.one/en/free-proxy-list/")
#         check_1 = driver.find_element(
#             By.XPATH, "//tbody/tr[3]/td[1]/font[1]").text
#         while True:
#             if not first_get:
#                 while True:
#                     try:
#                         driver.get("https://spys.one/en/free-proxy-list/")
#                         check_2 = driver.find_element(
#                             By.XPATH, "//tbody/tr[3]/td[1]/font[1]").text
#                         if check_1 != check_2:
#                             check_1 = check_2
#                             break
#                         time.sleep(120)
#                     except:
#                         continue
#             for row in range(3, 33):
#                 check_proxy(driver.find_element(
#                     By.XPATH, "//tbody/tr["+str(row)+"]/td[1]/font[1]").text, index_type)
#             first_get = False
#     except:
#         print(Fore.LIGHTRED_EX+"[!] Error get proxy from spys"+Fore.RESET)
#         driver.quit()


# def getProxyList_freeproxylist(ops, capabilities, index_type):
#     try:
#         driver = webdriver.Firefox(
#             options=ops, desired_capabilities=capabilities)
#         driver.implicitly_wait(5)
#         first_get = True
#         driver.get("https://free-proxy-list.net/")
#         check_1 = driver.find_element(
#             By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[1]").text+":"+driver.find_element(
#             By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[2]").text
#         while True:
#             if not first_get:
#                 while True:
#                     try:
#                         driver.get("https://free-proxy-list.net/")
#                         check_2 = driver.find_element(
#                             By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[1]").text+":"+driver.find_element(
#                             By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr[1]/td[2]").text
#                         if check_1 != check_2:
#                             check_1 = check_2
#                             break
#                         time.sleep(300)
#                     except:
#                         continue
#             for row in range(1, 70):
#                 check_proxy(driver.find_element(
#                     By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr["+str(row)+"]/td[1]").text+":"+driver.find_element(
#                     By.XPATH, "//table[@class='table table-striped table-bordered']/tbody/tr["+str(row)+"]/td[2]").text, index_type)
#             first_get = False
#     except:
#         print(Fore.LIGHTRED_EX +
#               "[!] Error get proxy from free-proxy-list"+Fore.RESET)
#         driver.quit()


# def getProxyList_cybersyndrome(ops, capabilities, index_type):
#     try:
#         driver = webdriver.Firefox(
#             options=ops, desired_capabilities=capabilities)
#         driver.implicitly_wait(5)
#         first_get = True
#         cybersyndrome_url = ["http://www.cybersyndrome.net/plr6.html",
#                              "http://www.cybersyndrome.net/pla6.html", "http://www.cybersyndrome.net/pld6.html"]
#         path_update_time = "//div[@id='content']/div[2]/span"
#         time_update_time_1 = []
#         for url in cybersyndrome_url:
#             driver.get(url)
#             time_update_time_1.append(driver.find_element(
#                 By.XPATH, path_update_time).text)
#         while True:
#             check = [False, False, False]
#             if not first_get:
#                 while True:
#                     try:
#                         time_update_time_2 = []
#                         for url in cybersyndrome_url:
#                             driver.get(url)
#                             time_update_time_2.append(driver.find_element(
#                                 By.XPATH, path_update_time).text)
#                         for i in (0, 3):
#                             if time_update_time_1[i] != time_update_time_2[i]:
#                                 time_update_time_1[i] = time_update_time_2[i]
#                                 check[i] = True
#                         if check[0] == True or check[1] == True or check[2] == True:
#                             break
#                         time.sleep(300)
#                     except:
#                         continue
#             if check[0] or first_get:
#                 driver.get(cybersyndrome_url[0])
#                 for row in range(1, 31):
#                     check_proxy(driver.find_element(
#                         By.XPATH, "//td[@id='n"+str(row)+"']").text, index_type)
#             if check[1] or first_get:
#                 driver.get(cybersyndrome_url[1])
#                 for row in range(1, int(driver.find_element(By.XPATH, "//div[@id='content']/div[2]/span[2]").text)+1):
#                     check_proxy(driver.find_element(
#                         By.XPATH, "//a[@id='n"+str(row)+"']").text, index_type)
#             if check[2] or first_get:
#                 driver.get(cybersyndrome_url[2])
#                 for row in range(1, int(driver.find_element(By.XPATH, "//div[@id='content']/div[2]/span[2]").text)+1):
#                     check_proxy(driver.find_element(
#                         By.XPATH, "//a[@id='n"+str(row)+"']").text, index_type)
#             first_get = False
#     except:
#         print(Fore.LIGHTRED_EX +
#               "[!] Error get proxy from cybersyndrome"+Fore.RESET)
#         driver.quit()


# def getProxyList_foxtools(ops, capabilities, index_type):
#     try:
#         driver = webdriver.Firefox(
#             options=ops, desired_capabilities=capabilities)
#         driver.implicitly_wait(5)
#         first_get = True
#         driver.get("http://foxtools.ru/Proxy?page=1")
#         check_1 = driver.find_element(
#             By.XPATH, "//table[@id='theProxyList']/tbody/tr[1]/td[2]").text
#         while True:
#             if not first_get:
#                 while True:
#                     try:
#                         driver.get("http://foxtools.ru/Proxy?page=1")
#                         check_2 = driver.find_element(
#                             By.XPATH, "//table[@id='theProxyList']/tbody/tr[1]/td[2]").text
#                         if check_1 != check_2:
#                             check_1 = check_2
#                             break
#                         time.sleep(300)
#                     except:
#                         continue
#             for i in range(1, 3):
#                 driver.get("http://foxtools.ru/Proxy?page="+str(i))
#                 driver.implicitly_wait(5)
#                 for row in range(1, 31):
#                     check_proxy(driver.find_element(
#                         By.XPATH, "//table[@id='theProxyList']/tbody/tr["+str(row)+"]/td[2]").text, index_type)
#             first_get = False
#     except:
#         print(Fore.LIGHTRED_EX +
#               "[!] Error get proxy from foxtools"+Fore.RESET)
#         driver.quit()


# def getProxyList_premproxy(ops, capabilities, index_type):
#     try:
#         driver = webdriver.Firefox(
#             options=ops, executable_path=r"geckodriver.exe", desired_capabilities=capabilities)
#         driver.implicitly_wait(5)
#         first_get = True
#         driver.get("https://premproxy.com/list/ip-port/time-1.htm")
#         check_1 = driver.find_element(
#             By.XPATH, "//ul[@id='ipportlist']/li[1]").text
#         while True:
#             if not first_get:
#                 while True:
#                     try:
#                         driver.get(
#                             "https://premproxy.com/list/ip-port/time-1.htm")
#                         check_2 = driver.find_element(
#                             By.XPATH, "//ul[@id='ipportlist']/li[1]").text
#                         if check_1 != check_2:
#                             check_1 = check_2
#                             break
#                         time.sleep(300)
#                     except:
#                         continue
#             for i in range(1, 6):
#                 driver.get(
#                     "https://premproxy.com/list/ip-port/time-"+str(i)+".htm")
#                 for row in range(1, 31 if i == 5 else 53):
#                     check_proxy(driver.find_element(
#                         By.XPATH, "//ul[@id='ipportlist']/li["+str(row)+"]").text, index_type)
#             first_get = False
#     except:
#         print(Fore.LIGHTRED_EX +
#               "[!] Error get proxy from premproxy"+Fore.RESET)
#         driver.quit()


# # ================================CHECK AND Export PROXY=============================
# url_list = ['https://www.facebook.com/login', 'https://www.youtube.com/',
#             'https://www.instagram.com', 'https://www.tiktok.com/login/phone-or-email/email', 'https://twitter.com/i/flow/login', 'https://www.gapo.vn/', 'https://biztime.com.vn/', 'https://accounts.hahalolo.com/sign-in/']
# social_name = ['facebook', 'youtube', 'instagram',
#                'tiktok', 'twitter', 'gapo', 'biztime', 'hahalolo']


# def check_proxy(myproxy, index_type):
#     for s in index_type:
#         try:
#             io.open(options.getproxylist, "a+")
#             list_in_file = io.open(options.getproxylist, "r").readlines()
#             get_str = "" if len(list_in_file) == 0 else list_in_file.pop()
#             if not social_name[s]+"-"+myproxy in get_str:
#                 requests.get(url_list[s],
#                              proxies={'https': myproxy, 'http': myproxy}, timeout=2)
#                 io.open(options.getproxylist, "w").write(
#                     social_name[s]+"-"+myproxy+","+get_str)
#                 print(Fore.LIGHTGREEN_EX+"[V]"+social_name[s] +
#                       "-"+myproxy+Fore.RESET)
#         except KeyboardInterrupt:
#             raise KeyboardInterrupt
#         except:
#             print(Fore.LIGHTRED_EX+"[X]"+social_name[s] +
#                   "-"+myproxy+Fore.RESET)

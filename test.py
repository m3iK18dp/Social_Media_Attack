
import io
from operator import le
import selectors
import threading
import time

# t = time.time()


# def loopp(h):
#     for i in range(100):
#         print(i)
#         time.sleep(1)


# def looppp():
#     for i in range(100, 200):
#         print(i)
#         time.sleep(5)


# t1 = threading.Thread(target=loopp, args=(10,))
# t2 = threading.Thread(target=looppp)
# t1.start()
# t2.start()

# print("time"+str(time.time() - t))
import requests
from async_timeout import timeout
from selenium.webdriver.common.proxy import Proxy, ProxyType
import smtplib
import threading
from optparse import *
import time
from os import *
import sys
import io
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import selenium.common.exceptions
import requests
from colorama import Fore, Back, Style
from selenium.webdriver.support.select import Select
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = '200.82.188.26:999'
# proxy.ssl_proxy = '200.82.188.26:999'
# capabilities = webdriver.DesiredCapabilities.FIREFOX
# proxy.add_to_capabilities(capabilities)
# brows = webdriver.Firefox()
# brows.get('https://biztime.com.vn/')
# path_update_time = "//div[@id='content']/div[2]/span"
# driver = webdriver.Firefox()
# driver.get("http://www.cybersyndrome.net/plr6.html")
# driver.find_element(By.XPATH,
#                     path_update_time).text
# 108.166.183.204:80
#!/usr/bin/env python3
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = "41.186.44.106:3128"
# proxy.ssl_proxy = "41.186.44.106:3128"
# capabilities = webdriver.DesiredCapabilities.FIREFOX
# proxy.add_to_capabilities(capabilities)
# driver = webdriver.Firefox()
# driver.get("https://api.ipify.org/")

# driver.get("https://api.ipify.org/")


driver = webdriver.Firefox()

driver.get("https://spys.me/socks.txt")

lit = driver.find_element(
    By.XPATH, "//body/pre").text.split("\n")
prx = []
for i in range(6, len(lit)-2):
    prx.append(lit[i].split(" ")[0])
print(prx)

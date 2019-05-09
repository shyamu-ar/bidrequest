from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
#
# # PROXY = "173.214.169.77:3128"
# #
# # webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
# #     "httpProxy":PROXY,
# #     "ftpProxy":PROXY,
# #     "sslProxy":PROXY,
# #     # "noProxy":None,  # Not avaliable also ok
# #     "proxyType":"MANUAL", # not avaliable also ok
# #     # "class":"org.openqa.selenium.Proxy",
# #     # "autodetect":False # not avaliable also ok
# # }
# #
# # # you have to use remote, otherwise you'll have to code it yourself in python to
# # # driver = webdriver.Remote("https://www.google.co.in", webdriver.DesiredCapabilities.FIREFOX)
# # driver = webdriver.Firefox()
# # wait = driver.implicitly_wait(50)
# # driver.get("http://filmgrapevine.com/beta1.html")
#
# PROXY = "200.229.238.42:20183"
#
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     # "noProxy":None,  # Not avaliable also ok
#     "proxyType":"Manual", # not avaliable also ok
#     # "class":"org.openqa.selenium.Proxy",
#     # "autodetect":False # not avaliable also ok
# }

# you have to use remote, otherwise you'll have to code it yourself in python to
# driver = webdriver.Remote("https://www.google.co.in", webdriver.DesiredCapabilities.FIREFOX)
# driver = webdriver.Chrome()
# wait = driver.implicitly_wait(20)
# driver.get("http://filmgrapevine.com/beta1.html")
#
# import requests
# url = 'http://filmgrapevine.com/beta1.html'
# proxies1 = {
#     "http": 'http://91.187.113.205:53281'
# }
# proxy = 'http://91.187.113.205:53281'
# response = requests.get(url)
#
# print(response.json())

import selenium as se

options = se.webdriver.ChromeOptions()
options.add_argument('headless')

driver = se.webdriver.Chrome(chrome_options=options)

url = "http://filmgrapevine.com/beta1.html"
proxies = "46.219.80.142:50374"
# driver = webdriver.PhantomJS()
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy= proxies  #'220.248.229.45:3128'
#????????webdriver.DesiredCapabilities.PHANTOMJS?
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
driver.get(url)
html = driver.page_source
print(html)

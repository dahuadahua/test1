import re

# 八种定位方法：
# ID  # 此标签的id属性值
# NAME  # 此标签的name属性值
# CLASS_NAME  # 此标签的class属性值
# LINK_TEXT  # 适用于a标签（又称：超链接）
# PARTIAL_LINK_TEXT  # 适用于a标签（又称：超链接）
# TAG_NAME  # 直接使用标签名（准确度低）
# CSS_SELECTOR
# XPATH      万能
# sleep(3)
from selenium import webdriver   # 导入驱动
from selenium.webdriver.common.by import By     # 用于定位HTML标签
from time import sleep
chrome = webdriver.Chrome()     # 通过驱动打开浏览器
chrome.maximize_window()  # 最大化
chrome.implicitly_wait(30)  # 隐式等待30秒，意思就是最大等待的时间
chrome.get('http://172.31.22.189/#/login')    # 打开网页
chrome.find_element(by=By.ID, value='username').send_keys('admin')
chrome.find_element(by=By.ID, value='password').send_keys('dxcs12345')
chrome.find_element(by=By.TAG_NAME, value='button').click()
sleep(3)
chrome.find_element(by=By.LINK_TEXT, value='人 员 管 理').click()
sleep(3)
chrome.find_element(by=By.XPATH, value='//*[@class="ic-add"]').click() #添加
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('41272719941029613X')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-success"]').send_keys('喻华永')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('1-1-1-101')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="layui-layer-btn0"]').click() #确定
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="ic-add"]').click() #添加
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('1188')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-success"]').send_keys('卫小芳')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('1-1-1-101')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="layui-layer-btn0"]').click() #确定
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="ic-add"]').click() #添加
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('2233')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-success"]').send_keys('李鑫')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="text ng-pristine ng-valid we-verify-init-element we-verify-fail"]').send_keys('1-1-1-101')
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="layui-layer-btn0"]').click() #确定
sleep(1)
# chrome.find_element(by=By.XPATH, value='//*[@class="ng-pristine ng-valid"]').click()
sleep(1)
# chrome.find_element(by=By.XPATH, value='//*[@class="ic-empty"]').click()
sleep(1)
# chrome.find_element(by=By.XPATH, value='//*[@class="layui-layer-btn0"]').click() # 删除
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="exit"]').click()
sleep(1)
chrome.find_element(by=By.XPATH, value='//*[@class="layui-layer-btn0"]').click()
sleep(3)
chrome.find_element(by=By.ID, value='username').send_keys('admin')
sleep(1)
chrome.find_element(by=By.ID, value='password').send_keys('dxcs12345')
sleep(1)
chrome.find_element(by=By.TAG_NAME, value='button').click()
sleep(2)
chrome.find_element(by=By.ID, value='fold2').click()
sleep(3)
chrome.find_element(by=By.LINK_TEXT, value='事 件 查 询').click()

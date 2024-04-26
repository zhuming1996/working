from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(10)    
driver.maximize_window()
driver.find_element(By.ID, "kw").send_keys("哔哩哔哩")
time.sleep(3)
driver.find_element(By.ID,"su").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='content_left']/div[1]/div/h3/a[1]").click()
time.sleep(3)
# 获取当前的窗口句柄
current_handle = driver.current_window_handle
print("当前窗口句柄是：",current_handle, type(current_handle))
# 获取所有窗口句柄
handles = driver.window_handles
print("所有的窗口句柄是：",handles,type(handles))
driver.switch_to.window(handles[1])
el = driver.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[1]/li[2]/a/span').text
print(el)
# # 获取当前的窗口句柄
# current_handle = driver.current_window_handle
# print("当前窗口句柄是：",current_handle, type(current_handle))
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[1]/li[2]/a/span').click()
# # 获取所有窗口句柄
# handles = driver.window_handles
# print("所有的窗口句柄是：",handles,type(handles))
# driver.switch_to.window(handles[2])
# txt = driver.find_element(By.XPATH,'//*[@id="home_v3_mod_index"]/div/div[2]/a/span').text
# # scroll = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[1]/div/div/div[2])')
# # driver.execute_script("arguments[0].scrollIntoView();",scroll)
# time.sleep(3)
# print(txt)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.get('https://www.w3cschool.cn/tools/index?name=urlencode_decode')
sleep(3)    
driver.maximize_window()
#滚动页面到指定元素"URL在线编码转换工具"
# duizhao = driver.find_element(By.XPATH,'//*[@id="sortable_portlets"]/div[3]/div[2]/div/div/div[5]/a/div/div[2]')
# dz=driver.execute_script("arguments[0].scrollIntoView();",duizhao)
# sleep(5)
# 获取当前的窗口句柄
# current_handle = driver.current_window_handle
# print("当前窗口句柄是：",current_handle, type(current_handle))
# duizhao.click()
# 获取所有窗口句柄
# handles = driver.window_handles
# print("所有的窗口句柄是：",handles,type(handles))
# driver.switch_to.window(handles[1])


# 再次获取当前的窗口句柄,校验是否切换成功
# current_handle_new = driver.current_window_handle
# print("当前窗口句柄是：",current_handle_new, type(current_handle_new))
# driver.implicitly_wait(5)
#打印title
# url = driver.find_element(By.XPATH, '//h2[@align="center"]').text
# print(url)
# #滚动页面到指定元素"按钮"
# btn = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[2]/div/button')
# dz=driver.execute_script("arguments[0].scrollIntoView();",btn)
# driver.find_element(By.XPATH, '//*[@id="source"]').clear()
# driver.find_element(By.XPATH, '//*[@id="source"]').send_keys("https://fanyi.baidu.com/mtpe-individual/multimodal?ext_channel=Aldtype")
# driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div/label').click()
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[2]/div/button').click()
sleep(3)



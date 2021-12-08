
import time
from selenium.webdriver.common.by import By
def exec_search(driver,url,name,passwd,key):
    driver.get(url)
    driver.find_element(By.ID, 'username').send_keys(name)
    driver.find_element(By.ID, 'password').send_keys(passwd)
    driver.find_element(By.ID, 'btnSubmit').click()

    username = driver.find_element(By.XPATH,"//p").text  #找用户名 sunny
    driver.find_element(By.XPATH,'//span[text()="零售出库"]').click()
    id = driver.find_element(By.XPATH,'//div[text()="零售出库"]/..').get_attribute("id") # 取值零售出库上一级的id
    frame_id=id+"-frame"   # 得到iframe id
    driver.switch_to.frame(frame_id)  # 通过id进行 iframe的子页面进行切换
    driver.find_element(By.ID,'searchNumber').send_keys(key) # 对子界面的元素进行操作
    driver.find_element(By.ID,"searchBtn").click() # 判断 搜索 是否正确
    time.sleep(0.1) #不出来，加一个强制等待)
    text=driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text #获取文本
    return text

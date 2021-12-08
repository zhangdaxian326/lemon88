from selenium import webdriver
from common import method
from testdata import data

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url=data.testdata.get("url")
name=data.testdata.get("name")
passwd=data.testdata.get("passwd")
key=data.testdata.get("key")
result= method.exec_search(driver=driver,url=url,name=name,passwd=passwd,key=key)
print(result)
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\prave\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.milonic.com/login.php")
driver.find_element_by_name("email").send_keys("tejaswini536.t@gmail.com")
driver.find_element_by_name("password").send_keys("saivivek")
driver.find_element_by_xpath('//*[@id="f1"]/table/tbody/tr[5]/td/input[2]').click()
#write a python selenium script for auto login
#https://opensourse-demo.orangehrmlive.com/
driver.get("https://opensource-demo.orangehrmlive.com/")



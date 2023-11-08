from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Edge()
driver.get('https://www.instagram.com/')
time.sleep(5)

username= driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('coacervados77')

time.sleep(1)

senha= driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.send_keys('saviogatoboy22')

time.sleep(1)

entrar= driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]')
entrar.click()

time.sleep(10)

agrn= driver.find_element("xpath", '//*[@id="react-root"]/section/main/div/div/div/div/button')
agrn.click()

time.sleep(7)



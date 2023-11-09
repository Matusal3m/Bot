from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time 
options=Options()
options.add_argument("window-size=762,1000")
driver = webdriver.Edge(options=options)
action = ActionChains(driver)
driver.get('https://www.instagram.com/')
# driver.set_window_size(720, 1000)
time.sleep(5)

def clicar_elemento(metodo, elemento):
    variavel =  driver.find_element(metodo, elemento)
    variavel.click()

username = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('foguetesovietico')

time.sleep(1)

senha = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.send_keys('saviogatoboy22')

time.sleep(1)

clicar_elemento('xpath', '//*[@id="loginForm"]/div/div[3]')

time.sleep(10)

clicar_elemento('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')

time.sleep(5)

pesquisar = driver.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
pesquisar.send_keys('kll7')

time.sleep(3)

clicar_elemento('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')

time.sleep(6)

clicar_elemento('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button')

time.sleep(2)

try:
    clicar_elemento('xpath', '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]')
except:
    clicar_elemento('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div/div/div/div[1]/a')

time.sleep(10)

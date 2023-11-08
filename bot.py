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
driver.set_window_size(720, 1000)
time.sleep(5)

def clicar_elemento(metodo, elemento):

time.sleep(1)

senha = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
senha.send_keys('saviogatoboy22')

time.sleep(1)

clicar_elemento('xpath', '//*[@id="loginForm"]/div/div[3]')

time.sleep(15)

clicar_elemento('class name', '_ac8f')

time.sleep(10)

clicar_elemento('css selector', 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1')

time.sleep(5)

clicar_elemento('class name','xq8finb')

time.sleep(5)

clicar_elemento('xpath','//*[@id="mount_0_0_+k"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button')

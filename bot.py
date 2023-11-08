from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
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

time.sleep(15)

agrn= driver.find_element('class name', '_ac8f')
agrn.click()
time.sleep(10)

agrn2= driver.find_element('css selector','body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1')

agrn2.click()

time.sleep(10)

pesquisa = driver.find_element('class name', 'x1n2onr6')

pesquisa.click()
time.sleep(10)

#//*[@id="mount_0_0_Nv"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div


#mount_0_0_Nv > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1dr59a3.xixxii4.x13vifvy.xeq5yr9.x1n327nk > div > div > div > div > div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a
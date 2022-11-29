from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(executable_path='/Users/rafaellaramartins/Desktop/99freelas/blaze/chromedriver')


driver.get('https://blaze.com/en')

def login():
    
    click_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]')
    click_login.click()
    
    sleep(3)
    
    input_email = driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[1]/div')
    input_email.click()
    input_email.send_keys('rafaellara1405@gmail.com')
    
    input_pass = driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]')
    input_email.click()
    input_pass.send_keys('Coxinha123*')
    
    sleep(1)
    
    btn_entrar = driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]')
    btn_entrar.click()
    
    sleep(5)
    
    driver.close()

    #driver.get()

login()
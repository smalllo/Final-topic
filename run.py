from selenium import webdriver
import tkinter as tk
import time
#用selenium控制,driver只能跑chrome


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
#隱藏被控制


driver.get("https://pacific.asia.edu.tw/HealthDeclaration#/Login")
#憑證網頁
element = driver.find_element_by_class_name("form-control")
element.send_keys("109021049")
time.sleep(1)
element = driver.find_element_by_name("password")
element.send_keys("Aa900748")
time.sleep(1)
button = driver.find_element_by_xpath("/html/body/div/main/div/div[2]/div[1]/form/button")
button.click()
time.sleep(1)
button = driver.find_element_by_xpath("/html/body/div/main/div/div[3]/button")
button.click()
time.sleep(1)
element = driver.find_element_by_name("cell")
element.send_keys("0902181773")
button = driver.find_element_by_xpath("/html/body/div/main/form/div[4]/div[4]/div/div/div/div[8]/input")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[4]/div[5]/div/div/div[6]/input")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[4]/div[7]/div/div/div[1]/input")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[4]/div[12]/input")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[5]/button")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[6]/div[2]/div[2]/button[1]")
button.click()
button = driver.find_element_by_xpath("/html/body/div/main/form/div[7]/div[2]/div[2]/button")
button.click()
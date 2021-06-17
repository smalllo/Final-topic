from selenium import webdriver
import tkinter as tk
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
#隱藏被控制

driver.get("https://pacific.asia.edu.tw/HealthDeclaration#/Login")
#憑證網頁

def start():   
    account = str(ac_variable.get())
    password = str(pw_variable.get())
    telephone = str(tg_variable.get())
    try:
        account_input = driver.find_element_by_class_name("form-control")
        account_input.send_keys(account)
        password_input = driver.find_element_by_name("password")
        password_input.send_keys(password)
        button = driver.find_element_by_xpath("/html/body/div/main/div/div[2]/div[1]/form/button")
        button.click()
        time.sleep(1)
        button = driver.find_element_by_xpath("/html/body/div/main/div/div[3]/button")
        button.click()
        time.sleep(1)
        telephone_input = driver.find_element_by_name("cell")
        telephone_input.send_keys(telephone)
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
    except:
        pass
window = tk.Tk()
window.title("健康憑證填寫系統")
window.geometry("400x450")
window.resizable(0,0)

name = tk.Label(window, text="健康聲明自動表單")
name.pack(pady=10, side="top", fill="x")
name = tk.Label(window, text="警告:預設皆為無異狀,若有不符請勿使用",fg="Red")
name.pack(pady=10, side="top", fill="x")

tk.Label(window, text="帳號:",font=('Arial',15)).place(x=60,y=70)
ac_variable = tk.StringVar()
ac = tk.Entry(window,textvariable = ac_variable)
ac.place(x=120,y=75)

tk.Label(window, text="密碼:",font=('Arial',15)).place(x=60,y=110)
pw_variable = tk.StringVar()
pw_variable.set("")
pw = tk.Entry(window,show = '*',textvariable = pw_variable)
pw.place(x=120,y=115)


tk.Label(window, text="電話:",font=('Arial',15)).place(x=60,y=160)
tg_variable = tk.StringVar()
tg = tk.Entry(window,textvariable = tg_variable)
tg.place(x=120,y=160)

start = tk.Button(window,text = "Login",command = start)
start.place(x=280,y=70)

window.mainloop()



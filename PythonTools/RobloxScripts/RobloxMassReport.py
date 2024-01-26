import secrets
import string
import time
import os
import sys
import random
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import threading

def status(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;34m" + text + "\033[0m")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def report():
    driver.get(reporturl + str(useridtoreport))
    #finding elements
    try:
        reportdropdown = driver.find_element("id", "ReportCategory")
        reporttext =  driver.find_element("id", "Comment")
        reportbutton = driver.find_element("id", "report-abuse")
    except:
        status("Unfortunately, you've reached the maximum amount of reports. This may reset at midnight (GMT). Please try again later.")
        exit()

    selection = Select(reportdropdown)
    selection.select_by_value("3")

    reporttext.send_keys("they were really mean to me")
    time.sleep(1)

    reportbutton.click()
    time.sleep(2)

cookie_found = False
url = "https://www.roblox.com/login"
reporturl = "https://www.roblox.com/abusereport/userprofile?id="
clear()
useridtoreport = input("Please enter the victim's user id: ")
reportamount = input("Please enter the amount of reports to report the victim with: ")
x = input("Please hit enter to initialize the report bot (you may need to complete Roblox's human verification). ")
status("In order to report, you'll need to make a dummy bot account (CANT HAVE 2 STEP VERIFICATION) that you're ok with getting banned. Then you can continue below.")
username = input("Please enter the username of the bot account: ")
password = input("Please enter the password of the bot account:")

chrome_options = webdriver.EdgeOptions()
chrome_options.add_argument("--log-level=3")
driver = webdriver.Edge(options=chrome_options)
driver.set_window_size(1200, 800)
driver.set_window_position(0, 0)
driver.minimize_window()
driver.get(url)

time.sleep(2)

#finding elements
usernametext = driver.find_element("id", "login-username")
passwordtext = driver.find_element("id", "login-password")
submitbutton = driver.find_element("id", "login-button")

#logging in
usernametext.send_keys(username)
passwordtext.send_keys(password)
time.sleep(2)
submitbutton.click()
status("Please check the browser window to do the verification if you have to. If there isn't any verification and it's logged in, DONT CLOSE THE WINDOW.")
while not cookie_found:
            status("Waiting for the cookie...")
            time.sleep(3)
            for cookie in driver.get_cookies():
                if cookie.get('name') == '.ROBLOSECURITY':
                    cookie_found = True
                    break
clear()
print("Logged in successfully!")
print("To make all " + str(reportamount) + " reports, it will take about " + str(int(reportamount) * 3) + " seconds.")
x = input("Press enter to confirm that you want to mass report and potentially BAN the victim you selected. ")
driver.maximize_window()
for i in range(int(reportamount)):
     status("Made reports " + str(i) + "/" + str(reportamount))
     report()
status("Finished! Goodbye.")
driver.minimize_window()


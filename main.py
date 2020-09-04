import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login import login
from to_task import go_to_task
from vocab_learn import do_vocab_learn
from vocab_test import do_vocab_test

options = Options()
options.add_argument('--no-sandbox')  # Bypass OS security model
browser = webdriver.Chrome(options=options,
                           executable_path=f"{os.getcwd()}\\chromedriver_win32\\chromedriver.exe")  # Gets the web driver
browser.get("https://www.pearsonactivelearn.com/app/login")  # Goes to Active Learn website
browser.maximize_window()

task = "LINK TO TASK LIST HERE"

username = "USERNAME HERE"
password = "PASSWORD HERE"
login(browser, username, password)
go_to_task(browser, task)
while True:
    do_vocab_learn(browser)
    do_vocab_test(browser)

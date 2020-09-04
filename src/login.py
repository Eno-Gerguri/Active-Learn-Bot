from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def login(browser: webdriver.chrome, username: str, password: str):
    username_input_field = WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.ID, "username")))
    username_input_field.send_keys(username)

    password_input_field = WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.ID, "password")))
    password_input_field.send_keys(password)

    sign_in_button = WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.ID, "mainButton")))
    sign_in_button.click()

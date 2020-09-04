from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

def go_to_task(browser: webdriver.chrome, task: str):
    sleep(2)
    browser.get(task)

    try:
        exercises_tab = WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div/div[2]/div[1]/ul/li[2]/a')))
        exercises_tab.click()

        higher_tab = WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="li_225545"]/a')))
        higher_tab.click()

    except:
        return

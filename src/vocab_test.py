from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import json


def do_vocab_test(browser: webdriver.chrome):
    with open("english_to_french_translations.json", 'r') as f:
        english_to_french = json.load(f)

    frame = WebDriverWait(browser, 600).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="playerFrame"]')))
    browser.switch_to.frame(frame)
    is_first_iteration = True

    while True:
        try:
            if is_first_iteration:
                english_text = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="mCSB_7_container"]/div[3]/div[3]/div[1]')))

                french_input_field = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="userInputText"]')))

                french_to_type = english_to_french[english_text.text]

                ActionChains(browser).send_keys_to_element(french_input_field, french_to_type).perform()

                is_first_iteration = False

            else:
                english_text = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="mCSB_7_container"]/div[3]/div[3]/div[1]')))

                french_input_field = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="userInputText"]')))

                french_to_type = english_to_french[english_text.text]

                ActionChains(browser).send_keys_to_element(french_input_field, french_to_type).perform()

                submit_button = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="vocalb_check"]')))
                submit_button.click()

                next_button = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="vocalb_next"]')))
                next_button.click()

        except (StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException,
                ElementClickInterceptedException, NoSuchWindowException, KeyError):
            break

    browser.switch_to.default_content()


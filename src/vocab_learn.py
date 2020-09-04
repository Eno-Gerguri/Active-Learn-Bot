from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import json


def do_vocab_learn(browser: webdriver.chrome):
    english_to_french = {}
    frame = WebDriverWait(browser, 600).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="playerFrame"]')))
    browser.switch_to.frame(frame)
    is_first_iteration = True

    while True:
        try:
            if is_first_iteration:
                english_text = WebDriverWait(browser, 600).until(
                    ec.presence_of_element_located((By.ID, "mCSB_10_container")))
                french_text = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="mCSB_7_container"]/div[2]/div[1]/div[1]')))

                english_to_french[english_text.text] = french_text.text
                is_first_iteration = False

            else:
                english_text = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, ".translation_textBox")))
                french_text = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="mCSB_7_container"]/div[2]/div[1]/div[1]')))

                french_input_field = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="userInputText"]')))
                # browser.execute_script("arguments[0].click();", french_input_field)
                ActionChains(browser).send_keys_to_element(french_input_field, french_text.text).perform()

                check_button = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="vocalb_check"]')))
                check_button.click()

                next_button = WebDriverWait(browser, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//*[@id="vocalb_next"]')))
                next_button.click()

                english_to_french[english_text.text] = french_text.text

        except (StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException,
                ElementClickInterceptedException, NoSuchWindowException):
            break

    with open("english_to_french_translations.json", 'w') as f:
        f.write(json.dumps(english_to_french))

    browser.switch_to.default_content()

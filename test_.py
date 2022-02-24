from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    browser.find_element_by_css_selector('button.btn').click()

    browser.find_element_by_css_selector('input[id="answer"]').send_keys(calc(int(browser.find_element_by_css_selector('span[id="input_value"]').text)))

    browser.find_element_by_css_selector('button.btn')
    time.sleep(100)
    assert True == True

finally:
    #browser.quit()
    pass
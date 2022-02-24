from selenium import webdriver


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

input_1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
input_1.send_keys('Val')

input_2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
input_2.send_keys('Val')

input_3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
input_3.send_keys('Val')

input_4 = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]')
input_4.send_keys('Val')

input_5 = browser.find_element_by_css_selector('input[placeholder="Input your address:"]')
input_5.send_keys('Val')

button_1 = browser.find_element_by_tag_name('button')
button_1.click()

assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name('h1').text

browser.quit()
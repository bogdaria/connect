from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/path/to/chromedriver')  # Укажите путь до chromedriver

driver.get("http://localhost:3001/v1.0/browser_profiles/26598613/start")

button = driver.find_element_by_xpath('xpath_of_button')  # Замените 'xpath_of_button' на xpath кнопки
button.click()

input_field = driver.find_element_by_xpath('xpath_of_input')  # Замените 'xpath_of_input' на xpath поля ввода
input_field.send_keys('Your data')  # Замените 'Your data' на данные, которые вы хотите ввести

input_field.send_keys(Keys.RETURN)  # Это нажмет Enter после ввода данных

driver.quit()

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, "price"),'$100')
       )

    button = browser.find_element(By.ID, "book")
    button.click()
    

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    button1 = browser.find_element(By.ID, "solve")
    button1.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
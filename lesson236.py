import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstbtn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    firstbtn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    element1 = browser.find_element(By.ID, "answer")
    element1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
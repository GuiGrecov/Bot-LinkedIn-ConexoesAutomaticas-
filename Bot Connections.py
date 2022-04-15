from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys('my-email')
password.send_keys('my_password')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


# ======= ADD CONTACTS ===========
driver.get("https://www.linkedin.com/search/results/people/?keywords=cientista%20de%20dados%20-comunidade&origin=CLUSTER_EXPANSION&page=6&sid=EyD")
time.sleep(3)

while True:
    all_buttons = driver.find_elements_by_tag_name("button")
    avancar_buttons = [btn1 for btn1 in all_buttons if btn1.text == "Avançar"]
    connect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Enviar agora']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(2)

    for btn1 in avancar_buttons:
        driver.execute_script("arguments[0].click();", btn1)


print("fim")
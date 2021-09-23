from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)


names = ["+972 53-255-8515"]

for name in names:

    person = driver.find_element_by_xpath(r'//span[@title = "{}"]'.format(name))
    person.click()


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

    number = msg[-1]

    reply = driver.find_element_by_class_name("_2S1VP.copyable-text.selectable-text")
    reply.clear()
    reply.send_keys('https://wa.me/972' + number)
    reply.send_keys(Keys.RETURN)

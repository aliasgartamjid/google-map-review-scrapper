from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


website='https://www.google.com/maps/place/Salauddin+Specialized+Hospital+Ltd./@23.7169386,90.4178704,17z/data=!4m7!3m6!1s0x3755b9c74641e61f:0x51a0480487a88dc1!8m2!3d23.7169337!4d90.4200591!9m1!1b1'
driver = webdriver.Chrome()
driver.get(website)

matches = driver.find_elements_by_class_name('wiI7pd')
name = driver.find_elements_by_xpath('//span[@jstcache="1371"]')

while 5==5:
    op = input()

    matches = driver.find_elements_by_class_name('wiI7pd')

    for match in matches:
        print(match.text)







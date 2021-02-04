from selenium.webdriver.support.select import Select
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
import webbrowser
import time


def amazon(product):
    print("\n-------Amazon-------\n")
    ua = UserAgent()
    ua.chrome
    chrome_driver_path = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--kiosk')
    options.add_argument('--window-position=0,0')
    options.add_argument('--disable-infobars')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    #headers = {"User-Agent":}
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    print("User AGent\n")
    user_agent = driver.execute_script("return navigator.userAgent;")
    print(user_agent)
    # driver.get("http://google.com")
    # inputElement = driver.find_element_by_name("q")
    # inputElement.send_keys("Amazon")
    # inputElement.submit()
    driver.get("https://www.amazon.com/")
    #time.sleep(5)
    # elem = driver.find_element_by_partial_link_text("Amazon")
    # print("element found")
    # elem.click()
    elem1 = driver.find_element_by_name("field-keywords")
    elem1.send_keys(product)
    elem1.submit()
    driver.implicitly_wait(50)
    elem2 = driver.find_element_by_partial_link_text(product)
    elem2.click()
    # newURl = driver.window_handles[0]
     # Getting current URL 
    driver.implicitly_wait(50)
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    # driver.switch_to.window(newURl)
    # elem3 = driver.find_element_by_tag_name("span")
    # print(elem3)
    
    # phonenames = driver.find_element(By.ID, "productTitle")
    # print(phonenames)
    # prices=driver.find_element_by_class("_30jeq3 ").click()
    
    # url = driver.get(URL)
    # print(url)
    driver.implicitly_wait(50)
    
    # Getting current URL 
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    pn=driver.find_element_by_id("productTitle")
    price = driver.find_element_by_id("priceblock_ourprice")

    print("\n--------Name----\n")
    print(pn.get_attribute('innerHTML'))
    print("\n")
    print(price.get_attribute('innerHTML'))
#     html = driver.page_source
#     f = open("amazon_product.html", "w")
#     f.write(html)
#     f.close()
#     # time.sleep(2)
#     # print(html)
#     new = 2
#     url = "file:///home/priya/Minor_Project/amazon_product.html"
#     webbrowser.open(url,new=new)

# # close web browser
#     driver.close()
    # myphone=[]
    # myprice=[]

    # for phone in phonenames:
    #     print(phone.text)
    #     myphone.append(phone.text)


    # for price in prices:
    #     print(price.text)	
    #     myprice.append(price.text)
    # finallist=zip(myphone,myprice)

# for data in list(finallist):
# 	print(data)
#     #time.sleep(20)

def flipkart(product):
    print("\n-------------Flipkart-----------\n")
    ua = UserAgent()
    ua.chrome
    chrome_driver_path = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--kiosk')
    options.add_argument('--window-position=0,0')
    options.add_argument('--disable-infobars')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    #headers = {"User-Agent":}
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    print("User AGent\n")
    user_agent = driver.execute_script("return navigator.userAgent;")
    print(user_agent)
    # driver.get("http://google.com")
    # inputElement = driver.find_element_by_name("q")
    # inputElement.send_keys("Amazon")
    # inputElement.submit()
    driver.get("https://www.flipkart.com/")
    #time.sleep(5)
    # elem = driver.find_element_by_partial_link_text("Amazon")
    # print("element found")
    # elem.click()
    elem1 = driver.find_element_by_name("q")
    elem1.send_keys(product)
    elem1.submit()
    driver.implicitly_wait(50)
    elem2 = driver.find_element_by_partial_link_text(product)
    # driver.implicitly_wait(50)
    #elem2.click()
    driver.execute_script("arguments[0].click();", elem2)
    # newURl = driver.window_handles[0]
     # Getting current URL 
    driver.implicitly_wait(50)
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    # driver.switch_to.window(newURl)
    # elem3 = driver.find_element_by_tag_name("span")
    # print(elem3)
    
    # phonenames = driver.find_element(By.ID, "productTitle")
    # print(phonenames)
    # prices=driver.find_element_by_class("_30jeq3 ").click()
    
    # url = driver.get(URL)
    # print(url)
    driver.implicitly_wait(50)
    
    # Getting current URL 
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    pn=driver.find_element_by_class_name("B_NuCI")
    # pn = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")
    price = driver.find_element_by_class_name("_30jeq3 _16Jk6d")

    print("\n--------Name----\n")
    print(pn.get_attribute('innerHTML'))
    print("\n")
    print(price.get_attribute('innerHTML'))
#     html = driver.page_source
#     f = open("amazon_product.html", "w")
#     f.write(html)
#     f.close()
#     # time.sleep(2)
#     # print(html)
#     new = 2
#     url = "file:///home/priya/Minor_Project/amazon_product.html"
#     webbrowser.open(url,new=new)

# # close web browser
#     driver.close()
    # myphone=[]
    # myprice=[]

    # for phone in phonenames:
    #     print(phone.text)
    #     myphone.append(phone.text)


    # for price in prices:
    #     print(price.text)	
    #     myprice.append(price.text)
    # finallist=zip(myphone,myprice)

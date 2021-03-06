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
    print("-----------------Amazon----------------------")
    ua = UserAgent()
    ua.chrome
    chrome_driver_path = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('headless')
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
    driver.get("https://www.amazon.com/")
    #time.sleep(5)
    # elem = driver.find_element_by_partial_link_text("Amazon")
    # print("element found")
    # elem.click()
    elem1 = driver.find_element_by_name("field-keywords")
    elem1.send_keys(product)
    elem1.submit()
    driver.implicitly_wait(50)
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
  #  elem2 = driver.find_element_by_partial_link_text(product)
    elem2 = driver.find_element_by_partial_link_text(product)
    elem2.click()
    # driver.execute_script("arguments[0].click();", elem2)
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    #elem2.click()
    # newURl = driver.window_handles[0]
     # Getting current URL 
    driver.implicitly_wait(50)
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    driver.implicitly_wait(50)
    get_url = driver.current_url
    
  
    # # Printing the URL 
    print(get_url) 
    # pn=driver.find_element_by_class_name("B_NuCI")
    pn=driver.find_element_by_id("productTitle")
    price = driver.find_element_by_id("priceblock_ourprice")

    # print("\n--------Name----\n")
    # print(pn.get_attribute('innerHTML'))
    # print("\n")
    # print(price.get_attribute('innerHTML'))
    print("\n--------Name----\n")
    title = pn.get_attribute('innerText')
    print(title)
    print("\n")
    price = price.get_attribute('innerHTML')
    print(price)
    driver.close()
    return title, price, get_url

def flipkart(product):
    print("\n-------------Flipkart-----------\n")
    ua = UserAgent()
    ua.chrome
    chrome_driver_path = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--kiosk')
    options.add_argument('headless')
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
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
  #  elem2 = driver.find_element_by_partial_link_text(product)
    elem2 = driver.find_element_by_partial_link_text(product)
    driver.execute_script("arguments[0].click();", elem2)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    #elem2.click()
    # newURl = driver.window_handles[0]
     # Getting current URL 
    driver.implicitly_wait(50)
    get_url = driver.current_url 
  
    # Printing the URL 
    print(get_url) 
    driver.implicitly_wait(50)
    get_url = driver.current_url 
  
    # # Printing the URL 
    print(get_url) 
    pn = driver.find_element_by_css_selector("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div:nth-child(1) > h1 > span")
    price = driver.find_element_by_css_selector("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d")
    print("\n--------Name----\n")
    title = pn.get_attribute('innerText')
    print(title)
    print("\n")
    price = price.get_attribute('innerHTML')
    print(price)
    driver.close()
    return title,price, get_url

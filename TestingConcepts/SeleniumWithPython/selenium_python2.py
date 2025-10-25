""""
DOM - Document Object Model:
1. When a web page loads, the browser reads the HTML and creates a tree-like structure called the DOM.
2. Each element (like <div>, <p>, <button>, etc.) becomes a node in that tree.
3. The DOM lets JavaScript (or other scripts) interact with, modify, or update the webpage dynamically
    — like changing text, styles, or adding/removing elements without reloading the page.
EX:
        <html>
          <body>
            <h1>Hello</h1>
            <p>Welcome to the DOM</p>
          </body>
        </html>

WEB ELEMENT:
1. Web elements are the individual components or parts of a webpage’s user interface (UI)
    that you can interact with or test using automation tools like Selenium.
EX:
    Search box, Buttons, Dropdowns
2. We need locators to identify the web elements

Tools to find xpath easily: SELECTORHUB

LOCATING ELEMENTS:
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "//xpath")
find_element(By.LINK_TEXT, "text")
find_element(By.PARTIAL_LINK_TEXT, "partial")
find_element(By.TAG_NAME, "tag")
find_element(By.CLASS_NAME, "class")
find_element(By.CSS_SELECTOR, "css")

To find multiple elements (these methods will return a list)
find_elements(By.ID, "id")
find_elements(By.NAME, "name")
find_elements(By.XPATH, "//xpath")
find_elements(By.LINK_TEXT, "text")
find_elements(By.PARTIAL_LINK_TEXT, "partial")
find_elements(By.TAG_NAME, "tag")
find_elements(By.CLASS_NAME, "class")
find_elements(By.CSS_SELECTOR, "css")

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# from webdriver_manager.chrome import ChromeDriverManager  #No need to install this package after 4.6 version of selenium

class DemoFindElementByID():
    def locate_by_id_demo(self):
        chrome_options = Options()  # Creating object for Options() class - chrome_options
        chrome_options.add_experimental_option("detach",True)  # Keep browser open, because python automatically closes browser after execution is done
        # driver = webdriver.Chrome(ChromeDriverManager().install()) # No need to use ChromeDriverManager().install() after 4.6 version
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        # wait = WebDriverWait(driver, 10)
        driver.find_element(By.CLASS_NAME,"a-button-text").click()
        driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
        driver.find_element(By.ID,"ap_email_login").send_keys("nani00889791@gmail.com")
        driver.find_element(By.CLASS_NAME,"a-button-input").click()
        driver.find_element(By.ID,"ap_password").send_keys("Fall@2025")
        driver.find_element(By.ID,"signInSubmit").click()
        print(driver.title)
        # time.sleep(10)
        # driver.find_element(By.XPATH, "//div[contains(@style, 'opacity: 1; transition: opacity 225ms')]//div/input[@id='mobile-number']").click()

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

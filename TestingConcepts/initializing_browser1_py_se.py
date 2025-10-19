"""---------------------------------Executing in Chrome---------------------------------------------"""
from selenium import webdriver
# used to customize the behavior of the Chrome browser before it starts.
# configure Chrome settings, arguments, extensions, and experimental options
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # Creating object for Options() class - chrome_options
chrome_options.add_experimental_option("detach", True)  # Keep browser open, because python automatically closes browser after execution is done

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.rcvacademy.com")
driver.maximize_window()    # To maximize window
print(driver.title)
# driver.close()  #driver.quit() - To close the browser (No need to mention it in python)
"""---------------------------------Executing in Edge------------------------------------------------
from selenium import webdriver
from selenium.webdriver.edge.options import Options

edge_options = Options() # Creating object for Options() class - edge_options
edge_options.add_experimental_option("detach", True)  # Keep browser open, because python automatically closes browser after execution is done

driver = webdriver.Chrome(options=edge_options)
driver.get("https://www.rcvacademy.com")
driver.maximize_window()    # To maximize window
print(driver.title)
# driver.close()  #driver.quit() - To close the browser (No need to mention it in python)
--------------------------------------------------------------------------------------------------"""
"""---------------------------------Executing in Firefox---------------------------------------------
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options() # Creating object for Options() class - firefox_options
firefox_options.set_preference("detach", True)  # Keep browser open, because python automatically closes browser after execution is done

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.rcvacademy.com")
driver.maximize_window()    # To maximize window
print(driver.title)
# driver.close()  #driver.quit() - To close the browser (No need to mention it in python)
--------------------------------------------------------------------------------------------------"""
"""------------------------------Information---------------------------------------------------------
Starting from Selenium v4.6.0,
👉 you no longer need to manually download or specify paths for browser drivers like:
chromedriver.exe, geckodriver.exe, msedgedriver.exe
👉 In previous versions we should explicitly download the webdriver-manager package
It helps to initialize the browser automatically instead of downloading all the browsers

chrome_options.add_argument("--headless")		Run Chrome without a GUI (no visible window)
chrome_options.add_argument("--start-maximized")	Open browser maximized
chrome_options.add_argument("--incognito")		Launch Chrome in Incognito mode
chrome_options.add_experimental_option("detach", True)	Keep browser open even after the script ends
chrome_options.add_experimental_option(			Hide the “Chrome is being controlled by automated test 						"excludeSwitches", ["enable-automation"])	software” message
chrome_options.binary_location = "path/to/chrome.exe"	Use a custom Chrome binary if needed
chrome_options.add_extension("path/to/extension.crx")	Load a Chrome extension
--------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------------
Old Method to initialize Web Browser
selenium/
│
├── webdriver/
│   ├── __init__.py
│   ├── chrome/
│   │   ├── __init__.py
│   │   ├── service.py   ← we are importing from here
│   │   ├── options.py
│   │   └── webdriver.py
│   ├── firefox/
│   └── edge/

from selenium import webdriver      # selenium - Package, webdriver - Module(or Sub-Package)  
from selenium.webdriver.chrome.service import Service   # selenium - Package, webdriver - Sub-Package, chrome - Subpackage, service - module, Service - Class

service = Service("C:\\browserdrivers\\chromedriver.exe") # Creating service object
driver = webdriver.Chrome() # Creating instance for Chrome Webdriver
driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
-------------------------------------------------------------------------------------------------"""
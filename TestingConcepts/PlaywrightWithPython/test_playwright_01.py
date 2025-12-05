"""
Command to execute:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v
To run in headed mode:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v --headed
To run specific testcase:
            python -m pytest PlaywrightWithPython/test_playwright_01.py::test_verifyTitle -s -v --headed
Command to run in specific browser:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v --headed --browser firefox
Command to run in 2 or more browsers:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v --headed --browser firefox --browser webkit --browser chromium
To run in parallel mode:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v --headed --numprocesses 2
To run in parallel using specific browser:
            python -m pytest PlaywrightWithPython/test_playwright_01.py -s -v --headed --numprocesses 2 --browser chromium --browser firefox

Built an inbuilt fixture - Page fixture (A reusable function)
By default it executes Chromium (Chrome/Edge)
By default playwright execute in headless mode
headless - no UI
headed - We can see the UI with the interactions
"""
from playwright.sync_api import Page, expect  # Page is class


def test_verifyPageUrl(page: Page):
    page.goto("http://www.automationpractice.pl/index.php")
    # myurl = page.url    # get the url
    # print("URL of the application: ", myurl)
    expect(page).to_have_url("http://www.automationpractice.pl/index.php")  # Verifying - Assertion method expect()


def test_verifyTitle(page: Page):
    page.goto("http://www.automationpractice.pl/index.php")
    # mytitle = page.title()  # get the title
    # print("URL of the application: ", mytitle)
    expect(page).to_have_title("My Shop")  # Verifying the title - Assertion

"""
Assertions:
to_have_url()
to_have_title()
"""
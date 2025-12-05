"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_browser_context_13.py -s -v

Browser Context Page:

multiple pages can be created through context.
It helps to execute the different pages parallel.

"""

from playwright.sync_api import sync_playwright, Page, expect, Playwright


# Browser --> Context ---> Page
def test_browsercontext(playwright:Playwright):
    # chromium = playwright.chromium
    # browser = chromium.launch()

    browser1 = playwright.chromium.launch(headless=False)  # Created browser
    context1 = browser1.new_context()     # Created context
    page1 = context1.new_page()   # Created page

    browser2 = playwright.firefox.launch(headless=False)  # Created browser
    context2 = browser2.new_context()  # Created context
    page2 = context2.new_page()  # Created page

    page1.goto("https://www.selenium.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Selenium")
    print("Execution Done in Chrome")

    page2.goto("https://www.python.org/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Welcome to Python.org")
    print("Execution Done in Firefox")
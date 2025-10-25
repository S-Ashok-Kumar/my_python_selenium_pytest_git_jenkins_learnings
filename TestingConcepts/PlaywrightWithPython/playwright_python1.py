""""
Playwright:
-----------
Playwright is a powerful and modern browser automation tool that helps you
test web apps faster, easier, and more reliably than older tools like Selenium.
| Feature                      | Playwright                   | Explanation                                           |
| -----------------------------| -----------------------------| ------------------------------------------------------|
| 🧭 Multi-browser support     | Chrome, Firefox, Safari, Edge| Test across all browsers easily                       |
| ⚡ Fast                       | Very quick and stable        | Less flaky than Selenium                              |
| 🧩 Auto-waiting              | Yes                          | Waits for elements automatically (no need for `sleep`)|
| 👥 Multiple tabs/contexts    | Built-in                     | Can handle multiple pages easily                      |
| 🧱 Cross-language            | JS/TS, Python, Java, .NET    | Use your favorite language                            |
| 🧠 Smart locators            | `page.get_by_text("Login")`  | Easier to find elements                               |
| 🔄 Record tests automatically| Yes                          | Can generate code from your clicks                    |

Install Playwright: pip install playwright
To install all the browsers: python -m playwright install
Playwright Version: python -m playwright --version
To launch Website: python -m playwright codegen URL (EX: https://www.google.com/chrome/index.html)
To run a python-playwright file: python .\PlaywrightWithPython\playwright_python1.py
"""
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.com/")
    page.get_by_role("button", name="Continue shopping").click()
    page.get_by_role("link", name="Hello, sign in Account & Lists").click()
    page.get_by_role("textbox", name="Enter your mobile number or").click()
    page.get_by_role("textbox", name="Enter your mobile number or").fill("nani00889791@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").fill("Fall@2025")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name="Amazon", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_screenshots_14.py -s -v --headed

Capture screenshot through code
"""

from playwright.sync_api import Page, expect, Playwright
import time
import datetime


def test_screenshots(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # timestamp = str(int(time.time()))
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = "PlaywrightWithPython/Screenshots/"
    # path = f"PlaywrightWithPython/Screenshots/homepage_{timestamp}.png"

    # Partial Page Screenshot
    # page.screenshot(path=path)
    page.screenshot(path=f"{path}partial_homepage_{timestamp}.png")

    # Full page screenshot
    page.screenshot(path=f"{path}fullpage_homepage_{timestamp}.png", full_page=True)

    #Element/specific section of the page screenshot
    logo = page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"{path}element_homepage_{timestamp}.png")

"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_auth_popup_13.py -s -v --headed

Authentication popup:

#Direct - inject user login with url

# https://the-internet.herokuapp.com/basic_auth

# https://admin:admin@the-internet.herokuapp.com/basic_auth
"""

import pytest
from playwright.sync_api import Playwright, expect, Page

# Using link - we can pass username and password inside the url
@pytest.mark.skip
def test_authPopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(5000)

# Using context - we can pass user and password along with the context
def test_authPopup_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(5000)
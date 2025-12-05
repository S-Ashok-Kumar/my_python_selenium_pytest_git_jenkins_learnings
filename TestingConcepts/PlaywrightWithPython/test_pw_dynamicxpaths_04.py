"""
Xpath:
//button[text()='START' or text()='STOP']
//button[@name='START' or @name='STOP']
//button[contains(@name,'st')]
//button[starts-with(@name,'st')]

CSS:
button[name='start'],button[name='stop']    or  [name='start'],[name='stop']
button[name^='st']
button[name*='st']

"""

import pytest
import re
from playwright.sync_api import Page, expect

def test_verify_dynamicxpths(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for time in range(5):
        button = page.locator("//button[text()='START' or text()='STOP']")    # Xpath
        # button = page.locator("button[name^='st']")     #CSS
        # button = page.get_by_role("button",name=re.compile(r"ST.*"))        #Regular expressions
        button.click()
        page.wait_for_timeout(5000)
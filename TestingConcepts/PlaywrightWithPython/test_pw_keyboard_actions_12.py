"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_keyboard_actions_12.py -s -v --headed

Keyboard Actions:
"""

import pytest
from playwright.sync_api import Page, expect

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1 = page.locator("#input1")

    #1. Focus on input1
    input1.focus()

    #2. Provide the text in input1
    page.keyboard.insert_text("Welcome")

    #3. Press CTRL+A
    page.keyboard.press("Control+A")

    #4. Press CTRL+C
    page.keyboard.press("Control+C")

    #5. Press "Tab" to move to next field (input2)
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #6. Press CTRL+V - Paste the text inside the 2nd input box - input2
    page.keyboard.press("Control+V")

    # 5. Press "Tab" to move to next field (input3)
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 6. Press CTRL+V - Paste the text inside the 3rd input box - input3
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")
    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")

    page.wait_for_timeout(5000)
"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_simple_dialog_box_10.py -s -v --headed

Simple Alert

to handle the alert we need to register an event before performing click() action.
"""
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_timeout(5000)

    # Approach 1 - Not preferred
    # Registering an event
    def handle_dialog(dialog):
        dialog.accept()
    page.on("dialog", handle_dialog)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)



def test_simple_dialog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_timeout(5000)

    # Approach 2 - preferred
    # Registering an event
    page.on("dialog", lambda dialog:dialog.accept())    #lambda parameters: expression
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)
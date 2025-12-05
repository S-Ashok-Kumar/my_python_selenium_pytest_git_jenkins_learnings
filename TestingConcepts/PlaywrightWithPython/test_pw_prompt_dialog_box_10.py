"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_prompt_dialog_box_10.py -s -v --headed

Prompt alert/ dialog box

to handle the alert we need to register an event before performing click() action.
"""
from playwright.sync_api import Page, expect


def test_prompt_dialog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_timeout(5000)

    # Registering an event
    page.on("dialog", lambda dialog:dialog.accept("John"))    # It is to pass value & accept the alert
    # page.on("dialog", lambda dialog: dialog.dismiss())  # It is to dismiss the alert
    page.wait_for_timeout(3000)
    page.locator("#promptBtn").click()
    page.wait_for_timeout(5000)

    text = page.locator("#demo")
    print("Output text ====>", text.inner_text())

    expect(text).to_have_text("Hello John! How are you today?")
    # expect(text).to_contain_text("John")
    page.wait_for_timeout(5000)

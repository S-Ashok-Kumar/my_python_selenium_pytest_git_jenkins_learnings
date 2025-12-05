"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_conformation_dialog_box_10.py -s -v --headed

Conformation alert

to handle the alert we need to register an event before performing click() action.
"""
from playwright.sync_api import Page, expect


def test_conformation_dialog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_timeout(5000)

    # Registering an event
    # page.on("dialog", lambda dialog:dialog.accept())    # It is to accept the alert
    page.on("dialog", lambda dialog: dialog.dismiss())  # It is to dismiss the alert
    page.wait_for_timeout(3000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)

    text = page.locator("#demo")
    print("Output text ====>", text.inner_text())

    # expect(text).to_have_text("You pressed OK!")    # Verifies when alert is accepted
    expect(text).to_have_text("You pressed Cancel!")  # Verifies when alert is accepted
    page.wait_for_timeout(5000)

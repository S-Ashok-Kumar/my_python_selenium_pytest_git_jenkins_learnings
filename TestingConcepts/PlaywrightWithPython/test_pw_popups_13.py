"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_popups_13.py -s -v

"""

from playwright.sync_api import sync_playwright, expect, Playwright
from pytest_playwright.pytest_playwright import browser


def test_handle_popups(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # def handle_popup(popup):
    #     popup.wait_for_load_state()
    # page.on("popup", handle_popup)

    page.on("popup", lambda popup: popup.wait_for_load_state())
    page.locator("#PopUp").click()

    page.wait_for_timeout(5000)

    all_popup_pages = context.pages
    print("Total number of popups and pages: ", len(all_popup_pages))

    # Capture urls of all the popup pages.
    for pup in all_popup_pages:
        print("Popup/Page URL=====> ",pup.url)
        title = pup.title()

        if "Selenium" in title:
            expect(pup).to_have_title("Selenium")
            pup.locator("a[href='https://seleniumconf.com/register/?utm_medium=Referral&utm_source=selenium.dev&utm_campaign=register']").click()
            pup.wait_for_timeout(5000)
            pup.close()

    page.wait_for_timeout(5000)
    context.close()
    browser.close()
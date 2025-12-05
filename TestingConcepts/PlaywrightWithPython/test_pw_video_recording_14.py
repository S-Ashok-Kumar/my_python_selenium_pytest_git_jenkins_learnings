"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_video_recording_14.py -s -v

Capture video through code
"""

from playwright.sync_api import sync_playwright, expect, Playwright


def test_video_recording(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir= "PlaywrightWithPython/videos/",
        record_video_size={"width":1024, "height": 768}
    )
    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.locator('#login2').click()
    page.locator("#loginusername").fill('nani2024')
    page.locator("#loginpassword").fill('Nani@2024')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome nani2024")

    context.close()
    browser.close()
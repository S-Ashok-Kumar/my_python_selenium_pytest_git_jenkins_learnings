"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_tracing_14.py -s -v

Command to open the trace.zip file in CMD:
                python -m playwright show-trace PlaywrightWithPython/trace_file/trace.zip

Capture tracing through code:
Advantages:
Time travel - see where and when the error occurred.
Can see Actions, Metadata,
Can see Action, Before, After
"""

from playwright.sync_api import sync_playwright, expect, Playwright


def test_tracing(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Starting the trace
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.locator('#login2').click()
    page.locator("#loginusername").fill('nani2024')
    page.locator("#loginpassword").fill('Nani@2024')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome nani2024")

    # Stopping the trace
    context.tracing.stop(path="PlaywrightWithPython/trace_file/trace.zip")

    context.close()
    browser.close()
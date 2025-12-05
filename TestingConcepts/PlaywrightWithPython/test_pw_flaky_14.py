"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_flaky_14.py -s -v --headed --reruns 3 --reruns-delay 2

Auto Retry (Rerun)
    flaky tests  - test case sometimes fail and sometime pass, because of unstable
                 - Based on the count we provide it will retry the failed test case.
                   if testcase is passed in first time only then the execution will be quit
                 - To achieve auto retrieve in playwright, we need to install a plugin.
                    Plug-in: pytest-rerunfailures
                    pip install pytest-rerunfailures
"""
from playwright.sync_api import Page, expect


def test_flaky_login(page:Page):

    page.goto("https://demoblaze.com/index.html")
    page.wait_for_timeout(5000)
    page.locator('#login2').click()
    page.locator("#loginusername").fill('nani2024')
    page.locator("#loginpassword").fill('Nani@2024')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(10000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome nani2024")

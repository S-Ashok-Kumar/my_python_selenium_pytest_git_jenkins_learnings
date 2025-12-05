"""
Command to execute:
                    python -m pytest PlaywrightWithPython/test_pw_datadriven_login_15.py -s -v --headed

Valid data + Successful test case = Test case pass
Valid data + Unsuccessful test case = Test case Fail
Invalid data + Successful test case = Test case Fail
Invalid data + Unsuccessful test case = Test case pass
"""

import pytest
from playwright.sync_api import Page, expect

login_testdata = [("nani00889791@gmail.com", "Fall@2025", "valid"),
                  ("randomf@gmail.com", "Fall@2520", "invalid"),
                  ("validuser@gmail.com", "test@2025", "invalid"),
                  ("", "", "invalid")]


@pytest.mark.parametrize("email, pword, validity", login_testdata)
def test_datadriven_login(email, pword, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("#Email").fill(email)  # email id
    page.locator("#Password").fill(pword)  # Password
    page.locator("input[value='Log in']").click()

    # Validation
    if validity == "valid":
        logout_link = page.locator("a.ico-logout")
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        error_message = page.locator("div.validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)

        # if data is failed then make sure we are in the same place.
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")

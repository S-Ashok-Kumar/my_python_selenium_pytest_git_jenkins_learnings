"""
Command to execute:
                    python -m pytest PlaywrightWithPython/test_pw_datadriven_login_json_15.py -s -v --headed

Valid data + Successful test case = Test case pass
Valid data + Unsuccessful test case = Test case Fail
Invalid data + Successful test case = Test case Fail
Invalid data + Unsuccessful test case = Test case pass
"""

import pytest
from playwright.sync_api import Page, expect, Playwright
import json

# Read json file
path = "PlaywrightWithPython/testdata/data.json"
file = open(path, "r")
login_data = json.load(file)


@pytest.mark.parametrize("email, password, validity", [
    (data["email"], data["password"], data["validity"]) for data in login_data
])
def test_datadriven_json_login(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("#Email").fill(email)  # email id
    page.locator("#Password").fill(password)  # Password
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

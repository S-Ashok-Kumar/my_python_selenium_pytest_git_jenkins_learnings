"""
Command to execute:
                    python -m pytest PlaywrightWithPython/test_pw_datadriven_login_excel_15.py -s -v --headed

prerequisite:
        openpyxl Package
        pip install openpyxl

Valid data + Successful test case = Test case pass
Valid data + Unsuccessful test case = Test case Fail
Invalid data + Successful test case = Test case Fail
Invalid data + Unsuccessful test case = Test case pass
"""

import pytest
from playwright.sync_api import Page, expect, Playwright
import openpyxl

login_data = []

# Read from Excel file
path = "PlaywrightWithPython/testdata/data.xlsx"
workbook = openpyxl.load_workbook(path)
worksheet = workbook.active  # ws = workbook["sheetname"]

for row in worksheet.iter_rows(min_row=2, values_only=True):
    email, password, validity = row
    login_data.append((str(email or ""), str(password or ""), str(validity or "")))
workbook.close()


@pytest.mark.parametrize("email, password, validity", login_data)
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

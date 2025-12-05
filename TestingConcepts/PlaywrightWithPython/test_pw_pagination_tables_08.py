"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_pagination_tables_08.py -s -v --headed
Pagination Tables
"""
import pytest
from playwright.sync_api import Page, expect

# @pytest.mark.skip     # To skip the testcase
def test_static_web_table(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    total_records = ""
    has_more_pages = True
    while has_more_pages:
        rows = page.locator("table#example tbody tr").all()
        for row in rows:
            each_row = row.inner_text()
            total_records += each_row + "\n"
            # print(type(each_row))

        next_button = page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")    # Extract the value of class attribute
        if "disabled" in is_disabled:
            has_more_pages = False
        else:
            next_button.click()
    print(total_records)
    print("Total number of records: ",len(total_records))


def test_filter_rows(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    # Apply filter to get the specified record
    dropdown = page.locator("#dt-length-0")
    dropdown.select_option(label="25")

    rows = page.locator("#example tbody tr")
    print("Total count: ", rows.count())
    expect(rows).to_have_count(25)
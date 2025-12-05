"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_dynamic_tables_08.py -s -v --headed

Dynamic web tables
"""

import pytest
from playwright.sync_api import Page, expect

def test_dynamic_tables(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # Locating the table
    table = page.locator("table.table tbody")

    # Get all the rows from the table
    rows = table.locator("tr").all()

    cpu_load = ""
    for row in rows:
        browser_name = row.locator("td").nth(0).inner_text()
        if browser_name == "Chrome":
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print(browser_name, cpu_load)
            break

    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)
    page.wait_for_timeout(5000)

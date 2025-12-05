"""
Command to execute:
                    python -m pytest PlaywrightWithPython/test_pw_datadriven_items_15.py -s -v --headed --reruns 3 --reruns-delay 2

"""
import pytest
from playwright.sync_api import Page, expect

search_items = ["laptop", "Gift card", "smartphone", "monitor"]

@pytest.mark.parametrize("item",search_items)
def test_search_items(item, page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill(item) # We need to pass search_item name
    page.locator("input[type='submit']").click()

    # Assertion
    first_item = page.locator("h2 a").nth(0)
    expect(first_item).to_contain_text(item, ignore_case=True)

    page.wait_for_timeout(5000)
"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_multi_select_dropdowns_06.py -s -v --headed
Multi select dropdown:
By label
By value
By index
"""

import pytest
from playwright.sync_api import Page, expect


def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Select multiple options from the dropdown - 3 ways
    # page.locator("#colors").select_option(["Red", "Blue", "Green"]) # by label
    page.locator("#colors").select_option(label=["Red", "Blue", "Green"])  # by label
    page.wait_for_timeout(2000)

    page.locator("#colors").select_option(value=["Red", "White", "Green"])  # by values     Need to use "value" keyword
    page.wait_for_timeout(2000)

    page.locator("#colors").select_option(index=[2, 4])  # by index     Need to use "index" keyword
    page.wait_for_timeout(2000)

    #  Check number of options in the dropdown.
    dropdown_opt = page.locator("#colors>option")
    count = dropdown_opt.count()
    print("count: ", count)
    expect(dropdown_opt).to_have_count(count)
    page.wait_for_timeout(5000)


"""
Methods:
all_text_contents() - returns list of elements which matches the locator
count()             - returns total count of elements which matches the locator
select_option(label="<provide label here>") - Used for single selection dropdown by using label
select_option(value="<provide value here>") - Used for single selection dropdown by  using value
select_option(label="<provide index here>") - Used for single selection dropdown by  using index
select_option(label="<provide list of labels here>") - Used for multi selection dropdown by  using label
select_option(value="<provide list of values here>") - Used for multi selection dropdown by using value
select_option(label="<provide list of indexes here>") - Used for multi selection dropdown by using index
locator("<Pass css/xpath here>") -Helps to find the element on the webpage.

"""

"""
Assertions:
to_have_count(<provide count you are expecting>)

"""

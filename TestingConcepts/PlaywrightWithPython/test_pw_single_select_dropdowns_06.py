"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_single_select_dropdowns_06.py -s -v --headed
Single select dropdown.

3 ways to select option from the dropdown
By label    : select_option(label="India")
By Value    : select_option(value="germany")
By Index    : select_option(index=4)
"""


import pytest
from playwright.sync_api import Page, expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    # Select by label
    page.locator("#country").select_option("India")     # by label   # OR
    # page.locator("#country").select_option(label="India") # by label
    page.wait_for_timeout(5000)

    # Select by Value
    page.locator("#country").select_option("germany")      #by value    #OR
    # page.locator("#country").select_option(value="germany")  # by value
    page.wait_for_timeout(2000)

    # Select by Index
    page.locator("#country").select_option(index=4) # by Index
    page.wait_for_timeout(2000)

    # Check number of options in the dropdown.
    dropdown_opt = page.locator("#country>option")
    count = dropdown_opt.count()
    print("count: ",count)
    expect(dropdown_opt).to_have_count(count)

    lis_dropdown = dropdown_opt.all_text_contents()
    option_dropdown = [text.strip() for text in lis_dropdown]
    print(option_dropdown)
    page.wait_for_timeout(2000)

    # Print countries using loops
    for opt in option_dropdown:
        print(opt)


"""
Methods:
all_text_contents() - returns list of elements which matches the locator
count()             - returns total count of elements which matches the locator
select_option(label="<provide label here>") - Used for single selection dropdown by using label
select_option(value="<provide value here>") - Used for single selection dropdown by  using value
select_option(label="<provide index here>") - Used for single selection dropdown by  using index
locator("<Pass css/xpath here>") -Helps to find the element on the webpage.

"""

"""
Assertions:
to_have_count(<provide count you are expecting>)

"""
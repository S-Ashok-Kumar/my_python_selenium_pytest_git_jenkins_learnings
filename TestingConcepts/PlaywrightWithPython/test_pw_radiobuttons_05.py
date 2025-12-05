
"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_radiobuttons_05.py -s -v --headed
Actions - Working with Input box, Radio buttons, and Checkboxes

"""

import pytest
from playwright.sync_api import Page, expect

def test_radiobuttons(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    radio_btn = page.locator("#male")

    # Visibility of element and Enable or not
    expect(radio_btn).to_be_visible()
    expect(radio_btn).to_be_enabled()

    # male radio button should not be checked (default)
    expect(radio_btn).not_to_be_checked()

    # Select/Check radio button
    radio_btn.check()

    # male radio button should be checked (default)
    expect(radio_btn).to_be_checked()

    page.wait_for_timeout(5000)


"""
Methods:
fill("sendkeys-value")      - Used to write values in the text areas.
count()                     - Returns the total length
check()                     - checks the radio button/ checkboxes
uncheck()                   - unchecks the radio button/ checkboxes
text_content()              - Returns specific element which matches the locator
first.text_content()        - Returns first element which matches the locator
last.text_content()         - Returns last element which matches the locator
nth(index).text_content()   - Returns nth(index) element which matches the locator 
all_text_content()          - Returns a list of web elements
get_attribute("attribute")  - Returns value
input_value()               - Returns what value we passed into the textarea.
"""

"""
Assertions:
to_be_visible()
to_be_enabled()
to_be_checked()     - Verify the radio button/checkbox are selected
not_to_be_checked()     - Verify the radio button/checkbox are not selected
to_have_url("url")
to_have_title("title_name_you_want_to_verify")
to_have_text("value_you_want_to_verify")
to_have_count("total_length.count()")
to_have_attribute("attribute","Value")

"""

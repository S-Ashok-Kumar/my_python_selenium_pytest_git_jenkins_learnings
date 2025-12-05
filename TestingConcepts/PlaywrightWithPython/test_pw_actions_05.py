"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_actions_05.py -s -v --headed
Actions - Working with Input box, Radio buttons, and Checkboxes

"""

import pytest
from playwright.sync_api import Page, expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box = page.locator("#name")

    # Visibility of element and Enable or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    # Check the attribute of the elements
    expect(text_box).to_have_attribute("maxlength","15")

    # get an attribute value of the element
    maxlength = text_box.get_attribute("maxlength")
    print("Max Length of inputbox:", maxlength)

    # Fill the text
    text_box.fill("John Kenedy")

    # get the input value from input box (the input we provided)
    enteredvalue = text_box.input_value()
    print("Entered Value is: ", enteredvalue)

    page.wait_for_timeout(5000)


"""
Methods:
fill("sendkeys-value")      - Used to write values in the text areas.
count()                     - Returns the total length
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
to_have_url("url")
to_have_title("title_name_you_want_to_verify")
to_have_text("value_you_want_to_verify")
to_have_count("total_length.count()")
to_have_attribute("attribute","Value")
"""
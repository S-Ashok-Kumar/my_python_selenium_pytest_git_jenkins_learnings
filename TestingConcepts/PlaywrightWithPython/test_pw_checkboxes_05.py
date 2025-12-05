"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_checkboxes_05.py -s -v --headed
Actions - Working with Input box, Radio buttons, and Checkboxes

check()
Checks the checkbox only if it is not already checked.
If it is already selected, Playwright does nothing (no error, no uncheck).
"""
from calendar import weekday

import pytest
from playwright.sync_api import Page, expect


def test_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1. Select specific checkbox (sunday)
    sunday_checkbox = page.get_by_label("Sunday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(5000)

    # 2. Count number of checkboxes
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # checkboxes = []
    #
    # for day in days:
    #     checkbox = page.get_by_label(day)
    #     checkboxes.append(checkbox)

    checkboxes = [page.get_by_label(day) for day in days]
    print("Total number of checkboxes: ", len(checkboxes))

    # 3. Select all the checkboxes and assert each checkbox is selected.
    for ckbox in checkboxes:
        ckbox.check()
        expect(ckbox).to_be_checked()

    # 4. Uncheck or unselect the last 3 checkboxes
    for ckbox in checkboxes[-3:]:
        ckbox.uncheck()
        expect(ckbox).not_to_be_checked()

    # 5. Toggle checkboxes
    for ckbox in checkboxes:
        if ckbox.is_checked():
            ckbox.uncheck()
            expect(ckbox).not_to_be_checked()
        else:
            ckbox.check()
            expect(ckbox).to_be_checked()

    # 6. Randomly Check checkboxes - check 1, 3, 6 checkboxes
    indexs = [1, 3, 6]
    for i in indexs:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()

    # 7. Select checkbox based on the label or input
    weekday = "Sunday"
    for label in days:
        if label == weekday:
            ckbox = page.get_by_label(label)
            ckbox.check()
            expect(ckbox).to_be_checked()

    page.wait_for_timeout(5000)


"""
Methods:
fill("sendkeys-value")      - Used to write values in the text areas.
count()                     - Returns the total length
check()                     - checks the radio button/ checkboxes
uncheck()                   - unchecks the radio button/ checkboxes
is_checked()                - returns True if the checkbox is selected, False if not selected.
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
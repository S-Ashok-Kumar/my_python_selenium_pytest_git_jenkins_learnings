"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_jquery_datepicker_09.py -s -v --headed

jQuery Date Picker
"""


import pytest
from playwright.sync_api import Page, expect

def select_date(page, target_year, target_month, target_date, is_future):

    # Selecting month and year from the date picker
    while True:
        current_month = page.locator("span.ui-datepicker-month").text_content()
        current_year = page.locator("span.ui-datepicker-year").text_content()

        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
            page.locator(".ui-datepicker-next").click()    # For future date
        else:
            page.locator(".ui-datepicker-prev").click()    # For past date

    # Selecting date from the date picker
    all_dates = page.locator(".ui-datepicker-calendar td").all()

    for dt in all_dates:
        date_text = dt.inner_text()
        if date_text == target_date:
            dt.click()
            break


def test_jquery_date_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input = page.locator("#datepicker")

    #Approach 1
    date_input.fill("10/15/2025")   # mm/dd/yyyy
    expect(date_input).to_have_value("10/15/2025")
    page.wait_for_timeout(5000)

    #Approach 2
    # If future date: is_future = True, If past date: is_future = False
    is_future = False
    year = "2025"
    month = "October"
    date = "15"

    date_input.click()
    select_date(page, year, month, date, is_future)
    print("Selected date: ",date_input.input_value())
    expect(date_input).to_have_value("10/15/2025")
    page.wait_for_timeout(5000)

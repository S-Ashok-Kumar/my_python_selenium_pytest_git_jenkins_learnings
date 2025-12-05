"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_bootstrap_datepicker_09.py -s -v --headed

Bootstrap Date picker

Need to handle popup in this page while selecting date. Remember
"""

from playwright.sync_api import Page, expect

# Implementation for check-in date
def select_checkin_date(page, year, month, day):
    while True:
        checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()
        current_month, current_year = checkin_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click() # Go to next month

    all_dates = page.locator('table.b8fcb0c66a tbody').nth(0).locator('td').all()
    for date in all_dates:
        if date.inner_text() == day:
            print(date)
            date.click()
            break

# Implementation for check-in date
def select_checkout_date(page, year, month, day):
    while True:
        checkout_month_year = page.locator("h3[aria-live='polite']").nth(1).inner_text()
        current_month, current_year = checkout_month_year.split(" ")

        if current_month == month and current_year == year:
            break
        else:
            page.locator("button[aria-label='Next month']").click() # Go to next month

    all_dates = page.locator('table.b8fcb0c66a tbody').nth(1).locator('td').all()

    for date in all_dates:
        if date.inner_text() == day:
            print(date)
            date.click()
            break


def test_bootstrap_date_picker(page:Page):
    page.goto("https://www.booking.com/")
    page.get_by_test_id("searchbox-dates-container").click()
    # page.pause()
    page.get_by_test_id("searchbox-dates-container").click()

    select_checkin_date(page, "2026", "January", "2")
    select_checkout_date(page, "2026", "February", "5")

    checkin_text = page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text = page.locator("span[data-testid='date-display-field-end']").inner_text()

    # print("Checkin date=======> ",checkin_text)
    # print("Checkin date=======> ", checkout_text)

    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    page.wait_for_timeout(5000)

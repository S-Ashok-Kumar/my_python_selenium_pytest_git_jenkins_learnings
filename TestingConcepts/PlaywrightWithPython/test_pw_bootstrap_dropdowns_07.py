"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_bootstrap_dropdowns_07.py -s -v --headed

Bootstrap Dropdowns & Hidden Dropdown:
--------------------------------------
When you inspect the screen the options under that dropdown may or may not display in the HTML DOM
So we call them Bootstrap Dropdown & Hidden Dropdown.
"""

import pytest
from playwright.sync_api import Page, expect

def test_bootstrap_dropdown(page:Page):
    page.goto("https://bstackdemo.com/#")

    # Click on sign-in
    page.locator("span#signin").click()

    # Click on username
    page.locator("form div#username").click()

    # Capture all the options from username dropdown
    options = page.locator("div[tabindex='-1']")
    unames_count = options.count()
    print("Total number of usernames: ", unames_count)
    expect(options).to_have_count(unames_count)

    # print all the username options
    print("All the option from Username Dropdown: ", options.all_text_contents())

    # print all the usernames options using loop
    for i in range(unames_count):
        print(options.nth(i).text_content())

    page.wait_for_timeout(5000)

    # # Select/click on specific options
    # for i in range(unames_count):
    #     text = options.nth(i).text_content()
    #     if text == 'fav_user':
    #         options.nth(i).click()
    #         break

    # Click one option from username dropdown
    page.locator("div#react-select-2-option-0-2").click()

    # Click on password
    page.locator("form div#password").click()
    page.locator("div#react-select-3-option-0-0").click()

    # Click on login
    page.locator("button#login-btn").click()
    page.wait_for_timeout(5000)


"""
Methods:
click() - Used to click on the element where the locator is pointing 
all_text_contents() - returns list of all the elements which matches the locator
text_content() - returns a single/specific element which matches the locator
count()             - returns total count of elements which matches the locator
select_option(label="<provide label here>") - Used for single selection dropdown by using label
select_option(value="<provide value here>") - Used for single selection dropdown by  using value
select_option(label="<provide index here>") - Used for single selection dropdown by  using index
select_option(label="<provide list of labels here>") - Used for multi selection dropdown by  using label
select_option(value="<provide list of values here>") - Used for multi selection dropdown by using value
select_option(label="<provide list of indexes here>") - Used for multi selection dropdown by using index
locator("<Pass css/xpath here>") -Helps to find the element on the webpage.
copy() - python method used to create copy of original list.
sorted() - python method used to sort the list in ASCENDING/DESCENDING.
"""

"""
Assertions:
to_have_count(<provide count you are expecting>)
"""

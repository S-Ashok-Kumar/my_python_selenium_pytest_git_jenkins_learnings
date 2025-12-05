"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_sorted_dropdowns_06.py -s -v --headed

"""

import pytest
from playwright.sync_api import Page, expect

def test_sorteddropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_ani_opt = page.locator("#animals>option")     #Sorted list
    option_ani_text = [text.strip() for text in dropdown_ani_opt.all_text_contents()]
    original_ani_list = option_ani_text.copy()  # before sorting
    sorted_ani_list = sorted(option_ani_text)  # after sorting
    print("Original Animal List: ", original_ani_list)
    print("Sorted Animal List: ", sorted_ani_list)
    if original_ani_list == sorted_ani_list:
        print("Animal dropdown options are in sorted order.....")
        # assert True
    else:
        print("Animal dropdown options are not in sorted order.....")
        # assert False

    dropdown_col_opt = page.locator("#colors>option")  # unsorted list
    option_col_text = [text.strip() for text in dropdown_col_opt.all_text_contents()]
    original_col_list = option_col_text.copy()      # before sorting
    sorted_col_list = sorted(option_col_text)        # after sorting
    print("Original Color List: ",original_col_list)
    print("Sorted Color List: ", sorted_col_list)
    if original_col_list == sorted_col_list:
        print("Color dropdown options are in sorted order.....")
        # assert True
    else:
        print("Color dropdown options are not in sorted order.....")
        # assert False


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
copy() - python method used to create copy of original list.
sorted() - python method used to sort the list in ASCENDING/DESCENDING.
"""

"""
Assertions:
to_have_count(<provide count you are expecting>)
"""

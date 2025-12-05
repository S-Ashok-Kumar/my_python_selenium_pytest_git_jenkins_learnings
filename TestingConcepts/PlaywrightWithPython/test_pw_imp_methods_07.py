"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_imp_methods_07.py -s -v --headed
GDrive Link: https://drive.google.com/file/d/1XHvFMWU0U-N6Dr1gKbOzrW4Ziz4aHvAd/view?usp=drive_link

inner_text() vs text_content()
all_inner_texts() vs all_text_contents()
all()
"""

import pytest
from playwright.sync_api import Page, expect


def test_comparisonofmethods(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator("h2.product-title")

    # inner_test() vs text_content()
    # print("Using Inner Text: ",product_names.nth(1).inner_text())       # returns actual text
    # print("Using text content: ",product_names.nth(1).text_content())   # returns content with special chars and spaces

    count = products.count()
    for i in range(count):
        print(products.nth(i).inner_text())  # Using inner_text()

    print("---------------------------------")
    for i in range(count):
        print(products.nth(i).text_content().strip())  # Using text_content()

    # all_inner_texts() vs all_text_contents()
    product_names = products.all_inner_texts()  # returns the list of actual text
    print(product_names)

    product_names = products.all_text_contents()    # returns the list of content with special chars and spaces
    print(product_names)
    product_names = [text.strip() for text in product_names]
    print(product_names)

    # all() Returns objects (ElementHandles)
    product_locators = products.all()

    for product_loc in product_locators:    # Without using range function
        print(product_loc.inner_text())

    print("----------------------------------")
    for i in range(len(product_locators)):  # using range function
        print(product_locators[i].inner_text())


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
Differences:
inner_text() vs text_content():
    inner_text()   # returns actual text
    text_content() # returns content with special chars and spaces
    
all_inner_texts() vs all_text_contents()
    all_inner_texts()   # returns the list of actual text
    all_text_contents() # returns the list of content with special chars and spaces

all()
    Returns objects (ElementHandles).
    You must extract text manually.
"""

"""
Assertions:
to_have_count(<provide count you are expecting>)
"""
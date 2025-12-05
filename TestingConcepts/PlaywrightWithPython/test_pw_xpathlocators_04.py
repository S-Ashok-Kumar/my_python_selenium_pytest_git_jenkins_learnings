"""
Command to Execute: python -m pytest PlaywrightWithPython/test_pw_xpathlocators_04.py -s -v --headed

X-path:
-------
Gdrive: https://drive.google.com/file/d/1ZXRQSWxcWlDTjWBHLEWA6a4juASkUs9C/view?usp=drive_link

text_content()  - Returns the text of single web element
all_text_contents() - Returns the list of group of web elements
"""
import pytest
from playwright.sync_api import Page, expect


def test_verify_xpathlocators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # 1. Absolute xpath (Full Xpath) - Starts from root node
    logo = page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    expect(logo).to_be_visible()

    # 2. Relative xpath: //tagname[@attribute='value'] - starts from anywhere in the DOM
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)

    # 3. xpath with: contains() - Used for handling dynamic elements
    products = page.locator("//h2/a[contains(@href,'computer')]")
    product_count = products.count()
    print("Products Count :", product_count)
    expect(products).to_have_count(product_count)

    print("First Computer Product: ", products.first.text_content())
    print("Last Computer Product: ", products.last.text_content())
    print("Nth Computer Product: ", products.nth(3).text_content())  # nth() takes index from 0

    product_titles = products.all_text_contents()
    print("Product Titles",product_titles)

    print("Printing product titles using looping statement.........")
    for item in product_titles:
        print(item)

    #4. xpath with: starts-with()
    building_products = page.locator("//h2/a[starts-with(@href,'/build')]")
    print("Count of building products:", building_products.count())
    expect(building_products).to_have_count(building_products.count())

    #5. xpath with: text()  - is representing inner text of the element
    registration_link = page.locator("//a[contains(text(),'Register')]")
    expect(registration_link).to_be_visible()

    #6. xpath with: last()
    googlepluslink = page.locator("//div[@class='column follow-us']/ul/li[last()]")
    expect(googlepluslink).to_have_text("Google+")

    #7. xpath with: position()
    twitterlink = page.locator("//div[@class='column follow-us']/ul/li[position()=2]")
    expect(twitterlink).to_have_text("Twitter")

"""
Methods:
count()
text_content()
first.text_content()
last.text_content()
nth(index).text_content()
all_text_content()
"""

"""
Assertions:
to_be_visible()
to_have_url()
to_have_title()
to_have_text()
to_have_count()
"""
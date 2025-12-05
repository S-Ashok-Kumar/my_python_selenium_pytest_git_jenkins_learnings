"""
Playwright built-in locators:
-----------------------------
Command to execute: python -m pytest PlaywrightWithPython/test_pw_locators_02.py -s -v --headed
Learn how to bypass "Verify you are human" error

page.getByRole()        to locate by explicit and implicit accessibility attributes.
                        Gdrive link: https://drive.google.com/file/d/1ehh4vfWVdzLAQR8fka-wL31QDVlQWdu6/view?usp=drive_link
page.getByText()        to locate by text content.
page.getByLabel()       to locate a form control by associated label's text.
page.getByPlaceholder() to locate an input by placeholder.
page.getByAltText()     to locate an element, usually image, by its text alternative.
page.getByTitle()       to locate an element by its title attribute.
page.getByTestId()      to locate an element based on its data-testid attribute (other attributes can be configured).
"""
import re
import time
from playwright.sync_api import Page, expect


def test_verify_pwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(5000) # Playwright in-built method 5000 ms = 5 sec

    # 1. getByAltText() - to locate an element, usually image, by its text alternative.
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # 2. getByText() to locate by text content.
    expect(page.get_by_text("Welcome to our store")).to_be_visible()    # Using Full text
    # expect(page.get_by_text("Welcome to")).to_be_visible()              # Using Partial text
    # expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() # Using regular expressions

    """
    # Getting "Verify you are human error". From here, Don't execute - Just observe code
    
    # 3. getByRole() to locate by explicit and implicit accessibility attributes.
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # 4. getByLabel() to locate a form control by associated label's text.
    page.get_by_label("First name:").fill("John")
    page.get_by_label("Last name:").fill("Kenedy")
    page.get_by_label("Email:").fill("John")
    time.sleep(5) # Python in-built method. Takes seconds

    # 5. getByPlaceholder() to locate an input by placeholder.
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    """

    # 6. getByTitle() to locate an element by its title attribute.
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    # 7. page.getByTestId() to locate an element based on its data-testid attribute (other attributes can be configured).
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    page.wait_for_timeout(5000)



"""
Assertions:
to_be_visible()
to_have_url()
to_have_title()
to_have_text()
"""
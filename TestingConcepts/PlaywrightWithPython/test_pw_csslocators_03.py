"""
CSS Selectors/Locators
----------------------
Command to execute: python -m pytest PlaywrightWithPython/test_pw_csslocators_03.py -s -v --headed

GDrive Link: https://drive.google.com/file/d/1LoJuWrIiSqkBP4yPAoD4iZKbmDgIPuvf/view?usp=drive_link

Mostly Used Locators: Relative CSS Locator
---------------------
tag id                  - tag#id
tag class               - tag.class
tag attributes          - tag[attribute='value']
tag class attribute     - tag.class[attribute='value']

Other type of Locators:
-----------------------
Combination of both Relative and Absolute CSS selectors:
html>body>div>div>div>main[role='main']>div.td-content>div.centered>p#para1

Navigate to child element: >
Navigate to element anywhere in DOM: space ( )
                                    <p> inside <body>           body p
                                    <p> anywhere in the HTML    html p
Starts with: ^
Ends With: $
Anywhere: *
finding with multiple attributes: p[id='para1'][class='main']
Find first child: body>div>*:first-child
Find last child: body>div>*:last-child
Find nth child: body > div > *:nth-child(3)
negation: p:not([id='para1'])
"""

import pytest
from playwright.sync_api import Page, expect


def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # tag id
    page.locator("input#small-searchterms").fill("T-Shirts")
    # page.locator("#small-searchterms").fill("T-Shirts")   # Also correct
    page.wait_for_timeout(5000)

    # tag class
    # page.locator("input.search-box-text").fill("-Shorts")
    page.locator(".search-box-text").fill("-Shorts")  # Also correct
    page.wait_for_timeout(5000)

    # tag attribute
    page.locator("input[name=q]").fill("-Shirts")
    # page.locator("[name=q]").fill("-Shirts") # Also correct
    page.wait_for_timeout(5000)

    # tag class attribute
    page.locator("input.search-box-text[value='Search store']").fill("-Inner Wears")
    # page.locator(".search-box-text[value='Search store']").fill("-Inner Wears")   # Also correct
    page.wait_for_timeout(5000)

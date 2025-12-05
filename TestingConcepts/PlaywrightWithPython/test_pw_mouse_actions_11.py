"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_mouse_actions_11.py -s -v --headed

Mouse Actions:

@pytest.mark.skip - is used. So, execute each function separately
"""

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    point_me_btn = page.locator(".dropbtn")
    point_me_btn.hover()

    # page.locator("div[class='dropdown-content']>a").nth(1)
    laptops = page.locator("div[class='dropdown-content']>a:nth-child(2)")
    laptops.hover()
    expect(laptops).to_have_text("Laptops")

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_right_click(page:Page):
    page.goto("https://vinothqaacademy.com/mouse-event/")

    right_click = page.locator("button#rightclick")
    right_click.click(button="right")       # performs right click action - right, left, middle
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_double_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    right_click = page.locator("button[ondblclick='myFunction1()']")
    right_click.dblclick()

    field2 = page.locator("#field2")
    expect(field2).to_have_value("Hello World!")
    page.wait_for_timeout(5000)

def test_mouse_drag_drop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    # #Approach 1
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #Approach 2 - using drag_to()
    source.drag_to(target)
    page.wait_for_timeout(5000)



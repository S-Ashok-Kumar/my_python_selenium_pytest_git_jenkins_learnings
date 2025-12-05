"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_sample_16.py -s -v --headed

To view allure reports (Generate the reports at run time):
                            allure serve PlaywrightWithPython\allurereports\allure-results

To generate the permanent allure report (We can watch any time we want):
    allure generate PlaywrightWithPython\allurereports\allure-results -o PlaywrightWithPython\allurereports\allure-report --clean

GDrive Link: https://drive.google.com/file/d/1rJXvcUTtw-oxWVHH4-rZS9ggcmrVjNbo/view?usp=drive_link
"""
import pytest
from playwright.sync_api import Page, expect

def test_url(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_url("https://demoblaze.com/index.html")


def test_Title(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_title("STORE")


def test_google_search(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")


def test_bing_search(page):
    page.goto("https://www.bing.com/")
    expect(page).to_have_title("Bing123")

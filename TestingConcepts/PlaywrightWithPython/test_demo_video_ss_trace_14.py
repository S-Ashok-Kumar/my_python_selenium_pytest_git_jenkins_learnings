"""
Command to execute:
                    python -m pytest PlaywrightWithPython/test_demo_video_ss_trace_14.py -s -v --headed --reruns 3 --reruns-delay 2

Command used to execute using pytest.ini:
                    python -m pytest PlaywrightWithPython/test_demo_video_ss_trace_14.py

GDrive link: https://drive.google.com/file/d/1jwlfWMSH8xD3LSJdncV6xi17u7Ypg5I4/view?usp=drive_link
"""

from playwright.sync_api import Page, expect

def test_url(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_url("https://demoblaze.com/index.html")

def test_Title(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_title("STORE")

def test_Login(page:Page):
    page.goto("https://demoblaze.com/index.html")
    page.wait_for_timeout(5000)
    page.locator('#login2').click()
    page.locator("#loginusername").fill('nani2024')
    page.locator("#loginpassword").fill('Nani@2024')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(10000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome nani2024")
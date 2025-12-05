"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_inner_frames_10.py -s -v --headed

frame: Created by developer
iframe: embedded into the other frames

3 ways to handle frames:
frame locator
frame URL
frame name
"""
from playwright.sync_api import Page, expect

def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    
    #frame 3
    frame3 = page.frame(url = "https://ui.vision/demo/webtest/frames/frame_3.html") # grab the frame 3
    frame3.locator("input[name='mytext3']").fill("Welcome")
    child_frame = frame3.child_frames
    # print("Child Frame",child_frame)
    print("Number of child frames inside the frame3: ",len(child_frame))

    innerframe = child_frame[0]
    # print("inner Frame", innerframe)
    radio_btn = innerframe.get_by_label("I am a human")
    radio_btn.check()
    expect(radio_btn).to_be_checked()

    checkbox = innerframe.locator("div[aria-label='Web Testing']")
    checkbox.click()
    expect(checkbox).to_have_attribute("aria-checked", "true")
    page.wait_for_timeout(5000)
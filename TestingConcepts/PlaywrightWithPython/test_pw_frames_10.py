"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_frames_10.py -s -v --headed

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

    frame = page.frames    # returns all the frames present in the website DOM
    print("Number of frames in a page: ", len(frame))

    #frame 1
    # frame1 = page.frame_locator("frame[src='frame_1.html']")     #get the frame using CSS locator  # option 1
    frame1 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_1.html')  #get the frame using URL   #option 2
    # frame1 = page.frame("<name of the frame>")  ##get the frame using name attribute   #option 3
    inputbox = frame1.locator("input[name='mytext1']")
    inputbox.fill("Playwright")
    expect(inputbox).to_have_value("Playwright")

    page.wait_for_timeout(5000)
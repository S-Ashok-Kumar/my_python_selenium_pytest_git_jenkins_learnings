"""
Command to execute: python -m pytest PlaywrightWithPython/test_playwright_async_01.py -s -v --headed
Pre-requisite for asynchronous execution:
install pytest-asyncio
command: pip install pytest-asyncio

Typescript/Javascript we use this approach.
Also in API Testing
"""
import pytest
from playwright.async_api import expect, async_playwright  # Page is class


@pytest.mark.asyncio
async def test_verifyPageUrl():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        mypage = await browser.new_page()
        await mypage.goto("http://www.automationpractice.pl/index.php")
        # myurl = mypage.url    # get the url
        # print("URL of the application: ", myurl)
        await expect(mypage).to_have_url("http://www.automationpractice.pl/index.php")  # Verifying - Assertion method expect()



"""
Output: before installing "pytest-asyncio"

===================================================================== FAILURES ===================================================================== 
________________________________________________________________ test_verifyPageUrl ________________________________________________________________ 
async def functions are not natively supported.
You need to install a suitable plugin for your async framework, for example:
  - anyio
  - pytest-asyncio
  - pytest-tornasync
  - pytest-trio
  - pytest-twisted
============================================================= short test summary info ============================================================== 
FAILED PlaywrightWithPython/test_playwright_async_01.py::test_verifyPageUrl - Failed: async def functions are not natively supported.
================================================================ 1 failed in 0.07
"""
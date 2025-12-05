"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_working_with_files_12.py -s -v --headed

File Uploading/Downloading:

@pytest.mark.skip - is used. So, execute each function separately.
"""

import pytest
import os
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_upload_single_files(page: Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Uploading single file
    path = "C:/Users/ashok/PycharmProjects/cloned_project/my_python_selenium_pytest_git_jenkins_learnings/TestingConcepts/PlaywrightWithPython/file_uploads_12/test1.txt"
    upfile = page.locator("#filesToUpload")
    page.wait_for_timeout(5000)
    upfile.set_input_files(path)
    # page.locator("button:has-text('Upload Single File')").click()

    # Validation
    # msg = page.locator("#singleFileStatus")
    msg = page.locator("#fileList")
    expect(msg).to_contain_text("test1.txt")
    print("------Single File Uploaded Successful--------")
    page.wait_for_timeout(5000)


# @pytest.mark.skip
def test_upload_multiple_files(page: Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Uploading multiple file
    path1 = "C:/Users/ashok/PycharmProjects/cloned_project/my_python_selenium_pytest_git_jenkins_learnings/TestingConcepts/PlaywrightWithPython/file_uploads_12/test1.txt"
    path2 = "C:/Users/ashok/PycharmProjects/cloned_project/my_python_selenium_pytest_git_jenkins_learnings/TestingConcepts/PlaywrightWithPython/file_uploads_12/test2.txt"
    upfile = page.locator("#filesToUpload")
    page.wait_for_timeout(5000)
    upfile.set_input_files([path1,path2])
    # page.locator("button:has-text('Upload Multiple Files')").click()

    # Validation
    # msg = page.locator("#multipleFilesStatus")
    msg1 = page.locator("#fileList li").nth(0)
    msg2 = page.locator("#fileList li").nth(1)
    expect(msg1).to_contain_text("test1.txt")
    expect(msg2).to_contain_text("test2.txt")
    print("------Multiple File Uploaded Successful--------")
    page.wait_for_timeout(5000)


@pytest.mark.skip
def test_download_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    # #register an event - download
    # def download_handling(download):
    #     download.save_as("downloads/testfile.txt")
    #
    # page.on("download", download_handling)

    page.on("download", lambda download: download.save_as("PlaywrightWithPython/downloads/testfile.txt"))
    page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(3000)

    if os.path.exists("PlaywrightWithPython/downloads/testfile.txt"):
        print("File Exist")
    else:
        print("File Not Exist")

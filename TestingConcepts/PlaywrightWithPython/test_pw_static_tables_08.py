"""
Command to execute: python -m pytest PlaywrightWithPython/test_pw_static_tables_08.py -s -v --headed

Static Web Tables:
<table>
<tbody> = Table body
<tr> = Table row
<th> = Table head
<td> = Table data
--------------------------------
:nth-child(n)
:nth-of-type(n)
:first-child
:last-child
:first-of-type
:last-of-type
"""
import pytest
from playwright.sync_api import Page, expect

def test_static_web_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    #1. Count total number of rows in a table
    rows = table.locator("tr")      #equals to  table[name='BookTable'] tbody>tr
    rows_count = rows.count()
    print("Number of rows: ", rows_count)
    expect(rows).to_have_count(rows_count)

    #2. Count total number of columns/header in a table
    columns = rows.locator("th")    #equals to table[name='BookTable'] tbody tr th
    columns_count = columns.count()
    print("Number of columns: ",columns_count)
    expect(columns).to_have_count(columns_count)

    #3. Read all the data from 2nd row of the table
    second_row_data = rows.nth(1).locator("td")     # table[name='BookTable'] tbody tr:nth-of-type(2) td
    sec_row_texts = second_row_data.all_inner_texts()
    print("Second row data: ",sec_row_texts)
    expect(second_row_data).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    print("------------Printing one by one from sec_row_texts---------------")
    for text in sec_row_texts:
        print(text)

    #4. Read all the data from the table excluding headers
    print("------------Printing all the data from the table excluding headers---------------")
    all_row_data = rows.all()
    for row in all_row_data[1:]:
        col = row.locator("td").all_inner_texts()
        print(col)


    #5. Print book names whose author is Mukesh
    print("------------Printing book names whose author is Mukesh---------------")
    for row in all_row_data[1:]:
        author_name = row.locator("td").nth(1).inner_text()
        if author_name == "Mukesh":
            book_name = row.locator("td").nth(0).inner_text()
            print(author_name, "-", book_name)

    #6. What is the total prices of all the books
    print("------------Printing total prices of all the books---------------")
    total_price = 0
    for row in all_row_data[1:]:
        price = row.locator("td").nth(3).inner_text()
        print(price)
        total_price += int(price)
    print("Total Price: ", total_price)

























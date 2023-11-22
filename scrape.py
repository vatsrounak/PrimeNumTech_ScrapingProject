from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

# Configure Chrome options to run headless (without a visible browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Initialize the WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Load the webpage using Selenium
driver.get(url)

# Wait for a few seconds to ensure JavaScript execution
driver.implicitly_wait(5)

# Get the HTML content after JavaScript execution
page_source = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table with the id "table_id"
postings_table = soup.find('table', {'id': 'table_id'})

if postings_table:
    print("Table found successfully!")

    # Extract information from the first 5 postings
    postings_data = []
    rows = postings_table.find_all('tr')[1:7]  # Skip the header row
    if rows:
        for row in rows:
            # Skip rows with input elements (search criteria)
            if row.find('input'):
                continue

            columns = row.find_all('td')

            # Check if the number of columns is as expected
            if len(columns) >= 6:
                post_date = columns[0].text.strip()
                quest_number = columns[1].text.strip()
                category_code = columns[2].text.strip()
                bid_request_name = columns[3].text.strip()
                bid_closing_date = columns[4].text.strip()

                # Store the extracted information in the provided variables
                Est = post_date  # Example, you can replace this with the actual information
                Value = quest_number
                Notes = category_code
                Description = bid_request_name
                Closing_Date = bid_closing_date

                # If you want to store them in a dictionary, you can do:
                posting_info = {
                    'Est': Est,
                    'Value': Value,
                    'Notes': Notes,
                    'Description': Description,
                    'Closing Date': Closing_Date,
                }

                postings_data.append(posting_info)
            else:
                # Print the HTML content of the problematic row
                print(f"Skipping row with unexpected number of columns: {len(columns)}")
                print(row)

        # Print the extracted information
        print("Extracted Information:")
        for info in postings_data:
            print(info)

    else:
        print("No rows found in the table.")

else:
    print("Couldn't find the table with id 'table_id'.")

# Close the WebDriver
driver.quit()

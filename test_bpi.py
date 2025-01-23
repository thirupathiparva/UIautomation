import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_bpi_response():
    # Setup WebDriver (ensure you have the appropriate driver installed)
    driver = webdriver.Chrome("C:/Users/prava/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")  # You can use Firefox, Edge, etc.

    try:
        # Load the page that contains the API response (substitute with your actual page URL)
        driver.get('api.coindesk.com/v1/bpi/currentprice.json')  # Example URL

        # Pause to allow page load
        time.sleep(2)

        # Retrieve JSON data from the page, assume it's in a <pre> tag or similar element
        # You can adjust this selector based on the actual layout of your webpage
        json_data = driver.find_element(By.TAG_NAME, "pre").text

        # Parse the JSON data
        import json
        data = json.loads(json_data)

        # Verify the presence of BPIs
        bpi = data.get("bpi", {})
        assert len(bpi) == 3, "There should be 3 BPIs"

        # Verify each BPI
        assert "USD" in bpi, "USD BPI is missing"
        assert "GBP" in bpi, "GBP BPI is missing"
        assert "EUR" in bpi, "EUR BPI is missing"

        # Verify GBP description is correct
        gbp_description = bpi["GBP"].get("description", "")
        assert gbp_description == "British Pound Sterling", f"Expected 'British Pound Sterling', but got {gbp_description}"

    finally:
        # Cleanup: close the WebDriver
        driver.quit()


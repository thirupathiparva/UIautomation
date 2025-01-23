from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pytest

# Declare driver as a global variable (driver will be passed by the fixture)
driver = None

class TestUIebay:
    @pytest.fixture()
    def setup(self):
        global driver
        # Set up Chrome options (optional, but useful for headless mode or custom settings)
        options = Options()
        # options.add_argument('--headless')  # Uncomment to run Chrome in headless mode

        # Create a Service object for the ChromeDriver
        service = Service("C:/Users/prava/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")  # Make sure to update the path to your chromedriver

        # Initialize the driver with the service object and options (if needed)
        driver = webdriver.Chrome(service=service, options=options)

        # Wait for elements to appear (implicitly wait)
        driver.implicitly_wait(10)

        # Maximize the window
        driver.maximize_window()

        yield driver  # Yield driver to the test functions

        # Teardown
        driver.quit()
        print("Test completed")

    def test_add_to_cart(self, setup):
        driver = setup
        # Step 1: Navigate to eBay
        driver.get("https://www.ebay.com/")
        time.sleep(2)

        # Step 2: Search for 'book'
        search_box = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')
        search_box.send_keys("book")  # Type 'book' into the search box
        search_box.submit()
        time.sleep(2)

        # Step 3: Click on the first book in the list
        first_book = driver.find_element(By.XPATH, '(//*[@class="s-item__link"])[1]')
        first_book.click()
        time.sleep(2)

        # Step 4: Click on 'Add to cart' button
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="atcBtn_btn_1"]/span/span')
        add_to_cart_button.click()
        time.sleep(2)

        # Step 5: Verify the cart has been updated and displays the number of items in the cart
        cart_icon = driver.find_element(By.XPATH, '//*[@id="gh-cart-i"]')
        cart_count = cart_icon.text

        # Verify that the cart has updated. It should show a number (e.g., "2 item" or similar).
        assert cart_count.isdigit(), f"Test failed: Expected the cart count to be a number, but got '{cart_count}'"
        print(f"Test Passed: Cart count is '{cart_count}'")


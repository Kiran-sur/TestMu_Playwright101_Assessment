import re
from playwright.sync_api import sync_playwright, expect

def run():
    # Start Playwright and launch a browser instance
    with sync_playwright() as p:
        # headless=False allows you to see the browser in action
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Open TestMu AI’s Selenium Playground
        page.goto("https://www.testmuai.com/selenium-playground/")

        # 2. Click “Simple Form Demo”
        page.get_by_role("link", name="Simple Form Demo").click()

        # 3. Validate that the URL contains “simple-form-demo”
        # Web-first assertion: automatically waits for the condition to be met
        expect(page).to_have_url(re.compile(".*simple-form-demo.*"))

        # 4. Create a variable for a string value
        welcome_text = "Welcome to TestMu AI"

        # 5. Use this variable to enter values in the “Enter Message” text box
        # Using the unique ID selector for the input field
        page.locator("#user-message").fill(welcome_text)

        # 6. Click “Get Checked Value”
        page.get_by_role("button", name="Get Checked Value").click()

        # 7. Validate whether the same text message is displayed in the right-hand panel
        # The output container has the ID 'message'
        expect(page.locator("#message")).to_have_text(welcome_text)

        # Clean up
        browser.close()

if __name__ == "__main__":
    run()
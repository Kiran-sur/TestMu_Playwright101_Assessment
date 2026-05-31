from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

       
        page.goto("https://www.testmuai.com/selenium-playground/")
        page.get_by_role("link", name="Input Form Submit").click()

        
        submit_button = page.get_by_role("button", name="Submit")
        submit_button.click()

        name_input = page.locator("#name")
        validation_msg = name_input.evaluate("el => el.validationMessage")
        assert validation_msg != "", "Error message should be triggered"

        name_input.fill("John Doe")
        page.locator("#inputEmail4").fill("kiransuryawanshi43@gmail.com")
        page.locator("#inputPassword4").fill("SecurePass123!")
        page.locator("#company").fill("TestMu AI Engineering")
        page.locator("#websitename").fill("https://www.testmuai.com")

      
        page.locator("select[name='country']").select_option(label="United States")

     
        page.locator("#inputCity").fill("San Francisco")
        page.locator("#inputAddress1").fill("Market Street 101")
        page.locator("#inputAddress2").fill("Level 42")
        page.locator("#inputState").fill("California")
        page.locator("#inputZip").fill("94103")
        
        submit_button.click()

    
        success_text = "Thanks for contacting us, we will get back to you shortly."
        expect(page.locator(".success-msg")).to_have_text(success_text)

        browser.close()

if __name__ == "__main__":
    run()
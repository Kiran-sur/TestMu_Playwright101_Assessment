from playwright.sync_api import sync_playwright, expect

def run():
    # Start Playwright and launch a browser instance
    with sync_playwright() as p:
        # Using headless=False so you can observe the drag-and-drop interaction
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Open the Selenium Playground page and click “Drag & Drop Sliders”
        page.goto("https://www.testmuai.com/selenium-playground/")
        page.get_by_role("link", name="Drag & Drop Sliders").click()

        # 2. Select the slider with default value 15 (found in #slider1)
        slider = page.locator("#slider3 input")
        output = page.locator("(//div[contains(@class, 'sp__range')])[3]//output")
       
        # Ensure the slider is visible and in the viewport before calculating coordinates
        slider.scroll_into_view_if_needed()
        
        # Get the bounding box of the slider to calculate drag coordinates
        box = slider.bounding_box()
        if box:
            # Start position: roughly 15% into the slider width
            start_x = box["x"] + (box["width"] * 0.15)
            # Target position: roughly 95% into the slider width (0.945 is a precise offset for 95)
            target_x = box["x"] + (box["width"] * 0.952)
            center_y = box["y"] + (box["height"] / 2)

            # Perform the drag action using mouse simulation
            page.mouse.move(start_x, center_y)
            page.mouse.down()
            # Increasing steps to 30 ensures the browser's JS registers the 'slide' event
            page.mouse.move(target_x, center_y, steps=30)
            page.mouse.up()

        # 3. Validate whether the range value shows 95
        # Using expect ensures Playwright waits for the text to update correctly
        expect(output).to_have_text("95")
        
        browser.close()

if __name__ == "__main__":
    run()

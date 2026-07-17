from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.wait_for_timeout(2000)

    # ASSERTION - check karna ki "Products" text page pe hai ya nahi
    title = page.text_content(".title")
    print("Page pe ye title dikh raha hai:", title)

    assert title == "Products", "Login fail ho gaya bhai!"
    print("✅ TEST PASSED - Login successful hai")

    browser.close()
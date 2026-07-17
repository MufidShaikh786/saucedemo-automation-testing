def test_checkout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1000)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.wait_for_timeout(500)

    page.click(".shopping_cart_link")
    page.wait_for_timeout(1000)

    page.click("#checkout")
    page.wait_for_timeout(1000)

    page.fill("#first-name", "Mufid")
    page.fill("#last-name", "Shaikh")
    page.fill("#postal-code", "416606")
    page.click("#continue")
    page.wait_for_timeout(1000)

    page.click("#finish")
    page.wait_for_timeout(1000)

    confirmation = page.text_content(".complete-header")
    assert confirmation == "Thank you for your order!"
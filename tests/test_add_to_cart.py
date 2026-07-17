def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1500)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.wait_for_timeout(1000)

    cart_count = page.text_content(".shopping_cart_badge")
    assert cart_count == "1"
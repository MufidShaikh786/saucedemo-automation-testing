def test_remove_from_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1000)

    page.click("#add-to-cart-sauce-labs-backpack")
    page.wait_for_timeout(500)

    # Ab remove kar
    page.click("#remove-sauce-labs-backpack")
    page.wait_for_timeout(500)

    # Cart badge gayab hona chahiye (0 items)
    cart_badge = page.query_selector(".shopping_cart_badge")
    assert cart_badge is None
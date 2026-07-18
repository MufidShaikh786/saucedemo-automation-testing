def test_sort_by_price_low_to_high(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1500)

    # Dropdown se "Price low to high" select kar
    page.select_option(".product_sort_container", "lohi")
    page.wait_for_timeout(1000)

    # Pehla product ka price nikal, check kar sabse chota hai
    first_price = page.text_content(".inventory_item_price")
    print("Sorted first price:", first_price)
    assert first_price == "$7.99"  # saucedemo pe ye sabse sasta item hai
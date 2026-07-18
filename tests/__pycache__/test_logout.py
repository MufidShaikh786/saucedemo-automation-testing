def test_logout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1500)

    # Menu (hamburger icon) khol
    page.click("#react-burger-menu-btn")
    page.wait_for_timeout(500)

    # Logout pe click kar
    page.click("#logout_sidebar_link")
    page.wait_for_timeout(1000)

    # Check kar wapas login page pe aa gaya
    login_button = page.text_content("#login-button")
    assert login_button == "Login"
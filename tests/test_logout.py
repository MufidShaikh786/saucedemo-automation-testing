def test_logout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_timeout(1500)

    page.click("#react-burger-menu-btn")
    page.wait_for_timeout(500)

    page.click("#logout_sidebar_link")
    page.wait_for_timeout(1000)

    login_button = page.get_attribute("#login-button", "value")
    assert login_button == "Login"
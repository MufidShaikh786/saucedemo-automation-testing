def test_invalid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    page.wait_for_timeout(2000)

    error_message = page.text_content("[data-test='error']")
    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert error_message == expected_error
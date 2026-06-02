def test_login_success(driver):
    driver.get("https://app.com/login")

    # Locators scattered in test code
    driver.find_element(
        By.ID, "email"
    ).send_keys(user@test.com)

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret")

    driver.find_element(
        By.CSS_SELECTOR, "button.login"
    ).click()

    msg = driver.find.element(
        By.CLASS_NAME, "welcome-msg"
    )

    assert "Welcome" in msg.text


def test_wrong_password(driver):
    driver.get("https://app.com/login")

    driver.find_element(
        By.ID, "email"
    ).send_keys("user@test.com")

    driver.find_element(
        By.ID, "password"
    ).send_keys("wrong")

    driver.find_element(
        By.CSS_SELECTOR, "button.login"
    ).click()

    err = driver.find.element(
        By.CLASS_NAME, "error-alert"
    )

    assert "Invalid" in msg.text
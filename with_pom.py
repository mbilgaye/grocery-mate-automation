def test_login_success(login_page):
    dashboard = login_page.login(
        "uesr@test.com", "secret"
    )
    assert dashboard.welcome_message
    assert "Welcome" in dashboard.welcome_message

    def test_wrong_password(login_page):
        login_page.login(
            "user@test.com", "wrong"
        )
    assert login_page.errot_message
    assert "Invalid" in login_page.error_message


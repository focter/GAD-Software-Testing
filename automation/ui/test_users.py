import re

from playwright.sync_api import Page, expect


def test_users_page_requires_authentication(page: Page):
    page.goto("http://localhost:3000/users.html")

    expect(page).to_have_url(
        "http://localhost:3000/users.html"
    )

    auth_message = page.get_by_role(
        "cell",
        name=re.compile("You are not authenticated")
    )

    expect(auth_message).to_be_visible()

    login_link = page.get_by_role("link", name="login")
    expect(login_link).to_be_visible()
    expect(login_link).to_have_attribute(
        "href",
        "/login?redirectURL=/users.html"
    )

    register_link = page.get_by_role("link", name="register")
    expect(register_link).to_be_visible()
    expect(register_link).to_have_attribute(
        "href",
        "/register.html?redirectURL=/users.html"
    )


def test_users_list_after_login(page: Page):
    # 1. 未登录访问 Users
    page.goto("http://localhost:3000/users.html")

    # 2. 点击登录
    page.get_by_role("link", name="login").click()

    # 3. 验证进入登录页
    expect(page).to_have_url(
        re.compile(r".*/login/?\?redirectURL=/users\.html")
    )

    # 4. 输入账号密码
    page.get_by_placeholder("Enter User Email").fill(
        "John.Okuplok@test.test"
    )

    page.get_by_placeholder("Enter Password").fill(
        "1234"
    )

    # 5. 登录
    page.get_by_role("button", name="LogIn").click()

    # 6. 登录成功后应回到 Users
    expect(page).to_have_url(
        "http://localhost:3000/users.html"
    )

    # 7. 等待用户列表加载
    user_cards = page.locator(".item-card")
    expect(user_cards.first).to_be_visible()

    user_count = user_cards.count()

    assert user_count > 0

    # 8. 逐个检查每个用户
    for i in range(user_count):
        card = user_cards.nth(i)

        values = card.locator("span")

        # id / firstname / lastname / email
        assert values.count() == 4

        for j in range(4):
            assert values.nth(j).inner_text().strip() != ""

        # avatar
        avatar = card.locator("img")

        expect(avatar).to_be_visible()

        avatar_src = avatar.get_attribute("src")

        assert avatar_src is not None
        assert avatar_src.strip() != ""

        image_loaded = avatar.evaluate(
            "(img) => img.complete && img.naturalWidth > 0"
        )

        assert image_loaded

        # 用户详情链接
        user_link = card.locator(
            'a[href^="user.html?id="]'
        )

        expect(user_link).to_be_visible()
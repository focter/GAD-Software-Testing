from playwright.sync_api import Page


def test_open_browser(page: Page):
    page.goto("http://localhost:3000")
    print(page.title())
import re

import pytest
from playwright.sync_api import Page, expect


# UI-001
def test_articles_page_loads(page: Page):
    page.goto("http://localhost:3000/articles.html")

    expect(page).to_have_title(re.compile("GAD"))
    expect(page.get_by_text("Page: 1/10")).to_be_visible()

    article_links = page.locator(
        'strong a[href^="article.html?id="]'
    )

    expect(article_links).to_have_count(6)


# UI-002
def test_articles_next_page(page: Page):
    page.goto("http://localhost:3000/articles.html")

    expect(page.get_by_text("Page: 1/10")).to_be_visible()

    article_links = page.locator(
        'strong a[href^="article.html?id="]'
    )

    # 第一页
    expect(article_links).to_have_count(6)

    page_1_ids = [
        article_links.nth(i).get_attribute("href")
        for i in range(article_links.count())
    ]

    # Next
    page.get_by_role("link", name="Next").click()

    expect(page.get_by_text("Page: 2/10")).to_be_visible()
    expect(article_links).to_have_count(6)

    page_2_ids = [
        article_links.nth(i).get_attribute("href")
        for i in range(article_links.count())
    ]

    # 第一页和第二页不能出现相同文章
    assert set(page_1_ids).isdisjoint(page_2_ids)


# UI-006
@pytest.mark.xfail(
    reason="Known bug: Items/Page resets to 6 after page refresh",
    strict=True,
)
def test_items_per_page_persists_after_refresh(page: Page):
    page.goto("http://localhost:3000/articles.html")

    items_per_page = page.get_by_test_id("per-page-select")

    expect(items_per_page).to_have_value("6")

    article_links = page.locator(
        'strong a[href^="article.html?id="]'
    )

    expect(article_links).to_have_count(6)

    # 修改为 9
    items_per_page.select_option("9")

    expect(items_per_page).to_have_value("9")
    expect(article_links).to_have_count(9)

    # 刷新
    page.reload()

    # 正确需求：刷新后仍保持 9
    expect(items_per_page).to_have_value("9")
    expect(article_links).to_have_count(9)


# UI-007
def test_articles_next_previous(page: Page):
    page.goto("http://localhost:3000/articles.html")

    article_links = page.locator(
        'strong a[href^="article.html?id="]'
    )

    # Page 1
    expect(page.get_by_text("Page: 1/10")).to_be_visible()
    expect(article_links).to_have_count(6)

    page_1_ids = [
        article_links.nth(i).get_attribute("href")
        for i in range(article_links.count())
    ]

    # Page 1 → Page 2
    page.get_by_role("link", name="Next").click()

    expect(page.get_by_text("Page: 2/10")).to_be_visible()
    expect(article_links).to_have_count(6)

    page_2_ids = [
        article_links.nth(i).get_attribute("href")
        for i in range(article_links.count())
    ]

    assert set(page_1_ids).isdisjoint(page_2_ids)

    # Page 2 → Page 1
    page.get_by_role("link", name="Prev").click()

    expect(page.get_by_text("Page: 1/10")).to_be_visible()
    expect(article_links).to_have_count(6)

    page_1_returned_ids = [
        article_links.nth(i).get_attribute("href")
        for i in range(article_links.count())
    ]

    assert page_1_returned_ids == page_1_ids
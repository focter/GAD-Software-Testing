import re

from playwright.sync_api import Page, expect


def test_article_detail_matches_list(page: Page):
    page.goto("http://localhost:3000/articles.html")

    article_links = page.locator(
        'strong a[href^="article.html?id="]'
    )

    expect(article_links).to_have_count(6)

    first_article = article_links.first

    # 记录列表页文章信息
    list_title = first_article.inner_text()
    article_href = first_article.get_attribute("href")

    assert article_href is not None

    # 获取第一篇文章对应的作者
    list_author_link = page.locator(
        'a[href^="user.html?id="]'
    ).first

    expect(list_author_link).to_be_visible()

    list_author_name = list_author_link.inner_text()
    list_author_href = list_author_link.get_attribute("href")

    assert list_author_href is not None

    # 点击第一篇文章
    first_article.click()

    # 1. 验证文章 ID / URL
    expect(page).to_have_url(
        re.compile(rf".*{re.escape(article_href)}$")
    )

    # 2. 验证文章标题
    expect(
        page.get_by_text(list_title, exact=True)
    ).to_be_visible()

    # 3. 验证作者
    detail_author_link = page.locator(
        f'a[href="{list_author_href}"]'
    )

    expect(detail_author_link).to_be_visible()

    # 作者链接对应同一用户，并且显示文本包含列表页作者名
    expect(detail_author_link.first).to_contain_text(list_author_name)
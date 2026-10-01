# GAD Software Testing Project

基于 GAD（GUI/API Demo）的软件测试实践项目。

本项目用于完整实践软件测试流程，并逐步建立 API 自动化、UI 自动化和 CI 回归能力。

## Project Scope

当前自动化测试主要覆盖：

- Authentication
- Courses
- Course Progress
- Articles
- Article Detail
- Users
- Pagination
- Authorization
- UI state persistence

## Tech Stack

### API Automation

- Python
- pytest
- requests
- pytest-html
- pytest-metadata

### UI Automation

- Python
- pytest
- Playwright

### CI

- GitHub Actions
- Chromium
- Node.js
- GAD local test environment

---

## Project Structure

```text
GAD-Software-Testing/
├─ .github/
│  └─ workflows/
│     └─ ui-tests.yml
│
├─ automation/
│  ├─ api/
│  │  ├─ data/
│  │  ├─ tests/
│  │  │  ├─ test_auth_status.py
│  │  │  ├─ test_course_progress.py
│  │  │  ├─ test_courses.py
│  │  │  └─ test_login.py
│  │  ├─ config.py
│  │  ├─ pytest.ini
│  │  └─ requirements.txt
│  │
│  └─ ui/
│     ├─ test_article_detail.py
│     ├─ test_articles.py
│     ├─ test_users.py
│     └─ browser_check.py
│
├─ requirements-ui.txt
├─ .gitignore
└─ README.md
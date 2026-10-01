# GAD Software Testing Project

基于 GAD（GUI/API Demo）的软件测试实践项目。

本项目用于实践完整的软件测试流程，包括手工功能测试、缺陷记录、API 自动化、UI 自动化以及 GitHub Actions 持续集成。

---

## Project Overview

项目测试对象为 GAD。

测试过程中先通过手工测试理解系统功能、设计测试场景并发现问题，在此基础上选择稳定、重复、高价值的测试场景转化为自动化回归测试。

当前项目已经包含：

- 手工功能测试
- Bug Report
- API 自动化测试
- UI 自动化测试
- 已知缺陷自动化管理
- GitHub Actions CI

---

## Test Scope

当前主要测试范围包括：

### Articles

- 文章列表展示
- Article Detail 跳转
- 列表与详情数据一致性
- Next / Prev 分页
- Items/Page
- Sort
- 页面刷新后的状态保持

### Users

- 未登录访问控制
- 登录流程
- 用户列表展示
- 用户字段完整性
- 用户头像加载

### API

- Authentication
- Authentication Status
- Courses
- Course Detail
- Course Progress
- Authorization

---

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
├── .github/
│   └── workflows/
│       └── ui-tests.yml
│
├── automation/
│   ├── api/
│   │   ├── data/
│   │   │   └── course_progress_auth.json
│   │   ├── tests/
│   │   │   ├── conftest.py
│   │   │   ├── test_auth_status.py
│   │   │   ├── test_course_progress.py
│   │   │   ├── test_courses.py
│   │   │   └── test_login.py
│   │   ├── config.py
│   │   ├── pytest.ini
│   │   └── requirements.txt
│   │
│   └── ui/
│       ├── browser_check.py
│       ├── test_article_detail.py
│       ├── test_articles.py
│       └── test_users.py
│
├── docs/
│   └── manual-testing/
│       ├── test-cases.md
│       ├── bug-reports.md
│       └── test-summary.md
│
├── .gitignore
├── requirements-ui.txt
└── README.md
```

---

## Manual Testing

手工测试阶段主要覆盖 Articles 和 Users 模块。

已经整理的测试文档：

- [Manual Test Cases](docs/manual-testing/test-cases.md)
- [Bug Reports](docs/manual-testing/bug-reports.md)
- [Test Summary](docs/manual-testing/test-summary.md)

这些文档记录了从手工功能测试、问题发现、Bug 记录到自动化回归的过程。

### Manual Test Results

当前整理的主要手工测试场景：

| Result | Count |
|---|---:|
| PASS | 5 |
| FAIL | 3 |
| OBSERVATION | 1 |
| Total | 9 |

已确认的问题主要集中在 Articles 页面刷新后的状态保持。

---

## Confirmed Bugs

当前记录了 3 个可以稳定复现的问题：

| Bug ID | Description | Status |
|---|---|---|
| BUG-001 | Articles 刷新后当前分页恢复到第 1 页 | Open |
| BUG-002 | Articles 刷新后 Items/Page 恢复默认值 6 | Open |
| BUG-003 | Articles 刷新后 Sort 恢复默认排序 | Open |

三个问题都表现为：

> 用户在 Articles 页面进行的部分操作状态，在浏览器刷新后没有被恢复。

当前根据黑盒测试结果分别记录，暂不直接判断三个问题是否由同一个底层实现缺陷导致。

---

## API Automation

API 自动化使用：

```text
Python + pytest + requests
```

当前主要覆盖：

### Authentication

- 正常登录
- 错误密码
- 不存在用户
- 用户名为空
- 密码为空
- 缺少用户名
- 缺少密码
- 请求体字段缺失

### Authentication Status

- 未认证状态
- 有效认证状态

### Courses

- 获取课程列表
- 获取课程详情
- 不存在的 Course ID
- Course ID 为 0
- Course ID 为负数
- Course ID 为非数字

### Course Progress

- 缺少 Authorization
- 不完整 Bearer
- 错误认证 Scheme
- 无效 Token
- 有效认证后的 Course Progress 查询

当前 API 自动化共包含：

```text
21 pytest test instances
```

---

## Run API Tests

首先启动 GAD，并确认：

```text
http://localhost:3000
```

可以正常访问。

进入 API 自动化目录：

```bash
cd automation/api
```

安装依赖：

```bash
pip install -r requirements.txt
```

执行全部 API 测试：

```bash
pytest
```

也可以根据 pytest marker 执行指定测试类型。

例如 Smoke：

```bash
pytest -m smoke
```

Regression：

```bash
pytest -m regression
```

Authentication：

```bash
pytest -m auth
```

---

## UI Automation

UI 自动化使用：

```text
Python + pytest + Playwright
```

自动化场景并不是简单复制所有手工测试，而是优先选择：

- 行为稳定
- 可以重复执行
- 结果可以由程序明确判断
- 适合长期回归
- 业务价值较高

的场景。

### Current UI Regression Set

| ID | Test Scenario | Current Status |
|---|---|---|
| UI-001 | Articles 列表页加载 | PASS |
| UI-002 | Articles Next 分页 | PASS |
| UI-003 | Article Detail 数据一致性 | PASS |
| UI-004 | Users 未登录权限拦截 | PASS |
| UI-005 | 登录后 Users 字段和头像完整性 | PASS |
| UI-006 | Items/Page 刷新状态保持 | XFAIL |
| UI-007 | Articles Next → Prev 分页往返 | PASS |

当前本地回归基线：

```text
6 passed, 1 xfailed
```

---

## Known Issue Management

UI-006 对应已经确认的 Items/Page 刷新状态问题。

测试中使用：

```python
@pytest.mark.xfail(
    reason="Known bug: Items/Page resets to 6 after page refresh",
    strict=True,
)
```

这样处理的目的不是把 Bug 当作 PASS，而是明确表示：

```text
当前产品行为已知不符合预期
```

当缺陷仍然存在时：

```text
XFAIL
```

如果以后产品行为发生变化，该测试结果也会变化，从而提示重新确认缺陷状态。

---

## Run UI Tests

安装 UI 自动化依赖：

```bash
pip install -r requirements-ui.txt
```

安装 Playwright Chromium：

```bash
playwright install chromium
```

执行 UI 回归：

```bash
pytest automation/ui --browser chromium
```

如果本地已经安装 Chrome，也可以运行：

```bash
pytest automation/ui --browser-channel chrome --headed
```

其中：

```text
--headed
```

用于显示浏览器执行过程。

---

## Continuous Integration

项目已经接入 GitHub Actions。

Workflow：

```text
.github/workflows/ui-tests.yml
```

当代码 Push 到：

```text
main
```

或向 `main` 创建 Pull Request 时，CI 会自动执行 UI 回归测试。

### CI Process

GitHub Actions 自动执行：

1. Checkout 当前测试项目
2. 安装 Python
3. 安装 Python 测试依赖
4. 安装 Playwright Chromium
5. 安装 Node.js
6. Clone GAD
7. 安装 GAD dependencies
8. 启动 GAD
9. 等待 GAD 测试环境可访问
10. 执行 Playwright UI 自动化回归

因此 CI 不依赖开发者本地已经启动 GAD。

第一次 GitHub Actions UI CI 已成功执行。

---

## Testing Principles

本项目在测试过程中主要采用以下原则：

### 1. 测试正确的对象

测试脚本执行为绿色并不一定代表测试有效。

例如页面中存在相同文本时，需要确认 Locator 找到的是实际目标元素，而不是其他页面元素。

### 2. 验证业务结果

自动化测试不仅检查：

```text
页面没有报错
```

还应检查：

```text
实际结果是否符合预期结果
```

例如分页测试同时验证：

- 页码变化
- 数据发生变化
- 返回上一页后数据恢复

### 3. 使用稳定 Locator

优先使用：

- Role
- Label
- Test ID
- 稳定属性

尽量避免依赖容易变化的页面结构。

### 4. 利用 Playwright Auto-waiting

对于动态页面，不使用固定时间的 `sleep` 作为主要同步方式。

优先使用：

```python
expect(...)
```

等待实际条件成立。

### 5. 区分缺陷与测试脚本失败

测试失败可能来源于：

- 产品真实缺陷
- 测试环境问题
- Locator 错误
- 测试数据问题
- 测试脚本本身的问题

需要进一步分析后才能判定。

### 6. 不强行自动化所有场景

对于主观视觉效果、探索性问题等场景，手工测试可能比自动化更合理。

### 7. 缺少需求依据时不直接判 Bug

例如测试过程中发现不同 Articles 使用相同图片。

由于目前没有明确需求证明：

```text
每篇文章必须使用不同图片
```

因此该现象记录为：

```text
OBSERVATION
```

而不是直接判定为 FAIL。

---

## Current Progress

目前已经完成：

- 手工测试场景设计与执行
- Articles / Users 功能测试
- Bug 记录
- 回归测试
- API 自动化
- pytest 测试数据参数化
- pytest fixture
- pytest marker
- API HTML Report
- Playwright UI 自动化
- Known Bug XFAIL 管理
- Git 仓库管理
- GitHub 远程仓库
- GitHub Actions UI CI
- 手工测试文档整理

后续计划：

- 优化项目目录结构
- 完善 GitHub 项目展示
- 增加 API CI
- 整理最终测试总结
- 对手工测试与自动化测试范围进行复盘

---

## Repository

GitHub Repository:

```text
focter/GAD-Software-Testing
```
# GAD Test Plan

## 1. Purpose

本文档用于定义 GAD 软件测试实践项目的测试目标、范围、方法、环境、风险以及测试进入和退出准则。

本项目的主要目标不是穷举 GAD 的全部功能，而是完成一个从：

需求分析 → 测试设计 → 手工执行 → 缺陷记录 → 回归测试 → API 自动化 → UI 自动化 → CI

的完整软件测试流程。

---

## 2. Test Objectives

本轮测试主要目标：

1. 验证 Articles 和 Users 等核心 Web 功能能否正常工作
2. 验证分页、详情跳转、认证和列表展示等主要用户流程
3. 验证 Learning API 的正常、异常和鉴权行为
4. 识别可稳定复现的软件问题
5. 对已发现问题设计回归测试
6. 将适合长期回归的 API 和 UI 场景自动化
7. 通过 GitHub Actions 自动执行回归测试
8. 形成可以追踪需求、用例、Bug 和自动化测试的项目文档

---

## 3. Test Scope

### 3.1 In Scope

#### Articles

测试内容包括：

- Articles 列表展示
- Article Detail 跳转
- 列表和详情主要数据一致性
- Next 分页
- Prev 分页
- 分页往返
- Items/Page
- Sort
- 页面刷新后的状态保持
- Article 图片重复现象观察

#### Users

测试内容包括：

- 未认证访问控制
- Login 跳转
- 登录后访问 Users
- 用户列表展示
- 用户基础字段
- Avatar 加载
- User Detail Link

#### API

测试内容包括：

- Login
- Authentication Status
- Courses List
- Course Detail
- Invalid Course ID
- Course Progress
- Authorization Header
- Invalid Token
- Missing / Empty Login Fields

#### Automation

包括：

- pytest API Automation
- Playwright UI Automation
- GitHub Actions API CI
- GitHub Actions UI CI

---

## 4. Out of Scope

当前项目不进行系统性的：

- 性能测试
- 压力测试
- 安全渗透测试
- 数据库专项测试
- 移动端专项测试
- 全浏览器兼容性测试
- 无障碍专项测试
- 长时间稳定性测试
- 弱网和网络中断专项测试
- GAD 全部功能模块的完整覆盖

未纳入范围的内容不能视为已经测试通过。

---

## 5. Test Approach

### 5.1 Black-box Testing

项目主要采用黑盒方式进行测试。

第一阶段主要依据：

- 页面可见功能
- 用户可执行操作
- API 请求和响应
- 系统实际行为

设计测试场景。

---

### 5.2 Functional Testing

重点验证：

- 页面能否正确加载
- 操作能否成功完成
- 数据是否符合预期
- 页面之间的数据是否一致
- API 是否返回正确状态码和数据

---

### 5.3 Negative Testing

针对 API 等功能设计异常场景，例如：

- 错误密码
- 不存在用户
- 空字段
- 缺少字段
- 非法 Course ID
- 无效 Token
- 错误 Authorization Scheme

---

### 5.4 Regression Testing

对于已经验证通过的核心功能以及已经发现的问题进行回归。

当前回归重点包括：

- Articles Pagination
- Article Detail
- Users Authentication
- Users List
- Items/Page 状态保持
- API Authentication
- Courses API
- Course Progress Authorization

---

### 5.5 Exploratory Testing

对于：

- 需求不明确
- 视觉表现
- 未预先设计的异常行为

采用探索性测试。

例如：

不同 Articles 使用相同图片的问题，由于缺少明确需求依据，目前仅记录为 Observation。

---

## 6. Automation Strategy

自动化主要选择满足以下条件的场景：

- 行为稳定
- 需要重复执行
- 结果可被程序明确判断
- 长期回归价值较高
- 自动化维护成本合理

不强行自动化：

- 主观视觉判断
- 一次性探索
- 需求尚未明确的行为
- 自动判断成本明显高于人工检查的场景

---

## 7. Test Environment

### Local Environment

Operating System:

`Windows 11`

Application:

`GAD`

Base URL:

`http://localhost:3000`

API Base URL:

`http://localhost:3000/api`

Browser:

`Google Chrome`

Python:

`Python 3.12`

Main Tools:

- pytest
- requests
- Playwright
- Git
- GitHub
- GitHub Actions

---

### CI Environment

CI Platform:

`GitHub Actions`

Runner:

`ubuntu-latest`

CI 中会自动：

1. Checkout 测试项目
2. 安装 Python
3. 安装测试依赖
4. 安装 Node.js
5. Clone GAD
6. 安装 GAD dependencies
7. 启动 GAD
8. 等待测试环境可访问
9. 执行 API 或 UI 自动化测试

UI CI 额外安装：

`Playwright Chromium`

---

## 8. Test Data

当前测试数据主要包括：

- GAD 内置测试用户
- GAD 内置 Articles
- GAD 内置 Users
- GAD Learning API Courses
- 参数化异常登录数据
- 参数化无效 Course ID
- Authorization 异常数据

自动化测试尽量避免依赖：

- 不稳定 DOM 位置
- 无必要的固定文章文本
- 随机不可预测数据

---

## 9. Entry Criteria

开始正式测试前应满足：

- GAD 可以成功启动
- `http://localhost:3000` 可以访问
- 主要测试页面可以进入
- Learning API 可以访问
- 测试工具已经安装
- 测试环境没有已知阻塞性故障

对于自动化测试：

- Python 环境可用
- pytest 依赖安装完成
- UI 测试环境具备可使用的浏览器
- CI 环境能够成功启动 GAD

---

## 10. Exit Criteria

本阶段测试满足以下条件后可以结束：

- 计划范围内的主要手工测试已经执行
- 核心功能已有明确 Pass / Fail 结果
- 已发现问题已经形成 Bug Report
- 已知问题具有对应回归场景
- API 自动化回归能够稳定执行
- UI 自动化回归能够稳定执行
- API CI 能够正常执行
- UI CI 能够正常执行
- 遗留问题和未测试范围已经明确记录
- 已形成测试总结报告

测试结束不代表系统不存在其他缺陷。

---

## 11. Defect Management

确认 Bug 时至少记录：

- Bug ID
- 标题
- 模块
- 前置条件
- 复现步骤
- 预期结果
- 实际结果
- 是否稳定复现
- 影响
- Severity
- Priority
- 当前状态

对于缺乏明确需求依据的问题：

不直接判定为正式 Bug。

可先记录为：

`OBSERVATION`

等待进一步确认。

---

## 12. Known Issues

当前已记录：

### BUG-001

Articles 刷新后当前分页恢复到第 1 页。

### BUG-002

Articles 刷新后 Items/Page 恢复为默认值 6。

### BUG-003

Articles 刷新后 Sort 恢复为默认排序。

三个问题均涉及页面刷新后的状态恢复。

目前根据黑盒测试结果分别记录，不能仅凭现象相似就确认其底层原因相同。

---

## 13. Risks

### Risk 1: Missing Formal PRD

项目没有完整正式 PRD。

影响：

部分预期只能根据 UI、API 和实际行为建立。

处理：

明确区分：

- 已确认需求
- 测试预期
- Observation
- 待确认需求

---

### Risk 2: Demo Data Dependency

部分测试依赖 GAD 内置测试数据。

如果上游项目修改默认数据：

自动化测试可能需要同步调整。

---

### Risk 3: UI Structure Changes

Playwright Locator 依赖页面可访问结构。

如果 DOM 或测试标识发生较大修改：

可能导致自动化脚本失败。

失败后需要区分：

- 产品缺陷
- UI 改版
- Locator 失效

---

### Risk 4: External Repository Dependency

GitHub Actions 会 Clone GAD 上游仓库。

如果：

- GAD 仓库不可访问
- npm 依赖安装失败
- GAD 启动方式发生变化

可能导致 CI 环境失败。

此类失败不能直接判断为产品功能缺陷。

---

### Risk 5: Limited Compatibility Coverage

当前 UI 自动化 CI 主要使用 Chromium。

因此当前测试结果不能代表：

- Firefox
- WebKit
- 所有 Chrome 版本
- 移动端浏览器

均已验证通过。

---

## 14. Current Regression Baseline

### API Automation

当前：

`21 passed`

覆盖：

- Authentication
- Auth Status
- Courses
- Course Progress

---

### UI Automation

当前正式回归集：

`7 tests`

基线：

`6 passed, 1 xfailed`

其中：

`UI-006`

对应已知 Items/Page 刷新状态问题。

---

## 15. CI Baseline

当前 GitHub Actions 已建立：

- API Tests
- UI Tests

API CI 已成功执行：

`21 passed`

UI CI 已成功执行回归测试。

---

## 16. Deliverables

本项目最终交付内容包括：

- Requirement Analysis
- Test Plan
- Manual Test Cases
- Bug Reports
- Test Summary
- API Automation
- UI Automation
- GitHub Actions CI
- README
- Git Repository

---

## 17. Test Conclusion Policy

测试结论应基于实际执行证据。

需要区分：

- PASS：实际结果符合预期
- FAIL：实际结果与明确测试预期不一致
- XFAIL：已知缺陷导致的预期失败
- OBSERVATION：发现异常现象，但缺少足够依据直接判定为 Bug

不得因为：

- 自动化脚本成功执行
- 页面没有崩溃
- HTTP 请求返回响应

就直接判定业务功能测试通过。
# Test Summary

## 1. Project Overview

本轮测试对象为 GAD（GUI/API Demo）。

当前阶段主要围绕 Articles 和 Users 模块进行功能测试、状态保持测试、探索性测试，并将部分稳定、高价值场景进一步转换为 UI 自动化回归。

---

## 2. Test Scope

本轮手工测试主要覆盖：

- Articles 列表基础展示
- Article 详情页跳转
- 列表页与详情页数据一致性
- Articles 分页
- Next / Prev 分页往返
- Users 列表基础信息展示
- 页面刷新后的分页状态
- 页面刷新后的 Items/Page 状态
- 页面刷新后的 Sort 状态
- Articles 配图重复现象检查

以下内容不在本轮手工测试总结范围内：

- 性能测试
- 压力测试
- 安全测试
- 多浏览器兼容性测试
- 移动端适配测试

---

## 3. Test Environment

测试环境：

- GAD 本地测试环境
- Base URL: `http://localhost:3000`
- Chrome 浏览器
- 手工功能测试
- Playwright UI 自动化回归
- pytest 自动化测试

---

## 4. Manual Test Results

本轮整理的主要手工测试共 9 个场景。

| Result | Count |
|---|---:|
| PASS | 5 |
| FAIL | 3 |
| OBSERVATION | 1 |
| Total | 9 |

### PASS

已验证通过的主要功能包括：

- Articles 列表正常加载
- Article 详情页正常跳转
- 列表页与详情页主要数据一致
- Next 分页正常
- Next → Prev 分页往返正常
- Users 列表基础信息正常展示

### FAIL

发现 3 个与页面刷新状态恢复相关的问题：

1. 当前分页刷新后恢复到第 1 页
2. Items/Page 刷新后恢复为默认值 6
3. Sort 刷新后恢复为默认排序方式

以上问题均可以稳定复现。

### OBSERVATION

发现部分不同文章使用相同展示图片。

由于目前没有明确需求证明不同文章必须使用不同图片，因此该问题暂时记录为观察项，不直接判定为 Bug。

---

## 5. Confirmed Bugs

当前确认并记录 3 个 Bug：

| Bug ID | Description | Status |
|---|---|---|
| BUG-001 | Articles 刷新后当前分页丢失 | Open |
| BUG-002 | Articles 刷新后 Items/Page 恢复默认值 | Open |
| BUG-003 | Articles 刷新后 Sort 排序状态丢失 | Open |

三个问题表现出相似特征：

> 用户在 Articles 页面进行的部分操作状态，在刷新页面后无法恢复。

从黑盒测试结果可以确认三个不同的用户可见问题。

目前没有足够证据确认三个问题是否由同一个底层缺陷导致，因此分别记录。

---

## 6. Regression Testing

针对测试过程中发现的问题进行了回归范围设计。

其中 Items/Page 刷新状态问题已经加入 UI 自动化回归测试。

该用例使用：

`pytest.mark.xfail(strict=True)`

当前结果为：

`XFAIL`

这表示：

- 缺陷仍然存在时，用例按已知缺陷管理
- 如果未来行为发生变化，需要重新确认该缺陷是否已修复
- 不会将已知缺陷误认为正常 PASS

---

## 7. UI Automation Result

当前 UI 自动化正式回归集共 7 个场景：

| ID | Scenario | Result |
|---|---|---|
| UI-001 | Articles 列表加载 | PASS |
| UI-002 | Articles Next 分页 | PASS |
| UI-003 | Article Detail 数据一致性 | PASS |
| UI-004 | Users 未认证访问拦截 | PASS |
| UI-005 | Users 登录后列表字段及头像检查 | PASS |
| UI-006 | Items/Page 刷新状态保持 | XFAIL |
| UI-007 | Articles Next → Prev 分页往返 | PASS |

当前回归基线：

`6 passed, 1 xfailed`

---

## 8. API Automation Result

API 自动化使用：

- Python
- pytest
- requests

目前共包含 21 个 pytest 测试实例。

主要覆盖：

- 登录成功
- 登录失败
- 空字段和缺失字段
- Authentication Status
- Courses 列表
- Course Detail
- 非法 Course ID
- Authorization 异常
- Course Progress

当前已有完整 API 自动化回归执行记录。

---

## 9. CI Status

项目已经接入 GitHub Actions。

当前 UI CI 可以自动完成：

1. Checkout 测试项目
2. 安装 Python 及测试依赖
3. 安装 Playwright Chromium
4. 安装 Node.js
5. Clone GAD
6. 安装 GAD 依赖
7. 启动 GAD
8. 等待测试环境可用
9. 执行 UI 自动化回归

首次 GitHub Actions CI 已成功运行。

因此 UI 自动化测试目前已经可以脱离本地人工启动测试流程，在 GitHub CI 环境中自动执行。

---

## 10. Risk Assessment

当前主要风险集中在 Articles 页面的状态保持能力。

用户修改以下状态后：

- Current Page
- Items/Page
- Sort

刷新页面会恢复为默认状态。

这不会阻止 Articles 基础浏览和分页功能使用，但会影响用户连续浏览体验。

尤其是在：

- 已浏览到较后分页
- 已修改每页显示数量
- 已选择特定排序方式

的情况下，页面刷新会导致用户需要重新进行操作。

---

## 11. Test Conclusion

本轮测试确认：

- Articles 和 Users 的主要基础功能可以正常使用
- Articles 分页和详情跳转功能正常
- 列表与详情主要数据能够保持一致
- Users 基础数据显示正常
- Articles 页面存在刷新后状态无法保持的问题

本轮测试同时完成了从手工测试到自动化回归的部分转换。

当前项目已经形成：

- 手工测试用例
- Bug Report
- API 自动化测试
- UI 自动化测试
- 已知缺陷回归管理
- GitHub Actions CI

后续仍可继续补充：

- 更多稳定 UI 回归场景
- API CI
- 测试数据管理
- 多浏览器测试
- 更完整的测试报告和项目展示内容
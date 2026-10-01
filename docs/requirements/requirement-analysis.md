# Requirement Analysis

## 1. Document Purpose

本文档用于整理 GAD 项目当前测试范围内的功能需求、可观察行为、测试边界和风险点。

本项目以黑盒测试为主。

测试过程中没有使用正式 PRD 作为唯一需求来源，因此本文档将内容区分为：

- 已确认的系统行为
- 基于界面和接口设计得到的测试预期
- 目前无法确认的需求

避免把测试人员的推测直接当作正式产品需求。

---

## 2. System Under Test

测试对象：

GAD（GUI/API Demo）

本地测试地址：

`http://localhost:3000`

当前主要测试范围包括：

- Articles
- Article Detail
- Users
- Authentication
- Learning API

---

## 3. Requirement Sources

当前需求分析主要依据：

1. GAD 实际页面和接口行为
2. 页面中的可操作控件
3. API 返回结果
4. 测试执行过程中观察到的系统行为
5. 已完成的手工测试和自动化测试

由于没有正式业务 PRD，因此对于没有明确依据的行为，不直接定义为强制需求。

---

# 4. Articles Requirements

## ART-REQ-001 Articles 列表展示

Articles 页面应能够展示文章列表。

列表中的文章应包含可识别的文章信息，例如：

- 标题
- 作者
- 相关展示内容

### Current Verification

已通过手工测试和 UI 自动化验证。

---

## ART-REQ-002 Article Detail 跳转

用户应能够从 Articles 列表进入对应文章详情页。

进入详情页后：

- 应显示对应文章
- 文章标题应与列表中选择的文章一致
- 作者等主要关联信息应保持一致

### Current Verification

已通过手工测试和 UI 自动化验证。

---

## ART-REQ-003 Articles 分页

Articles 页面支持分页浏览。

用户点击：

`Next`

后，应进入下一页。

用户点击：

`Prev`

后，应返回上一页。

分页后：

- 页码应发生对应变化
- 当前显示的文章集合应发生对应变化
- 返回上一页后应能够恢复该页对应数据

### Current Verification

已通过手工测试和 UI 自动化验证。

---

## ART-REQ-004 Items/Page

Articles 页面提供 Items/Page 控件。

用户修改该控件后，每页显示的文章数量应按照选择值发生变化。

### Current Verification

修改后的即时行为已验证正常。

---

## ART-REQ-005 Sort

Articles 页面提供 Sort 功能。

用户修改排序方式后，文章列表应按照当前选择的排序条件重新排列。

### Current Verification

修改后的即时排序行为已进行手工验证。

---

## ART-REQ-006 页面刷新后的状态恢复

测试中观察到以下状态：

- Current Page
- Items/Page
- Sort

在刷新页面后均恢复为默认状态。

从用户体验角度，本项目测试时采用的预期是：

> 页面刷新后应保持用户刷新前的当前浏览状态。

因此当前分别记录了：

- BUG-001 Current Page 状态丢失
- BUG-002 Items/Page 状态丢失
- BUG-003 Sort 状态丢失

### Requirement Limitation

当前没有正式 PRD 明确规定这些状态必须在浏览器刷新后保持。

因此：

- 可以确认当前行为与本项目测试预期不一致
- 可以确认其对连续浏览体验产生影响
- 但若进入真实企业项目，最终是否判定为正式产品缺陷，需要产品需求或产品负责人确认

---

## ART-REQ-007 Article Image

测试过程中发现部分不同文章使用了相同展示图片。

目前没有正式需求证明：

> 每篇文章必须使用不同图片。

因此该行为目前仅记录为：

`OBSERVATION`

不直接作为确认缺陷。

---

# 5. Users Requirements

## USER-REQ-001 未认证访问控制

未登录用户访问 Users 页面时，应受到认证限制。

页面应提示用户需要：

- Login
- 或 Register

才能访问相关内容。

### Current Verification

已通过 UI 自动化验证。

---

## USER-REQ-002 登录后访问 Users

有效用户完成登录后，应能够访问 Users 页面。

### Current Verification

已通过 UI 自动化验证。

---

## USER-REQ-003 Users 列表展示

认证成功后，Users 页面应正常显示用户列表。

当前测试关注字段包括：

- ID
- First Name
- Last Name
- Email
- Avatar
- User Detail Link

字段应能够正常显示。

### Current Verification

已通过手工测试和 UI 自动化验证。

---

## USER-REQ-004 Avatar 加载

Users 页面中的头像不仅应存在图片地址，还应能够实际加载。

因此自动化测试不仅检查：

`src`

还检查图片实际加载状态。

### Current Verification

已通过 UI 自动化验证。

---

# 6. API Requirements

## API-REQ-001 Login Success

使用有效账号登录时：

- HTTP Status 应为 200
- 返回结果应表示登录成功
- 应返回 access token
- 应返回用户标识信息

### Current Verification

已通过 API 自动化验证。

---

## API-REQ-002 Invalid Login

错误用户名或错误密码登录时：

- 应拒绝认证
- 当前系统返回 HTTP 401
- 当前错误信息为 `Invalid credentials`

### Current Verification

已通过参数化 API 自动化验证。

---

## API-REQ-003 Missing Login Fields

Login 请求出现以下情况时应被拒绝：

- username 为空
- password 为空
- 缺少 username
- 缺少 password
- 请求体缺少全部登录字段

### Current Verification

已通过 API 自动化验证。

---

## API-REQ-004 Authentication Status

Authentication Status 接口应能够区分：

- 未认证用户
- 已认证用户

有效认证后返回结果应能够关联当前用户。

### Current Verification

已通过 API 自动化验证。

---

## API-REQ-005 Courses List

Courses 接口应能够返回课程列表。

返回结果应：

- HTTP 200
- 为列表结构
- 至少包含课程数据

### Current Verification

已通过 API 自动化验证。

---

## API-REQ-006 Course Detail

有效 Course ID 应能够获取对应课程详情。

返回数据应包含：

- Course ID
- Title 等课程信息

### Current Verification

已通过 API 自动化验证。

---

## API-REQ-007 Invalid Course ID

无效 Course ID 应被正确处理。

当前覆盖：

- 不存在的大 ID
- 0
- 负数
- 非数字 ID

当前系统返回：

- HTTP 404
- `Course not found`

### Current Verification

已通过参数化 API 自动化验证。

---

## API-REQ-008 Course Progress Authorization

Course Progress 接口需要有效认证。

当前测试覆盖：

- 缺少 Authorization
- 不完整 Bearer
- 错误认证 Scheme
- 无效 Token
- 有效 Token

无效认证请求应被拒绝。

有效认证并满足课程条件后，应能够获取 Progress。

### Current Verification

已通过 API 自动化验证。

---

# 7. Test Scope

## In Scope

当前项目主要覆盖：

- Articles 基础浏览
- Article Detail
- Pagination
- Items/Page
- Sort
- Users Authentication
- Users List
- Login API
- Authentication Status API
- Courses API
- Course Progress API
- 手工功能测试
- API 自动化
- UI 自动化
- CI 回归

---

## Out of Scope

当前阶段未系统覆盖：

- 性能测试
- 压力测试
- 安全渗透测试
- 数据库完整性专项测试
- 移动端专项测试
- 大规模兼容性测试
- 无障碍专项测试
- 网络异常专项测试
- 长时间稳定性测试

这些内容不应被理解为已经验证通过。

---

# 8. Main Risk Areas

当前识别的主要风险包括：

## 8.1 Articles 状态保持

以下状态刷新后会丢失：

- Current Page
- Items/Page
- Sort

可能影响用户连续浏览体验。

---

## 8.2 Authentication

Users 和 Course Progress 等功能依赖认证状态。

需要重点关注：

- 未登录访问
- 无效 Token
- Token 格式
- 登录状态

---

## 8.3 Dynamic UI Data

Articles 和 Users 页面数据属于动态页面内容。

自动化测试需要避免：

- 过度依赖固定文本
- 依赖不稳定 DOM 位置
- 使用固定 sleep 等待动态内容

---

# 9. Requirement Traceability

| Requirement | Manual Test | Automation |
|---|---|---|
| ART-REQ-001 | MT-ART-001 | UI-001 |
| ART-REQ-002 | MT-ART-002 | UI-003 |
| ART-REQ-003 | MT-ART-003 / MT-ART-004 | UI-002 / UI-007 |
| ART-REQ-004 | MT-ART-006 | UI-006 |
| ART-REQ-005 | MT-ART-007 | Not automated |
| ART-REQ-006 | MT-ART-005 / 006 / 007 | Partial |
| ART-REQ-007 | MT-ART-008 | Manual observation |
| USER-REQ-001 | Manual verification | UI-004 |
| USER-REQ-002 | Manual verification | UI-005 |
| USER-REQ-003 | MT-USER-001 | UI-005 |
| USER-REQ-004 | Manual verification | UI-005 |
| API-REQ-001 | API manual testing | Automated |
| API-REQ-002 | API manual testing | Automated |
| API-REQ-003 | API manual testing | Automated |
| API-REQ-004 | API manual testing | Automated |
| API-REQ-005 | API manual testing | Automated |
| API-REQ-006 | API manual testing | Automated |
| API-REQ-007 | API manual testing | Automated |
| API-REQ-008 | API manual testing | Automated |

---

# 10. Conclusion

当前需求分析已经覆盖本项目主要测试对象。

由于本项目没有正式 PRD，测试过程中需要始终区分：

- 系统当前实际行为
- 可以明确验证的功能
- 测试人员提出的预期
- 尚需产品确认的需求

后续测试计划、测试用例和 Bug Report 均以该范围为基础进行组织。
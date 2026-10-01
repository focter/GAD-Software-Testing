# Bug Reports

本文件记录 GAD 项目手工测试过程中确认的问题。

---

## BUG-001 Articles 刷新后当前分页丢失

**模块：** Articles  
**类型：** 状态保持 / 分页  
**状态：** Open
**Severity：** Minor  
**Priority：** Medium

### 前置条件

- GAD 已正常启动
- Articles 页面存在多页文章数据

### 测试步骤

1. 打开 Articles 页面
2. 通过分页操作进入第 5 页
3. 确认当前显示第 5 页内容
4. 刷新浏览器页面
5. 观察刷新后的页码和文章列表

### 预期结果

刷新页面后，应保持用户刷新前所在的第 5 页。

### 实际结果

刷新后页面恢复到第 1 页。

进一步测试其他分页后发现：

- 在不同页执行刷新均会恢复至第 1 页
- 分页操作前后浏览器 URL 保持一致
- URL 中没有体现当前页码状态

### 是否稳定复现

是。

### 影响

用户在浏览较后页面时刷新网页，会失去当前浏览位置，需要重新进行分页操作。

### 关联测试用例

`MT-ART-005`

### 备注

当前仅确认了用户可见行为。

分页状态具体应通过 URL、前端状态、Session Storage、Local Storage 或其他方式保存，需要结合产品设计和实现进一步判断。

---

## BUG-002 Articles 刷新后 Items/Page 恢复默认值

**模块：** Articles  
**类型：** 状态保持 / 列表设置  
**状态：** Open
**Severity：** Minor  
**Priority：** Medium

### 前置条件

- GAD 已正常启动
- Articles 默认 Items/Page 为 6

### 测试步骤

1. 打开 Articles 页面
2. 修改 Items/Page
3. 确认文章列表数量按照新设置发生变化
4. 刷新浏览器页面
5. 检查刷新后的 Items/Page

### 预期结果

刷新页面后，应继续保持用户刷新前选择的 Items/Page。

### 实际结果

修改 Items/Page 后设置立即生效。

刷新页面后：

`Items/Page = 6`

恢复为初始默认值，用户设置没有被保留。

### 是否稳定复现

是。

### 影响

用户修改每页文章数量后，只要刷新页面就需要重新设置。

### 关联测试用例

`MT-ART-006`

### 自动化回归

该问题目前已经加入 UI 自动化回归。

对应测试使用：

`pytest.mark.xfail(strict=True)`

当前预期状态为 XFAIL。

当该缺陷被修复后，用例结果会发生变化，从而提示重新检查该问题。

---

## BUG-003 Articles 刷新后 Sort 排序状态丢失

**模块：** Articles  
**类型：** 状态保持 / 排序  
**状态：** Open
**Severity：** Minor  
**Priority：** Medium

### 前置条件

- GAD 已正常启动
- Articles 页面支持修改 Sort

### 测试步骤

1. 打开 Articles 页面
2. 修改 Sort 排序方式
3. 确认文章列表排序发生变化
4. 刷新浏览器页面
5. 检查刷新后的 Sort 选项和文章顺序

### 预期结果

刷新页面后，应继续保持用户刷新前选择的排序方式。

### 实际结果

刷新后 Sort 恢复为初始默认排序方式，即按日期排序。

用户设置的排序状态没有被保留。

### 是否稳定复现

是。

### 影响

用户修改文章排序方式后，刷新页面会丢失当前排序条件，需要重新设置。

### 关联测试用例

`MT-ART-007`

---

# Bug Summary

| Bug ID | Description | Severity | Priority | Reproducible | Status |
|---|---|---|---|---:|---|
| BUG-001 | 刷新后当前分页恢复到第 1 页 | Minor | Medium | Yes | Open |
| BUG-002 | 刷新后 Items/Page 恢复为 6 | Minor | Medium | Yes | Open |
| BUG-003 | 刷新后 Sort 恢复默认排序 | Minor | Medium | Yes | Open |

三个问题具有共同现象：

> Articles 页面中的用户操作状态在浏览器刷新后没有被恢复。

目前根据黑盒测试结果，可以确认三个用户可见问题。

是否由同一个底层状态管理机制导致，需要结合实现进一步分析，因此当前分别记录为三个 Bug。
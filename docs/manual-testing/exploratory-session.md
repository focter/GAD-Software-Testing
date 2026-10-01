# Exploratory Testing Session

## Session Title

Articles 页面浏览、分页与刷新状态探索

---

## 1. Session Charter

探索 Articles 页面在正常浏览过程中的异常行为，重点关注：

- 文章列表展示
- 分页操作
- 页面刷新
- Items/Page
- Sort
- 图片展示
- 用户操作状态是否能够保持

本次测试不限定为固定测试用例，允许根据测试过程中发现的现象继续扩展测试方向。

---

## 2. Test Object

测试对象：

`GAD Articles`

测试页面：

`http://localhost:3000/articles.html`

---

## 3. Test Method

采用探索性测试方式。

基本过程：

1. 浏览 Articles 页面
2. 观察文章列表和图片
3. 根据发现的异常现象继续操作
4. 修改分页、Items/Page、Sort
5. 使用浏览器刷新验证状态
6. 对发现的问题进行重复复现
7. 将稳定问题转入正式 Bug 和回归测试

---

## 4. Session Notes

### 4.1 Articles 图片观察

浏览不同 Articles 时，发现：

- 不同文章存在相同展示图片
- 文章标题等其他内容不同
- 图片重复现象能够被观察到

进一步分析后发现：

当前没有明确需求证明：

`不同文章必须使用不同图片`

因此不能仅根据图片重复直接判断为产品 Bug。

处理结果：

`OBSERVATION`

---

### 4.2 Pagination Refresh

在浏览 Articles 分页过程中：

1. 进入后续页面
2. 停留在当前分页
3. 刷新浏览器
4. 页面恢复到第 1 页

进一步尝试多个分页后发现：

该行为可以稳定复现。

同时观察到：

分页前后 URL 没有记录当前页状态。

处理结果：

记录为：

`BUG-001`

---

### 4.3 Items/Page Refresh

继续探索列表设置。

操作：

1. 修改 Items/Page
2. 确认页面文章数量发生变化
3. 刷新页面
4. 再次观察 Items/Page

发现：

刷新后 Items/Page 恢复为默认值：

`6`

重复测试后行为稳定。

处理结果：

记录为：

`BUG-002`

---

### 4.4 Sort Refresh

继续测试与列表状态相关的其他控件。

操作：

1. 修改 Sort
2. 确认文章顺序发生变化
3. 刷新页面
4. 检查 Sort 状态

发现：

刷新后 Sort 恢复为默认排序方式。

重复测试后行为稳定。

处理结果：

记录为：

`BUG-003`

---

## 5. Findings

本次探索测试得到 4 个主要发现：

| Finding | Type | Result |
|---|---|---|
| 不同文章可能使用相同图片 | Observation | 待需求确认 |
| 当前分页刷新后丢失 | Bug | BUG-001 |
| Items/Page 刷新后丢失 | Bug | BUG-002 |
| Sort 刷新后丢失 | Bug | BUG-003 |

---

## 6. Follow-up Testing

对于三个状态保持问题进行了进一步验证：

- 多次重复操作
- 在不同分页下刷新
- 修改 Items/Page 后刷新
- 修改 Sort 后刷新

三个问题均能够稳定复现。

其中：

`BUG-002 Items/Page`

后续已经加入 UI 自动化回归，并通过：

`pytest.mark.xfail(strict=True)`

管理已知缺陷。

---

## 7. Testing Decisions

### 图片重复问题

未直接判为 Bug。

原因：

缺少明确需求说明不同文章必须拥有不同图片。

因此记录为：

`OBSERVATION`

---

### Refresh State Issues

分页、Items/Page 和 Sort 刷新后状态丢失均属于用户可观察行为。

本项目采用的测试预期为：

页面刷新后应恢复用户刷新前的浏览状态。

因此分别记录为三个问题。

由于仅进行黑盒测试，目前不能确认：

- 三个问题是否具有同一个技术根因
- 状态应该存储于 URL、Local Storage、Session Storage 或其他位置

不对实现原因作未经验证的结论。

---

## 8. Session Outcome

本次探索性测试从最初的 Articles 列表浏览开始，通过测试过程中的动态观察逐步扩展到：

`图片 → 分页 → 刷新 → Items/Page → Sort`

最终形成：

- 1 个 Observation
- 3 个稳定复现 Bug
- 相关回归测试
- 1 个已进入 UI 自动化的已知缺陷场景

该过程体现了探索性测试的特点：

测试方向不是完全预先固定，而是根据实际发现不断调整和深入。

---

## 9. Limitations

本次 Session 未记录精确的：

- 开始时间
- 结束时间
- Session 持续时长

因此文档中不补造时间数据。

本记录重点保留：

- 测试目标
- 探索路径
- 实际发现
- 后续处理
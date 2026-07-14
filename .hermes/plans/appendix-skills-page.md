# 新增附录页：工作坊 Hermes 技能清单

> **Goal:** 在 V10 版本 deck 中新增一个附录页（第 40 页），列出并解析 Steven 本次工作坊会用到的两个 Hermes 技能（`huashu-design`、`reddit-community-research`），说明它们的工作流程原理，并提供可下载 / 安装的链接。

---

## 当前上下文

- V10 版本 deck 路径：`/workspace/0715_PM_Workshop_v10/`
- 当前总页数：39 页（`slides/01-cover.html` 至 `slides/39-resources.html`）
- 新附录页计划作为第 40 页，放在所有页面之后
- 两个技能已确认存在于用户当前 Hermes 环境中

## 技能信息摘要

### 1. huashu-design（花叔 Design）
- **来源**：公开仓库 `alchaincyf/huashu-design`
- **作用**：用 HTML 做高保真原型、交互 Demo、幻灯片、动画、设计变体探索和专家评审
- **核心工作流**：理解需求 → 事实验证 → 资产收集 → 多方向视觉探索 → 原型交付 → 验证
- **下载链接**：`https://github.com/alchaincyf/huashu-design`

### 2. reddit-community-research
- **来源**：本地 Hermes 安装路径 `/home/hermeswebui/.hermes/skills/research/reddit-community-research`
- **远程**：`git remote` 指向 `https://github.com/hermes-skills/reddit-community-research.git`
- **GitHub 页面检查**：`hermes-skills` 组织页面显示 "doesn't have any public repositories yet"，可能仓库为私有或不存在公开页面
- **作用**：系统性爬取 Reddit 社区数据，提取痛点、情绪信号、功能需求优先级
- **核心工作流**：确认目标 → 环境检查 → 用 pullpush.io 爬取 → 数据结构化 → 观点整合 → 报告交付
- **下载链接**：待确认，候选为 `https://github.com/hermes-skills/reddit-community-research`（需用户确认可访问性）

---

## 执行计划

### Task 1: 确认下载链接可访问性
**Objective:** 验证两个技能仓库链接是否可访问，避免听众点击后 404。

**Files:**
- 检查：`https://github.com/alchaincyf/huashu-design`
- 检查：`https://github.com/hermes-skills/reddit-community-research`

**Step 1:** 用 `mcp_fetch` 或 GitHub API 检查 `alchaincyf/huashu-design` 是否可访问。  
**Step 2:** 用 `mcp_fetch` 或 GitHub API 检查 `hermes-skills/reddit-community-research` 是否可访问。  
**Step 3:** 如果后者不可访问，询问用户是否有替代链接（如私有仓库、fork 地址等）。

---

### Task 2: 创建附录页 HTML 文件
**Objective:** 新增 `slides/40-appendix-skills.html`，风格与现有 deck 一致。

**Files:**
- 创建：`/workspace/0715_PM_Workshop_v10/slides/40-appendix-skills.html`

**内容结构：**
1. 顶部 page-masthead：`AI 工具深度应用` + `40 / 40 · 附录`
2. 标题：`附录 A · 本次工作坊会用到的 Hermes 技能`
3. 两个技能卡片，每个包含：
   - 技能名称与图标
   - 一句话简介
   - 工作流程原理（3-4 步）
   - 适用场景
   - 下载 / 安装链接（按钮样式）
4. 底部说明：如何安装 Hermes skill（将仓库 clone 到 `~/.hermes/skills/<category>/<skill-name>/`）
5. page-footer：`附录 · Hermes 技能`

**样式要求：**
- 使用 `shared/tokens.css`
- 与 37-resources 页风格一致，但突出"附录"属性
- 链接使用可识别按钮样式

---

### Task 3: 更新 index.html manifest
**Objective:** 将第 40 页加入 deck 导航。

**Files:**
- 修改：`/workspace/0715_PM_Workshop_v10/index.html`

**Step 1:** 在 `DECK_MANIFEST` 数组末尾添加第 40 项。  
**Step 2:** 确认 manifest 总数为 40。

---

### Task 4: 更新所有 slide 的总页数
**Objective:** 将 39 页改为 40 页。

**Files:**
- 修改：`/workspace/0715_PM_Workshop_v10/slides/*.html`（所有现有页面）

**Step 1:** 用脚本批量替换所有 `X / 39` 为 `X / 40`。  
**Step 2:** 检查 39-resources.html 的 page-masthead 和 footer 是否同步更新。

---

### Task 5: 本地验证与推送
**Objective:** 确保页面正常渲染并发布到 GitHub Pages。

**Files:**
- 无需新文件，验证已有文件

**Step 1:** 用浏览器或 `mcp_fetch` 检查第 40 页内容是否完整。  
**Step 2:** 确认导航可以从第 39 页翻到第 40 页。  
**Step 3:** 提交并 push 到 `dongtonghui/hermes-pm-deck-v10`。

---

## 风险与注意事项

1. **链接有效性**：`hermes-skills/reddit-community-research` 公开页面可能无法访问，需要确认。
2. **页码同步**：新增一页后，所有现有页码都需要更新，避免不一致。
3. **安装说明**：如果听众没有用过 Hermes，需要简要说明 skill 安装路径。

## 依赖信息

- `huashu-design` 仓库：可公开访问
- `reddit-community-research` 仓库：需确认公开可访问性

## 下一步

确认 `reddit-community-research` 公开链接后，即可执行 Task 2-5。
